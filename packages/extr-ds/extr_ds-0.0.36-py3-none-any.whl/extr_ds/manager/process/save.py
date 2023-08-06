import os

from .workspace import WORKSPACE
from ..utils.filesystem import load_data, \
                               append_data


def save_entities() -> None:
    dataset = set(load_data(os.path.join(WORKSPACE, '2', 'dev.txt')))
    append_data(os.path.join(WORKSPACE, '4', 'ents.txt'), dataset)

    redacted_dataset = set(load_data(os.path.join(WORKSPACE, '3', 'dev-ents-redacted.txt')))
    append_data(os.path.join(WORKSPACE, '4', 'ents-redacted.txt'), redacted_dataset)

def save_relations() -> None:
    dataset = set(load_data(os.path.join(WORKSPACE, '2', 'dev.txt')))
    append_data(os.path.join(WORKSPACE, '4', 'rels.txt'), dataset)

def save_all() -> None:
    save_entities()
    save_relations()
