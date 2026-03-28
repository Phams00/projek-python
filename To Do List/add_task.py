import json
import os
from utils import clrscr, load_task, save_task, pause

class AddTask:
    def __init__(self):
        pass

    def add(self):
            try:
                while True:
                    try:
                        clrscr()
                        print("==================")
                        print('     Add Task')
                        print("==================")
                        print('Enter New Task (or type "back" to return):')
                        task_add = input('>>').strip()
                        
                        if task_add.lower() == 'back':
                            break
                        elif not task_add:
                            print('Task cannot be empty. try again.')
                            pause()
                            continue
                        
                        task = load_task()
                        task.append({
                            'task': task_add,
                            'completed': False
                            })
                        save_task(task)
                        print('Task Added')
                        pause()
                        
                    except ValueError:
                        print('Invalid input. please enter a number.')
                        pause()
            except KeyboardInterrupt:
                pass