tasks = []

def show_tasks():
    """Display all tasks."""
    if not tasks:
        print("\n No tasks in the list.\n")
    else:
        print("\n Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "✔" if task["done"] else "❌"
            print(f"{i}. {task['title']} [{status}]")
        print()

def add_task():
    """Add a new task."""
    title = input("Enter task: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        print(" Task added!\n")
    else:
        print(" Task cannot be empty.\n")

def mark_done():
    """Mark a task as done."""
    show_tasks()
    if tasks:
        try:
            num = int(input("Enter task number to mark as done: "))
            if 1 <= num <= len(tasks):
                tasks[num - 1]["done"] = True
                print(" Task marked as done!\n")
            else:
                print(" Invalid task number.\n")
        except ValueError:
            print(" Please enter a valid number.\n")

def update_task():
    """Update an existing task."""
    show_tasks()
    if tasks:
        try:
            num = int(input("Enter task number to update: "))
            if 1 <= num <= len(tasks):
                new_title = input("Enter new task title: ").strip()
                if new_title:
                    tasks[num - 1]["title"] = new_title
                    print(" Task updated!\n")
                else:
                    print(" Task title cannot be empty.\n")
            else:
                print(" Invalid task number.\n")
        except ValueError:
            print(" Please enter a valid number.\n")

def delete_task():
    """Delete a task."""
    show_tasks()
    if tasks:
        try:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f" Task '{removed['title']}' deleted!\n")
            else:
                print(" Invalid task number.\n")
        except ValueError:
            print(" Please enter a valid number.\n")

def main():
    while True:
        print("===== To-Do List Menu =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            update_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("Have a Nice day!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
