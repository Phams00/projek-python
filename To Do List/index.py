import os
import json
from add_task import AddTask
from view_list import ViewList
from remove_task import RemoveTask
from marklist import MarkList
from utils import clrscr, pause

tambah = AddTask()
lihat = ViewList()
hapus = RemoveTask()
tandai = MarkList()


def ui():
    print("==================")
    print('   To Do list')
    print("==================")
    print('1. View List')
    print('2. Add Task')
    print('3. Remove Task')
    print('4. Mark Task As Completed')
    print('5. Clear List/reset list')
    print('0. Exit')
    print("==================")
    print('Pick an option: ')

def main():
    try:
        while True:
            try:
                clrscr()
                ui()
                menu_choice = int(input('>>'))
                if menu_choice == 1:
                    lihat.view()
                elif menu_choice == 2:
                    tambah.add()
                elif menu_choice == 3:
                    hapus.remove()
                elif menu_choice == 4:
                    tandai.mark()
                elif menu_choice == 5:
                    if os.path.exists('list.json') == False:
                        clrscr()
                        print('No Task Found')           
                        pause()
                    else:
                        clrscr()
                        print('sure you want to clear the list? (y/n)')
                        choice = input('>>').lower()
                        if choice == 'y':
                            os.remove('list.json')
                            clrscr()
                            print('List Cleared')
                            pause()
                        elif choice == 'n':
                            clrscr()
                            print('List Not Cleared')
                            pause()
                        else:
                            clrscr()
                            print('Invalid option')
                            pause()
                elif menu_choice == 0:
                    print('Exiting...')
                    break
                else:
                    print('invalid option')
                    pause()

            except ValueError:
                print('Invalid input. please enter a number.')
                pause()

    except EOFError:
        print('')
        print('Exiting...')
    except KeyboardInterrupt:
        print('')
        print('Exiting...')

if __name__ == '__main__':
    main()