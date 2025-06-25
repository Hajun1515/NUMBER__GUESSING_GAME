from time import sleep
class Libs:
    def start(self):
        print('Welcome to the Number Guessing Game!')  
        print('i am thinking of a number between 1 and 100')
    def stop(self):
        print('Thank you for playing this game')
        print('The program will be stopped')
        sleep(1)
        print('...3')
        sleep(1)
        print('...2')
        sleep(1)
        print('...1')
        sleep(1)
        print('The program stopped')
        return
libs = Libs()

if __name__ == '__main__':
    Libs.start()
    Libs.stop()