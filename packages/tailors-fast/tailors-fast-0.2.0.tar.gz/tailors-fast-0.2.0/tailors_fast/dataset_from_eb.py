# -*- coding: utf-8 -*-
import json
import os
import random
from collections import defaultdict
from typing import List, Optional

import hao
import requests
from hao.namespaces import attr, from_args
from tqdm import tqdm

from tailors_fast.tokenizer import JiebaTokenizer

LOGGER = hao.logs.get_logger(__name__)


@from_args
class Conf:
    task: str = attr(str, required=True, help='task name')
    token: str = attr(str, help='task token or user token in eb', secret=True)
    format: str = attr(str, choices=['raw', 'neat'], default='raw')
    selection: str = attr(str, choices=('annotated', 'reviewed', 'all'), default='annotated')
    cases: bool = attr(bool, default=True)
    cases_factor: int = attr(int, default=2, help='n duplicates of the cases')
    cases_starts: int = attr(int, help='No. from which are all cases')
    ignore_by: str = attr(str, help='ignore items annotated by user')
    seed: int = attr(int)
    type: str = attr(str, choices=('SLC', 'MLC'), help='task types')
    endpoint: str = attr(str, default='http://bjb.bl-ai.com')


def process(conf: Optional[Conf] = None):
    sw = hao.stopwatch.Stopwatch()
    conf = conf or Conf()
    LOGGER.info(conf)

    tokenizer = JiebaTokenizer()
    labels = get_labels(conf)
    items = get_items(conf)
    items_cases = get_items(conf, is_cases=True) if conf.cases and not conf.task.endswith('cases') else []
    items_train, items_val = group_split(conf, items, items_cases)

    dataset = {'train': items_train, 'val': items_val}
    log_summary(conf, dataset, labels)
    msgs = [save_to_file(conf, tokenizer, split, items) for split, items in dataset.items()]
    LOGGER.info(f'done, took: {sw.took()}')
    for msg in msgs:
        LOGGER.info(msg)


def get_labels(conf: Conf):
    labels_path = hao.paths.get(f"data/raw/{conf.task}-labels.json")
    if os.path.exists(labels_path):
        return json.loads(open(labels_path).read())

    headers = {'API-Token': conf.token}
    url = f"{conf.endpoint}/api/task/{conf.task}/tags"
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    hao.paths.make_parent_dirs(labels_path)
    data = res.json().get('data')
    labels = {
        label: {tag.get('name'): tag.get('description') for tag in tags.get('tags')}
        for label, tags in data.items()
    }

    with open(labels_path, 'w') as f:
        f.write(hao.jsons.prettify(labels))
        LOGGER.info(f"[labels] saving to: {labels_path}")

    if len(labels) == 1:
        dataset_labels = next(iter(labels.values()))
    else:
        dataset_labels = labels.get(conf.type)
    if dataset_labels:
        dataset_labels_path = hao.paths.get(f"data/dataset/{conf.task}/labels.json")
        hao.paths.make_parent_dirs(dataset_labels_path)
        with open(dataset_labels_path, 'w') as f:
            f.write(hao.jsons.prettify(dataset_labels))
            LOGGER.info(f"[labels dataset] saving to: {dataset_labels_path}")

    return labels


def get_items(conf: Conf, *, is_cases: bool = False):
    def qualified(item):
        if item.get('enabled') == False:
            return False
        if item.get('editor_timestamp') is None:
            return False
        if conf.ignore_by is not None and item.get('editor') == conf.ignore_by:
            return False
        return True

    task = f"{conf.task}-cases" if is_cases else conf.task
    dataset_raw_path = hao.paths.get(f"data/raw/{task}.jsonl")

    if os.path.exists(dataset_raw_path):
        items = open(dataset_raw_path).readlines()
        items = [json.loads(item) for item in items]

    else:
        headers = {'API-Token': conf.token}
        url = f"{conf.endpoint}/api/task/export?name={task}&format={conf.format}&selection={conf.selection}&zip=false"
        res = requests.get(url, headers=headers)
        res.raise_for_status()

        contents = res.text.splitlines()
        if len(contents) == 1 and json.loads(contents[0]).get('message') is not None:
            LOGGER.error(f"[{task}] {res.text}")
            return []

        hao.paths.make_parent_dirs(dataset_raw_path)
        LOGGER.info(f"[raw.jsonl] saving to: {dataset_raw_path}")

        with open(dataset_raw_path, 'w') as f:
            f.write(res.text)
        items = res.text.splitlines()
        items = [json.loads(item) for item in items]

    return list(filter(qualified, items))


