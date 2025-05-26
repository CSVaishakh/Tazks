from tazkDATA import tasks,path_AT
from jsonUTILS import load_json
        
def get_task():
    tasks = load_json(path_AT)
    identification = input('Enter the task id or task name : ').strip()

    if(identification.isdigit()):
        task = tasks.get(identification)
        if task:
            return task
    else:
        for i in range(1,len(tasks)+1):
            task = tasks.get(str(i))
            if task["name"].lower() == identification.lower():
                return task
    return "No task present with the given name or id"
    
def get_task_id():
    tasks = load_json(path_AT)
    name = input('Enter the task name : ').strip()
    for i in range(1,len(tasks)+1):
        task = tasks.get(str(i))
        if task and task["name"].lower() == name.lower():
            return i
    return -1

def get_task_name():
    tasks = load_json(path_AT)
    id = input('Enter the task id : ').strip()
    task = tasks.get(id)
    if task:
        return task["name"]
    else:
        return -1
    
def print_tasks():
    tasks = load_json(path_AT)
    for id,info in tasks.items():
        for key,value in info.items():
            print(f"{key} : {value}")
        print()