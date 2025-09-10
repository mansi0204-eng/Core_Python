tasks = []

while True:
    print("\n1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Mark complete")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        for i in tasks:
            print(i)

    elif choice == "2":
        task = input("Enter task: ")
        tasks.append(task + " (Pending)")

    elif choice == "3":
        num = int(input("Enter task number to delete: "))
        if 0 < num <= len(tasks):
            tasks.pop(num - 1)



    elif choice == "4":
        num = int(input("Enter task number to mark complete: "))
        if 0 < num <= len(tasks):
            tasks[num - 1] = tasks[num - 1].replace("(Pending)", "(Completed)")

    elif choice == "5":
        break

    else:
        print("Invalid choice!")
