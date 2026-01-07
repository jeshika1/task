def show_menu():
    print("\n task that you want to perform")
    print("1. add task")
    print("2.view tasks")
    print("3.complete tasks")
    print("4.exit task_manager")

def add_task(tasks):
    title= input("add your task:")
    task= {
        "title" : title,
        "done": False
    }
    tasks.append(task)
    print("task added sucessfully!!")

def view_tasks(tasks):
    if not tasks:
        print("no tasks available!!")
    else:
        print("\n your tasks:")
        for index, task in enumerate(tasks,start=1):
            status="˚˖𓍢🌷✧˚.🎀⋆done" if task ["done"] else "˚.🎀༘⋆pending"
            print(f"{index}.{task}[{status}]")

def complete_tasks(tasks):
    view_tasks(tasks)
    try:
        task_number= int(input("the task number to be completed:"))
        if 1<= task_number<=len(tasks):
            tasks[task_number-1]["done"]=True
            print("task marked as completed")
        else:
            print("invalid task number")
    except ValueError:
        print("please enter a valid number")



def main():
    tasks=[]

    while True:
        show_menu()
        choice= int(input("enter you choice 1-4:"))
        if choice== 1:
            add_task(tasks)
        elif choice==2:
            view_tasks(tasks)
        elif choice==3:
            complete_tasks(tasks)
        elif choice==4:
            print("exiting task manager")
        else:
            print("\nInvalid choice!!")
           
if __name__=="__main__":
    main()
