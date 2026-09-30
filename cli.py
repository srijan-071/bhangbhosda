"""Command-line interface for the task tracker."""
import argparse

from src.task_tracker import add_task, complete_task, load_tasks


def main() -> None:
    parser = argparse.ArgumentParser(description="Tiny local task tracker")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add = subparsers.add_parser("add", help="add a task")
    add.add_argument("title")

    done = subparsers.add_parser("done", help="complete a task by number")
    done.add_argument("index", type=int)

    subparsers.add_parser("list", help="list tasks")
    args = parser.parse_args()

    if args.command == "add":
        task = add_task(args.title)
        print(f"Added: {task.title}")
    elif args.command == "done":
        task = complete_task(args.index)
        print(f"Completed: {task.title}")
    else:
        for number, task in enumerate(load_tasks(), start=1):
            print(f"{number}. [{task.status}] {task.title}")


if __name__ == "__main__":
    main()
