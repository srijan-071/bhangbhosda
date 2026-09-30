import json

import pytest

from src.task_tracker import add_task, complete_task, load_tasks


def test_add_task_persists_data(tmp_path):
    path = str(tmp_path / "tasks.json")
    task = add_task("Write documentation", path)

    assert task.title == "Write documentation"
    assert task.status == "todo"
    assert load_tasks(path) == [task]


def test_complete_task_updates_status(tmp_path):
    path = str(tmp_path / "tasks.json")
    add_task("Run tests", path)

    task = complete_task(1, path)

    assert task.status == "done"
    assert json.loads((tmp_path / "tasks.json").read_text()) == [
        {"title": "Run tests", "status": "done"}
    ]


def test_empty_title_is_rejected(tmp_path):
    with pytest.raises(ValueError):
        add_task("   ", str(tmp_path / "tasks.json"))
