todo = []

def todo_menu():
    print('Press 1 to add task: ')
    print('Press 2 to delete task')
    print('Press 3 to view all tasks')
    print('Press q to quit')

def add_task():
    task_name = input('Enter task name: ')
    task_priority = input('Enter priority of task (high, medium, low): ')


    task = {'title' : task_name,
            'priority' : task_priority}

    todo.append(task)

def view_tasks():
    for (task) in todo:
        print(f"{todo.index(task)+1} : {task['title']} : {task['priority']}")

def delete_task():
    view_tasks()

    delete_index = input('Enter index of task you want to delete: ')
    del todo[int(delete_index)-1]

user_input = ''

while user_input != 'q':
    todo_menu()
    user_input = input('Select menu option (1, 2, 3, 4, q): ')

    if user_input == '1':
        add_task()
    elif user_input == '2':
        delete_task()
    elif user_input == '3':
        view_tasks()
