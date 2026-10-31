tasks = []

while True:
    print("\n--- Student Task Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task name: ")
        tasks.append({"name": task, "completed": False})
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{i}. {task['name']} - {status}")

    elif choice == "3":
        try:
            number = int(input("Enter task number: "))
            if 1 <= number <= len(tasks):
                tasks[number - 1]["completed"] = True
                print("Task completed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "4":
        try:
            number = int(input("Enter task number: "))
            if 1 <= number <= len(tasks):
                tasks.pop(number - 1)
                print("Task deleted!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "5":
        print("Thank you for using Student Task Manager!")
        break

    else:
        print("Invalid choice. Try again.")