# task1_todo.py
todo_list = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter a new task: ")
        todo_list.append(task)
        print("Task added!")
    elif choice == '2':
        if not todo_list:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(todo_list, 1):
                print(f"{i}. {t}")
    elif choice == '3':
        task_no = int(input("Enter task number to remove: "))
        if 0 < task_no <= len(todo_list):
            todo_list.pop(task_no - 1)
            print("Task removed!")
        else:
            print("Invalid task number.")
    elif choice == '4':
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
