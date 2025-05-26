from tazkDATA import tasks,path_AT
from datetime import date
from tazkUTILS import get_task_id
from jsonUTILS import load_json,save_json

import os

def add_task():
    tasks = load_json(path_AT)
    id_cntr = len(tasks)+1

    name = input('Enter the name of the task : ').title()
    status = input('Enter the status of the task["Started,Ongoing,Completed"] : ').title()
    task_desc = input('Enter a brief decription of the task (in 25-50 words) : ').capitalize()
    
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
    save_json(tasks,path_AT)
    print("\nTask Added Successfully")

def update_task():
    tasks = load_json(path_AT)
    id = get_task_id()
    if id == -1:
        print('Task does not exist')
    else:
        data = tasks[str(id)]
        print(data)
        print('Menu')
        print('\nFIELDS\n1. Name\n2. Status\n3. Task Description\n4. Deadline\n5. Exit')
        while True:
            try:
                field=int(input('Select the field to be updated : '))
            except ValueError:
                print("Please enter a number from the options")
            match field:
                case 1:
                    tasks[str(id)]["name"] = input("Enter the new task name : ").title()
                case 2:
                    tasks[str(id)]["status"] = input('Enter the current status of the task["Started,Ongoing,Completed"] : ').title()
                case 3:
                    tasks[str(id)]["task_desc"] = input('Enter the new decription of the task (in 25-50 words) : ').capitalize()
                case 4:
                    while True:
                        deadline = input('Enter the new deadline for task completion in "dd-mm-yyyy" format : ')
                        try:
                            dd, mm, yyyy = map(int,deadline.split('-'))
                            tasks[str(id)]["deadline"] = {
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
    print(tasks)
    save_json(tasks,path_AT)
    print("Updated Data")

def delete_task():
    tasks = load_json(path_AT)
    if not tasks:
        print("No tasks found")
        return
    
    print("Search for the task to be deleted")
    id = get_task_id()

    id_str = str(id)
    if id_str not in tasks:
        print(f"Task with {id} does not exist")
        return
    tasks.pop(id_str)
    
    tasks_new = {}
    id_new = 1

    for old_id in sorted(tasks.keys(),key=int):
        tasks_new[str(id_new)] = tasks[old_id]
        tasks_new[str(id_new)]["task_id"] = id_new
        id_new += 1
    
    save_json(tasks_new, path_AT)
    print("Task deleted successfully.")

