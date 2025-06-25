from welcome_message.libs import Libs
from games.gamee import gamer
libs = Libs()
def menu():
        print('Please select the difficulty level\n1. Easy (10 chances)\n1. Medium (5 chances)\n3. Hard (3 chances)')
        choose_level = input('Enter your choose: ')   
        if choose_level == '1':
            print('GREAT! You have selected the easy difficulty level.')
            print('Lets start the game!')
            gamer.easy()
        elif choose_level == '2':
            print('NICE! You have selected the medium difficulty level.')
            print('Lets start the game!')
            gamer.medium()
        elif choose_level == '3':
            print('WOW! You have selected the hard difficulty level.')
            print('Lets start the game!')
            gamer.hard()
        else:
            print('Sorry your input is not avilable, please try again!')
def again():       
    again = input('Do you want to play again? [yes/no] ')
    if again == 'no':
        libs.stop()
    elif again == 'yes':
        menu()
def main():
    Libs.start(self='')
    menu()
    again()
if __name__ == '__main__':
    main()