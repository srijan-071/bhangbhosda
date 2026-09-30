"""Small dependency-free task tracker used by the repository examples."""
from dataclasses import dataclass, asdict
from pathlib import Path
import json


@dataclass
class Task:
    title: str
    status: str = "todo"


def load_tasks(path: str = "tasks.json") -> list[Task]:
    file = Path(path)
    if not file.exists():
        return []
    data = json.loads(file.read_text(encoding="utf-8"))
    return [Task(**item) for item in data]


def save_tasks(tasks: list[Task], path: str = "tasks.json") -> None:
    Path(path).write_text(
        json.dumps([asdict(task) for task in tasks], indent=2) + "\n",
        encoding="utf-8",
    )


def add_task(title: str, path: str = "tasks.json") -> Task:
    title = title.strip()
    if not title:
        raise ValueError("Task title cannot be empty")
    tasks = load_tasks(path)
    task = Task(title)
    tasks.append(task)
    save_tasks(tasks, path)
    return task


def complete_task(index: int, path: str = "tasks.json") -> Task:
    tasks = load_tasks(path)
    if index < 1 or index > len(tasks):
        raise IndexError("Task index is out of range")
    tasks[index - 1].status = "done"
    save_tasks(tasks, path)
    return tasks[index - 1]
