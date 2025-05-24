from tazkDATA import tasks

        
def get_task():
    identification = input('Enter the task id or task name : ').strip()
    if(identification.isdigit()):
        task = tasks.get(identification)
        if task:
            return task
        else:
            return -1
    else:
        for i in range(1,len(tasks)+1):
            task = tasks.get(str(i))
            if task["name"].lower() == identification.lower():
                return task
        return -1
    
def get_task_id():
    name = input('Enter the task name : ').strip()
    for i in range(1,len(tasks)+1):
        task = tasks.get(str(i))
        if task and task["name"].lower() == name.lower():
            return i
    return -1

def get_task_name():
    id = input('Enter the task id : ').strip()
    task = tasks.get(id)
    if task:
        return task["name"]
    else:
        return -1
    
def print_tasks():
    for id,info in tasks.items():
        for key,value in info.items():
            print(f"{key} : {value}")
        print()