def group_split(conf: Conf, items_general: list, items_cases: list):
    items_train = [item for item in items_general if item.get('splits', {}).get(conf.seed) == 'train']
    items_val = [item for item in items_general if item.get('splits', {}).get(conf.seed) == 'val']
    items_general = [item for item in items_general if item.get('splits', {}).get(conf.seed) not in ('train', 'val')]

    if conf.cases_starts:
        _items_cases = items_general[conf.cases_starts:]
        items_cases.extend(_items_cases)
        items_general = items_general[:conf.cases_starts]

    groups = defaultdict(list)
    for item in items_general:
        annotation = item.get('annotation', {})
        label = annotation.get('SLC')
        labels = annotation.get('MLC')
        if conf.seed:
            random.seed(conf.seed)
        label = label or random.choice(labels)
        groups[label].append(item)

    items_train, items_val = [], []
    for items in groups.values():
        if conf.seed:
            random.seed(conf.seed)
            random.shuffle(items)
        i = len(items) * 8 // 10
        items_train.extend(items[:i])
        items_val.extend(items[i:])
    items_train.extend(items_cases * conf.cases_factor)
    return items_train, items_val


def convert(conf: Conf, items: list, tokenizer: JiebaTokenizer):
    def transform(e):
        text = e.get('text')
        annotation = e.get('annotation')
        if len(annotation) == 0:
            return

        text = ' '.join([tokenizer.cut_and_join(line) for line in text])
        if len(annotation) == 1:
            labels = next(iter(annotation.values()))
        else:
            labels = annotation.get(conf.type)
        if isinstance(labels, str):
            labels = [labels]
        labels = ' '.join([f"__label__{label}" for label in labels])
        return f"{text} {labels}"
    return list(filter(None, [transform(item) for item in items]))


def convert_to_json(items: list):
    def transform(e):
        annotation = e.get('annotation')
        if annotation is None or len(annotation) == 0:
            return

        label, labels = annotation.get('SLC'), annotation.get('MLC')
        data = {
            'uid': e.get('uid'),
            'es_id': e.get('es_id'),
            'caption': e.get('caption'),
            'text': e.get('text'),
            'html': e.get('html'),
            'label': label,
            'labels': labels,
            'splits': e.get('splits')
        }
        return hao.jsons.dumps({k: v for k, v in data.items() if v is not None})
    return list(filter(None, [transform(item) for item in items]))


def save_to_file(conf: Conf, tokenizer: JiebaTokenizer, split: str, items: List[dict]):
    filepath_json = f"data/dataset/{conf.task}/{split}.jsonl"
    filepath_text = f"data/dataset/{conf.task}/{split}.txt"
    hao.paths.make_parent_dirs(filepath_json)
    fields_to_remove = ['caption', 'editor', 'editor_timestamp', 'reviewer', 'reviewer_timestamp', 'updated_at', 'diff_reviewed', 'reviewer_timestamp_last']
    items = hao.dicts.remove_fields(items, fields_to_remove)
    with open(filepath_json, "w") as f:
        for item in tqdm(convert_to_json(items), desc=f"[saving] {os.path.basename(filepath_json): <20}"):
            f.write(f"{item}\n")
    with open(filepath_text, "w") as f:
        for item in tqdm(convert(conf, items, tokenizer), desc=f"[saving] {os.path.basename(filepath_text): <20}"):
            f.write(f"{item}\n")
    return f"saved to {filepath_json} and {filepath_text}, size: {len(items)}"


def log_summary(conf: Conf, dataset: dict, mappings: dict):
    counters_slc = defaultdict(lambda: defaultdict(int))
    counters_mlc = defaultdict(lambda: defaultdict(int))
    for split, items in dataset.items():
        for item in items:
            annotation = item.get('annotation')
            if annotation is None:
                continue
            label, labels = annotation.get('SLC'), annotation.get('MLC')
            if label:
                counters_slc[label][split] += 1
            if labels:
                for label in labels:
                    counters_mlc[label][split] += 1

    _print_counter('SLC', counters_slc, mappings.get('SLC'))
    _print_counter('MLC', counters_mlc, mappings.get('MLC'))


def _print_counter(name, counters: dict, labels: dict):
    if len(counters) == 0:
        return
    lines = [f" {name} ".center(35, '-')]
    size = max(10, max([len(label) for label in labels]) + 1)
    lines.append(f"\t{' ': <{size}} {'train': <10} {'val': <10} {'ratio': <10} (description)")
    for label, description in labels.items():
        counter = counters.get(label)
        if counter is None:
            counts = f"{'-': <10} {'-': <10}"
            ratio = '-'
        else:
            count_train, count_val = counter.get('train', 0), counter.get('val', 0)
            counts = f"{count_train: <10} {count_val: <10}"
            ratio = '0.0' if count_val == 0 else f"{count_train / count_val:0.1f}"
        lines.append(f"\t{label: <{size}} {counts} {ratio: <10} ({description})")
    LOGGER.info('\n'.join(lines))


if __name__ == '__main__':
    try:
        process()
    except KeyboardInterrupt:
        print('[ctrl-c] stopped')
    except Exception as err:
        LOGGER.exception(err)
