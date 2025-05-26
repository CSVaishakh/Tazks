import typer
import tazkACTIONS as ta
import tazkUTILS as tu

def main():
    print('Menu')
    print('\n1. Add Task\n2. Update Task\n3. Delete Tasks\n4. Print Existing Tasks\n5. Search for a Task\n5. Exit')
    while True:
        field=int(input('Enter your choice : '))
        match field:
            case 1:
                ta.add_task()
            case 2:
                ta.update_task()
            case 3:
                ta.delete_task()
            case 4:
                tu.print_tasks()
            case 5:
                print(tu.get_task())
            case 6:
                break
            case _:
                print("Invalid Choice!")

main()