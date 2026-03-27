import os
import json

class ViewList:
    def __init__(self):
        pass
    
    def view(self):
        try:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("==================")
                print('     To Do List')
                print("==================")
                if os.path.exists('list.json') == False:
                    print('No Task Found')
                    print('Press Enter to return')
                    input()
                    break
                else:
                    with open('list.json', 'r') as f:
                        task = json.load(f)
                    for i, t in enumerate(task, 1):
                        status = '✓' if t['completed'] else '✗'
                        print(f'{i}. {t["task"]} [{status}] ')
                    print('==================')
                    print('Press Enter to return')
                    input()
                    break
        except KeyboardInterrupt:
            print('')