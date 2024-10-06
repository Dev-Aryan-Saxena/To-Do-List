def create_tl():
    task_list = []
    return task_list
def add_t(task_list,task):
    task_list.append(task)
def remove_t(task_list,task):
    task_list.remove(task)
def mark_t(task_list,task):
    index = task_list.index(task)
    task_list[index] = f"✅ {task}"
def print_task_l(task_list):
    for task in task_list:
        print(task) 
def main():
    task_list = create_tl()

    while True:
        print("\n","Choose an option:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Mark a task as done")
        print("4. Print task list")
        print("5. Quit")

        choice = int(input(" Enter the number of what to be done: "))

        if choice == 1:
            task = input("Enter the task: ")
            add_t(task_list, task)
            print_task_l(task_list)
        elif choice == 2:
            task = input("Enter the task to be removed: ")
            remove_t(task_list,task)
            print_task_l(task_list)
        elif choice == 3:
            task = input("Enter the task to be marked as done: ")
            mark_t(task_list, task)
            print_task_l(task_list)
        elif choice == 4:
            print_task_l(task_list)
        elif choice == 5:
            break
        else: 
            print("Invalid Choice")

main()
     