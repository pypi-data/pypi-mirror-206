# -*- coding: utf-8 -*-
import datetime
import itertools
import os
from typing import List, Optional

import fasttext
import hao
import numpy as np
from hao.namespaces import attr, from_args
from hao.stopwatch import Stopwatch
from sklearn.metrics import classification_report

LOGGER = hao.logs.get_logger(__name__)


PARAM_MAPPING = {
    'train_file': 'input',
    'val_file': 'autotuneValidationFile',
    'tune_time': 'autotuneDuration',
    'tune_size': 'autotuneModelSize',
    'pretrained_file': 'pretrainedVectors',
    'min_count': 'minCount',
    'ngram': 'wordNgrams',
}
FILE_SKIP_ATTR = ('pretrained_file', 'train_file', 'val_file', 'tune_time', 'tune_size')

@from_args(config='tailors.yml')
class TrainConf(object):
    task: str = attr(str, help='task name in tailors.yml')
    exp: str = attr(str, key='tasks.{task}.exp', required=True, help='experiment name')
    dataset: str = attr(str, key='tasks.{task}.dataset', required=True, help='datasets.{dataset} in tailors.yml')
    tune_time: int = attr(int, key='tasks.{task}.tune_time', default=600, help='auto tune duration in seconds')
    tune_size: str = attr(str, key='tasks.{task}.tune_size', default="100M", help='auto tune model size')
    lr: list = attr(List[float], key='tasks.{task}.lr', default=[])
    dim: list = attr(List[int], default=[50])
    ws: list = attr(List[int], default=[], help="window size")
    epoch: list = attr(List[int], key='tasks.{task}.epoch', default=[])
    neg: list = attr(List[int], key='tasks.{task}.neg', default=[])
    min_count: list = attr(List[int], key='tasks.{task}.min_count', default=[30])
    ngram: list = attr(List[int], key='tasks.{task}.ngram', default=[3])
    minn: list = attr(List[int], default=[])
    maxn: list = attr(List[int], default=[])
    loss: list = attr(List[str], key='tasks.{task}.loss', choices=('ns', 'hs', 'softmax', 'ova'), default=[])
    k: int = attr(int, default=1, key='tasks.{task}.k', help='top k')
    threshold: float = attr(float, key='tasks.{task}.threshold', default=0.0, help='threshold for top k')
    pretrained: str = attr(str, key='tasks.{task}.pretrained')


def train(conf: Optional[TrainConf] = None):
    conf = conf or TrainConf()
    LOGGER.info(conf)

    dataset = hao.config.get(f"datasets.{conf.dataset}", config='tailors.yml')
    datasets = dataset.get('datasets')
    train_file = hao.paths.get(datasets.get('train'))
    val_file = hao.paths.get(datasets.get('val'))
    labels = dataset.get('meta', {}).get('labels')
    if labels is None:
        labels = get_labels_from_dataset([train_file, val_file])

    pretrained_file = hao.paths.get(conf.pretrained)
    k = conf.k
    threshold = conf.threshold

    results = []
    for lr, dim, epoch, ws, neg, min_count, ngram, minn, maxn, loss in itertools.product(
        _params(conf, 'lr'),
        _params(conf, 'dim'),
        _params(conf, 'epoch'),
        _params(conf, 'ws'),
        _params(conf, 'neg'),
        _params(conf, 'min_count'),
        _params(conf, 'ngram'),
        _params(conf, 'minn'),
        _params(conf, 'maxn'),
        _params(conf, 'loss'),
    ):
        params = {
            'pretrained_file': pretrained_file,
            'train_file': train_file,
            'val_file': val_file,
            'tune_time': conf.tune_time,
            'tune_size': conf.tune_size,
            'lr': lr,
            'dim': dim,
            'epoch': epoch,
            'ws': ws,
            'neg': neg,
            'min_count': min_count,
            'ngram': ngram,
            'minn': minn,
            'maxn': maxn,
            'loss': loss,
        }
        model_name, f1 = train_and_val(conf.exp, k, threshold, labels, **params)
        results.append((model_name, f1))
    return results


def _params(conf: TrainConf, field: str) -> list:
    v = getattr(conf, field)
    if v is None or isinstance(v, list):
        return v or [None]
    return [v]


def get_labels_from_dataset(files: list):
    assert len(files) > 0
    labels = set()
    for file in files:
        with open(file) as f:
            for line in f:
                splits = line.split('__label__')
                for s in splits[1:]:
                    labels.add(s.strip())
    return list(labels)


def train_and_val(exp: str, k, threshold, labels_all, **kwargs):
    params = {PARAM_MAPPING.get(k, k): v for k, v in kwargs.items() if v}
    LOGGER.info(f'train: \n{hao.jsons.prettify(params)}')

    sw = Stopwatch()
    date = datetime.datetime.now().strftime('%y%m%d-%H%M')
    model = fasttext.train_supervised(**params)
    LOGGER.info(f"vocab size: {len(model.words)}")
    LOGGER.info(f"labels: {[label[9:] for label in model.labels]}")

    file_val = kwargs.get('val_file')
    n, precision, recall = model.test(file_val, k=k, threshold=threshold)
    f1 = 2 * precision * recall / (precision + recall)
    LOGGER.info(f"val size: {n}, precision: {precision:.4}, recall: {recall:.4}, f1: {f1:.4}")

    model_params = '-'.join([
        f'{k}={v}' for k, v in kwargs.items()
        if k not in FILE_SKIP_ATTR and v is not None
    ])
    model_file = f'data/model/{exp}-{date}-{model_params}-f1={f1:.4}.bin'
    model_path = hao.paths.get(model_file)
    hao.paths.make_parent_dirs(model_path)
    model.save_model(model_path)

    for att in ('lr', 'dim', 'epoch', 'ws', 'neg', 'minCount', 'wordNgrams', 'minn', 'maxn'):
        LOGGER.info(f'{att: >25}: {getattr(model, att)}')

    lines = open(file_val).readlines()
    splits = [line.split('__label__') for line in lines]
    text, labels = list(zip(*[(s[0].strip(), [l.strip() for l in s[1:]]) for s in splits]))
    preds = [[p[9:] for p in prediction] for prediction in model.predict(list(text), k=k, threshold=threshold)[0]]
    indices_true = to_indices(labels, labels_all)
    indices_pred = to_indices(preds, labels_all)
    report = classification_report(indices_true, indices_pred, target_names=labels_all, digits=4, zero_division=0)
    LOGGER.info(f"\n{' classification report '.center(60, '=')}\n{report}")
    size = round(os.path.getsize(model_path) / (1024*1024), 2)
    LOGGER.info(f'model saved to: {model_file}, size: {size}')

    LOGGER.info(f'took: {sw.took()}')
    return model_file, f1


def to_indices(entries: List[list], labels):
    indices_labels = []
    for items in entries:
        indices = [0 for _ in labels]
        for label in items:
            if label in labels:
                indices[labels.index(label)] = 1
        indices_labels.append(indices)
    return np.array(indices_labels)


if __name__ == '__main__':
    try:
        train()
    except KeyboardInterrupt:
        print('[ctrl-c] stopped')
    except Exception as err:
        LOGGER.exception(err)
