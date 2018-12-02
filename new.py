#This script is written using Python 2
#This allows you to use a list to add values to it, delete, and move. It also allows you to stop. 

def main():
    while True:
        clear_screen()
        action = get_action()
        follow_up(action)
        print my_list
        raw_input("Press any key to continue >>> ")


def display_menu():
    print"MENU:\n\t\t\t---[A]dd\n\t\t\t---[M]ove\n\t\t\t---[D]elete\n\t\t\t---[S]top"


def clear_screen():
    import os; os.system('cls' if os.name == 'nt' else 'clear')


def get_action():
    while True:
        display_menu()
        action = raw_input(">>>\t").lower()
        if (action in 'amds') and (len(action) == 1):
            return action
        else:
            print "not an option TRY again"


def get_location():
    while True:
        location = raw_input("Enter location: ")
        try:
            location = abs(int(location))
            if location <= len(my_list):
                return location
            else:
                print "this number is too big, you chose {} but there are only {} items on the list".format(location, len(my_list))
                continue
        except ValueError:
            print "<{}> is not a number".format(location)


def get_move():
    while True:
        move = raw_input("Where do you want to move it? ")
        try:
            move = abs(int(move))
            if move <= len(my_list):
                return move
            else:
                print "this number is too big, you chose {} but there are only {} items on the list".format(move, len(my_list))
                continue
        except ValueError:
            print "<{}> is not a number"


def follow_up(choice):
    if choice == 'a':
        item = raw_input("Enter the item: ")
        my_list.append(item)
    elif choice == 'm' and len(my_list) >= 1:
        location = get_location()
        move = get_move()
        try:

            my_list.insert(
                int(location)-1,
                my_list.pop(
                    int(move)-1
                )
            )

        except ValueError:
            print "cannot move, <{}> or <{}> choices not an integer".format(location, move)
    elif choice == 'm':
        print "this option is not available yet"
    elif choice == 'd' and len(my_list) >= 1:
        while True:
            delete = abs(int(input("which will you delete? ")))
            if delete <= len(my_list):
                break
            else:
                print "cannot delete too big number"
        del my_list[delete-1]
    elif choice == 'd':
        print "this list has no items, cannot DELETE"
    elif choice == 's':
        print "Thanks for playing"
        import sys; sys.exit()


my_list = []
main()

