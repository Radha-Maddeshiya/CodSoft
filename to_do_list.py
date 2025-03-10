todo_list = []
def show_task():
    if not todo_list:
        print("No Task Available")
    else:
        print("\n Your To-Do List:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    todo_list.append(task)
    print(f"task'{task}' added successfully!")

def delete_task():
    show_task()
    try:
        task_no = int(input("Enter task number to delete: "))
        removed_task = todo_list.pop(task_no - 1)
        print(f"Task '{removed_task}' deleted successfully!")
    except (IndexError, ValueError):
        print("Invalid task number , please enter valid number")

while True:
    print("\n1> View Tasks\n2> Add Task\n3> Delete Task\n4> Exit")
    choice = input("Please choose an option: ")

    if choice =="1":
        show_task()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Exiting , Thank You !!")
        break
    else:
        print("Invalid choice , Please select right one")


