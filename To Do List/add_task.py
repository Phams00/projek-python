import json
import os

class AddTask:
    def __init__(self):
        pass

    def add(self):
            try:
                while True:
                    try:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("==================")
                        print('     Add Task')
                        print("==================")
                        print('Enter New Task (or type "back" to return):')
                        task_add = input('>>')
                        if task_add.lower() == 'back':
                            break
                        elif task_add.strip() == '':
                            print('Task cannot be empty. try again.')
                            print('Press Enter to continue')
                            input()
                        elif os.path.exists('list.json') == False:
                            with open('list.json', 'w') as f:
                                json.dump([{
                                    "task": task_add,
                                    "completed": False
                                }], f)
                        else:
                            with open('list.json', 'r') as f:
                                tasks = json.load(f)
                            tasks.append({
                                "task": task_add,
                                "completed": False
                            })
                            with open('list.json', 'w') as f:
                                json.dump(tasks, f)
                    except ValueError:
                        print('Invalid input. please enter a number.')
                        print('Press Enter to continue')
                        input()
            except KeyboardInterrupt:
                print('')