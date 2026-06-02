print("Welcome to the TO-DO list:")
print("What do you want to choose:")
print("1.Add Tasks")
print("2.View Tasks")
print("3.Delete Tasks")
print("4.Exit")

tasks = []
taskNo = 0
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        
        taskNo += 1
        taskName = input("Enter the task name: ")
        taskStatus = input("Enter the task status: ")
        task ={
    "taskNo": taskNo,
    "taskName": taskName,
    "taskStatus": taskStatus
        }
        tasks.append(task)
        print("Task added successfully!")
    elif choice == 2:
        print("Your tasks are:")
        for task in tasks:
            print(task)
    elif choice == 3:
        taskNOtoDelete = input("Enter the task number to delete: ")
        for task in tasks:
            if task["taskNo"] == int(taskNOtoDelete):
                tasks.remove(task)
                print("Task deleted successfully!")
                break
        else:
            print("Task not found!")
    elif choice == 4:
        print("Exiting the program. Goodbye!")
        break