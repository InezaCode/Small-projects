print("Welcome to the To-Do List App💕! Let's be productive today! ⌛⚡")
tasks=[]
task = ""

while task != "done":
    task = input("What are we doing today?: ")

    if task != "done":
        tasks.append(task)
while True: #This tells Python to repeat the menu and actions indefinitely.
    print("📝Your To-Do List:")

    for number, task in enumerate(tasks, start=1): #goes through each task and gives it a number starting from 1.
        print(f"{number}. {task}") #displays the number and task together
    print("What would you like to do?")
    print("1. Add a task ⚡")
    print("2. Mark a task as completed ✅")
    print("3. Delete a task ❌")
    print("4. Exit 👋")

    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
        new_task = input("Enter the new task: ")
        tasks.append(new_task)
        print(f"'{new_task}' added to your list. ⚡")
    elif choice == "2":
        completed_task = int(input("Which task did you complete? "))
        tasks.pop(completed_task - 1) # l'indice du task moins 1 car la liste commence à 0 (indice)
        print("Task marked as completed!✅")
    elif choice == "3":
        task_to_delete = int(input("Which task do you want to delete? "))
        tasks.pop(task_to_delete - 1)
        print("Task deleted! ❌")
    elif choice == "4":
        print("Goodbye! Stay productive! 💕")
        break