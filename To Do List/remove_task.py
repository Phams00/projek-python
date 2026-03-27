import os
import json

class RemoveTask:
    def __init__(self):
        pass

    def remove(self):
            try:
                while True:
                    try:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('==================')
                        print('   Remove Task')
                        print('==================')
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
                        print('Enter Task Number to Remove (or type "0" to return):')
                        hapus = int(input('>>'))
                        if hapus == 0:
                            break
                        elif 1<= hapus <= len(task):
                            task.pop(hapus - 1)
                            with open('list.json', 'w') as f:
                                json.dump(task, f)
                                print('Task Removed')
                                print('Press Enter')
                                input()
                            if task == []:
                                os.remove('list.json')
                        else:
                            print('Invalid Task Number, try again.')
                            print('Press Enter')
                            input()
                    except ValueError:
                        print('Invalid input. please enter a number.')
                        print('Press Enter')
                        input()
            except KeyboardInterrupt:
                print('')
            