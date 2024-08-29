def display_menu():
    print("To-Do List Menu:")
    print('''Please select one option from the following:- 
          1. Add a new task
          2. View all tasks
          3. Exit''')

def add_task(tasks):
    task = input("Enter the new task: ")
    tasks.append(task)
    print("Task added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks Added.")
    else:
        print("Your To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            print("Exiting the application. Have a good day!!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 3.")

if __name__ == "__main__":
    main()
