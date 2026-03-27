import os
import json
from add_task import AddTask
from view_list import ViewList
from remove_task import RemoveTask
from marklist import MarkList

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
                os.system('cls' if os.name == 'nt' else 'clear')
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
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('No Task Found')
                        print('Press Enter to return')
                        input()
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('sure you want to clear the list? (y/n)')
                        choice = input('>>').lower()
                        if choice == 'y':
                            os.remove('list.json') if os.path.exists('list.json') else None
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('List Cleared')
                            print('Press Enter to return')
                            input()
                        elif choice == 'n':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('List Not Cleared')
                            print('Press Enter to return')
                            input()
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('Invalid option')
                            print('Press Enter to return')
                            input()
                elif menu_choice == 0:
                    print('Exiting...')
                    break
                else:
                    print('Invalid option, try again.')

            except ValueError:
                print('Invalid input. please enter a number.')
                print('Press Enter to continue')
                input()

    except EOFError:
        print('')
        print('Exiting...')
    except KeyboardInterrupt:
        print('')
        print('Exiting...')

if __name__ == '__main__':
    main()