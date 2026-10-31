from datetime import date

tasks = []


# Feature 1: Add tasks with deadlines
# Feature 2: Assign priorities
def add_task():
    name = input("Enter task name: ").strip()

    if not name:
        print("Task name cannot be empty.")
        return

    while True:
        deadline_text = input("Enter deadline (YYYY-MM-DD): ")

        try:
            deadline = date.fromisoformat(deadline_text)
            break
        except ValueError:
            print("Invalid date. Example: 2026-11-05")

    while True:
        priority = input("Enter priority (High/Medium/Low): ")
        priority = priority.strip().capitalize()

        if priority in ["High", "Medium", "Low"]:
            break

        print("Please enter High, Medium, or Low.")

    task = {
        "name": name,
        "deadline": deadline,
        "priority": priority,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")


# Feature 3: Identify overdue tasks
def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    today = date.today()

    print("\n===== Your Tasks =====")

    for number, task in enumerate(tasks, start=1):

        if task["completed"]:
            status = "COMPLETED"
        elif task["deadline"] < today:
            status = "OVERDUE"
        else:
            status = "PENDING"

        print(f"\nTask {number}: {task['name']}")
        print(f"Deadline: {task['deadline']}")
        print(f"Priority: {task['priority']}")
        print(f"Status: {status}")

        if status == "OVERDUE":
            print("WARNING: This task is overdue!")


def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to complete: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            print("Task completed successfully!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"Deleted task: {removed['name']}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


while True:
    print("\n===== Student Task Manager =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("Thank you for using Student Task Manager!")
        break

    else:
        print("Invalid choice. Please select 1-5.")  
