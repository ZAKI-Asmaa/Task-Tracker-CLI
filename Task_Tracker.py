import json
import os
from datetime import datetime
import sys

def data_file():
    if not os.path.exists('tasks.json'):
        with open('tasks.json', 'w') as f:
            json.dump([], f)

def read_tasks():
    with open('tasks.json', 'r') as f:
        return json.load(f)

def write_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=4)

data_file()

def add_task(description):
    tasks = read_tasks()
    new_task = {
        'id': len(tasks) + 1,
        'description': description,
        'status': 'todo',
        'createdAt': datetime.now().isoformat(),
        'updatedAt': datetime.now().isoformat()
    }
    tasks.append(new_task)
    write_tasks(tasks)
    print(f"Task added: {new_task['id']} - {new_task['description']}")

def update_task(task_id, new_description=None, new_status=None):
    tasks = read_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            if new_status:
                task['status'] = new_status
            task['updatedAt'] = datetime.now().isoformat()
            write_tasks(tasks)
            print(f"Task updated: {task['id']}")
            return
    print(f"Task with ID {task_id} not found.")

def delete_task(task_id):
    tasks = read_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    write_tasks(tasks)
    print(f"Task with ID {task_id} deleted.")

def list_tasks(status=None):
    tasks = read_tasks()
    if status:
        tasks = [task for task in tasks if task['status'] == status]
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['createdAt']}, Updated At: {task['updatedAt']}")

def main():
    data_file()
    if len(sys.argv) < 2:
        print("Usage: python task_tracker.py [command] [arguments]")
        print("Commands:")
        print("  add [description]                  Add a new task")
        print("  update [id] [description] [status] Update an existing task")
        print("  delete [id]                        Delete a task")
        print("  list [status]                      List tasks (status can be 'todo', 'in-progress', 'done')")
        return

    command = sys.argv[1]

    if command == 'add':
        if len(sys.argv) < 3:
            print("Usage: python task_tracker.py add [description]")
            return
        description = ' '.join(sys.argv[2:])
        add_task(description)

    elif command == 'update':
        if len(sys.argv) < 4:
            print("Usage: python task_tracker.py update [id] [description] [status]")
            return
        task_id = int(sys.argv[2])
        new_description = sys.argv[3]
        new_status = sys.argv[4] if len(sys.argv) > 4 else None
        update_task(task_id, new_description, new_status)

    elif command == 'delete':
        if len(sys.argv) < 3:
            print("Usage: python task_tracker.py delete [id]")
            return
        task_id = int(sys.argv[2])
        delete_task(task_id)

    elif command == 'list':
        status = sys.argv[2] if len(sys.argv) > 2 else None
        list_tasks(status)

    else:
        print("Unknown command. Use 'add', 'update', 'delete', or 'list'.")

if __name__ == '__main__':
    main()
