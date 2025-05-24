from tazkDATA import tasks,id_cntr
from datetime import date
from tazkUTILS import get_task_id

def add_task():
    global id_cntr
    name = input('Enter the name of the task : ')
    status = input('Enter the status of the task["Started,Ongoing,Completed"] : ')
    task_desc = input('Enter a brief decription of the task (in 25-50 words) : ')
    while True:
        deadline_str = input('Enter the deadline for task completion in "dd-mm-yyyy" format : ')
        try:
            dd, mm, yyyy = map(int,deadline_str.split('-'))
            deadline = {
                "day": dd,
                "month": mm,
                "year": yyyy
            }
            break
        except ValueError:
            print('Follow the specified for adding the deadline date')
    start_date = {
        "day" : date.today().day,
        "month" : date.today().month,
        "year" : date.today().year
    }

    task = {
        "task_id" : id_cntr,
        "name" : name,
        "status" : status,
        "task_desc" : task_desc,
        "start_date" : start_date,
        "deadline" : deadline
    }

    tasks[str(id_cntr)] = task
    id_cntr+=1
    print("\nTask Added Successfully")

def update_task():
    id = get_task_id()
    if id == -1:
        print('Task does not exist')
    else:
        data = tasks[str(id)]
        print(data)
        print('Menu')
        print('\nFIELDS\n1. Name\n2. Status\n3. Task Description\n4. Deadline\n5. Exit')
        while True:
            field=int(input('Select the field to be updated : '))
            match field:
                case 1:
                    tasks[str(id)]["name"] = input("Enter the new task name : ")
                case 2:
                    tasks[str(id)]["status"] = input('Enter the current status of the task["Started,Ongoing,Completed"] : ')
                case 3:
                    tasks[str(id)]["task_desc"] = input('Enter the new decription of the task (in 25-50 words) : ')
                case 4:
                    while True:
                        deadline = input('Enter the new deadline for task completion in "dd-mm-yyyy" format : ')
                        try:
                            dd, mm, yyyy = map(int,deadline.split('-'))
                            tasks[id]["deadline"] = {
                                "day": dd,
                                "month": mm,
                                "year": yyyy
                            }
                            break
                        except ValueError:
                            print('Follow the specified for adding the deadline date')
                case 5:
                    break
                case _:
                    print("Invalid Choice!")
    print("Updated Data")

def delete_task():
    print("Search for the task to be deleted")
    id = get_task_id()
    length = len(tasks)
    if 0 < id <= length:
        tasks.pop(str(id))
        for i in range(id+1,length+1):
            tasks[i-1] = tasks.pop(str(i))
        id_cntr-=1
        print("Task deleted Successfully")
    else:
        print("Task does not exist with the name ")

