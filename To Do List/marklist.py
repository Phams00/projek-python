import os
import json

class MarkList:
    def __init__(self):
        pass

    def mark(self):
        try:
            while True:
                try:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('=======================')
                    print('Mark Task As Completed')
                    print('=======================')
                    with open('list.json', 'r') as f:
                        task = json.load(f)
                    for i, t in enumerate(task, 1):
                        status = '✓' if t['completed'] else '✗'
                        print(f'{i}. {t["task"]} [{status}] ')
                    print('=======================')
                    print('Enter Task Number To Mark (or type "0" to return):')
                    choice = int(input('>>'))
                    if choice == 0:
                        break
                    elif 1 <= choice <= len(task):
                        print('1. Mark As Completed')
                        print('2. Mark As Not Completed')
                        print('0. Return')
                        print('Enter Choice:')
                        mark_choice = int(input('>>'))
                        try:
                            if mark_choice == 0:
                                continue
                            elif mark_choice == 1:
                                with open('list.json', 'r') as f:
                                    task[choice - 1]['completed'] = True
                                with open('list.json', 'w') as f:
                                    json.dump(task, f)
                                print('Task Marked As Completed')
                                print('Press Enter To Continue')
                                input()
                            elif mark_choice == 2:
                                with open('list.json', 'r') as f:
                                    task[choice - 1]['completed'] = False
                                with open('list.json', 'w') as f:
                                    json.dump(task, f)
                                print('Task Marked As Not Completed')
                                print('Press Enter To Continue')
                                input()
                            else:
                                print('Invalid Choice, try again.')
                                print('Press Enter To Continue')
                                input()
                        except ValueError:
                            print('Invalid input. please enter a number.')
                            print('Press Enter To Continue')
                            input()
                            
                    else:
                        print('Invalid Task Number, try again.')
                        print('Press Enter To Continue')
                        input()
                except FileNotFoundError:
                    print('No tasks found')
                    print('Press Enter To Return')
                    input()
                    break
                except ValueError:
                    print('Invalid input. please enter a number.')
                    print('Press Enter To Continue')
                    input()
        except KeyboardInterrupt:
            print('')
