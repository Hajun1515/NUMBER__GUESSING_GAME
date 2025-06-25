import random
import time

class Game:
    
    def play_game(self, max_rounds):
        secret_number = random.randint(1, 100)
        rounds = 0
        start_time = time.perf_counter()

        while rounds < max_rounds:
            choose_num = int(input('Choose your number: '))
            rounds += 1
            if (choose_num < secret_number):
                print('Your guessing number is too small')
            elif (choose_num > secret_number):
                    print('Your guessing number too high')
            else:
                print('CONGRATULATIONS! YOU WIN')
                end_time = time.perf_counter()
                long_time = end_time - start_time
                print('Your chance is left ==> ' + str(max_rounds - rounds))
                print('The secret number is ==> ' + str(secret_number))
                print(f'the time you spend guessing: {long_time:.2f} seconds')
                print(f'The amount you guess the number is: {rounds}')
                print('Your chance is gone!')
                return
        end_time = time.perf_counter()
        long_time = end_time - start_time
        print('Your chance is left ==> ' + str(max_rounds - rounds))
        print('The secret number is ==> ' + str(secret_number))
        print(f'the time you spend guessing: {long_time:.2f} seconds')
        print(f'The amount you guess the number is: {rounds}')
        print('Your chance is gone!')   
    def easy(self):
        self.play_game(10)
    def medium(self):
        self.play_game(5)
    def hard(self):
        self.play_game(3)
    

gamer = Game()
if __name__ == '__main__':
    Game()