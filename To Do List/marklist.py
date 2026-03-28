import os
import json
from utils import clrscr, load_task, save_task, pause, task_display, task_status

class MarkList:
    def __init__(self):
        pass

    def mark(self):
        try:
            while True:
                try:
                    clrscr()
                    print('=======================')
                    print('Mark Task As Completed')
                    print('=======================')
                    task = load_task()
                    if not task:
                        print('no task found')
                        pause()
                        break

                    task_display(task)
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
                                selected_task = task[choice - 1]
                                selected_task['completed'] = True
                                save_task(task)
                                print('Task Marked As Completed')
                                pause()
                            elif mark_choice == 2:
                                selected_task = task[choice - 1]
                                selected_task['completed'] = False
                                save_task(task)
                                print('Task Marked As Not Completed')
                                pause()
                            else:
                                print('Invalid Choice, try again.')
                                pause()
                        except ValueError:
                            print('Invalid input. please enter a number.')
                            pause()
                            
                    else:
                        print('Invalid Task Number, try again.')
                        pause()
                except FileNotFoundError:
                    print('No tasks found')
                    pause()
                    break
                except ValueError:
                    print('Invalid input. please enter a number.')
                    pause()
        except KeyboardInterrupt:
            print('')
