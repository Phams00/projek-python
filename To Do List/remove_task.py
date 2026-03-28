import os
import json
from utils import clrscr, load_task, save_task, pause, task_display

class RemoveTask:
    def __init__(self):
        pass

    def remove(self):
            try:
                while True:
                        clrscr()
                        print('==================')
                        print('   Remove Task')
                        print('==================')
                        task = load_task()
                        if not task:
                            print('No Task Found')
                            pause()
                            break
                        else:
                            task_display(task)
                        print('==================')
                        print('Enter Task Number to Remove (or type "0" to return):')
                        try:
                            hapus = int(input('>>'))
                            if hapus == 0:
                                break
                            elif 1<= hapus <= len(task):
                                task.pop(hapus - 1)
                                save_task(task)
                                print('Task Removed')
                                pause()
                                if not task:
                                    os.remove('list.json')
                            else:
                                print('Invalid Task Number, try again.')
                                pause()
                        except ValueError:
                            print('Invalid input. please enter a number.')
                            pause()
            except KeyboardInterrupt:
                print('')
            