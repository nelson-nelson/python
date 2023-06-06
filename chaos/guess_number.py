import random


class GuessNumber:
    def __init__(self):
        self.answer = random.randrange(100)
        self.max_trial = 10
        print(f'Please guess an integer number between 0 and 100')
        print(f'Max number of guesses: {self.max_trial}')

    def play(self):
        for i in range(self.max_trial):
            guess = int(input(f'You have {self.max_trial - i} remaining guesses.  Make a guess: '))
            if guess == self.answer:
                print(f'Good job! You have guessed the number correctly')
                break
            hint = 'warmer' if guess < self.answer else 'colder'
            print(f'Incorrect! HINT: {hint}')
        else:
            print(f'Thanks for playing.  The answer is {self.answer}.  Better luck next time!')


if __name__ == '__main__':
    play = GuessNumber()
    play.play()
