from random import randint

class cab():

    guess_me = []
    state = ''
    counter = 0

    def __init__(self):
        self.guess_me = list(str(randint(1000,9999)))
        self.state = 'playing'
        print(self.guess_me)

    def stats(self):
        print('Current state:' + self.state + ' Guessed ' + str(self.counter) + ' times.')

    def guess(self, your_guess):
        for char in your_guess:
            if char not in '0123456789':
                raise TypeError("Input must be a 4 digit number")
        your_guess = list(str(your_guess))
        self.cows = 0
        self.bulls = 0
        self.temp = []
        for i, item in enumerate(your_guess):
            if item == self.guess_me[i]:
                self.bulls += 1
                self.temp.append(item)
        for item in your_guess:
            if item in self.guess_me and item not in self.temp:
                self.cows += 1
        print('Bulls: ' + str(self.bulls) + ', cows: ' + str(self.cows))
        if self.bulls == 4:
            print('You have won!')
            self.state = 'finished'
        self.counter += 1
        return self.cows, self.bulls

game = cab()
while game.state == 'playing':
    game.guess(input('Guess: '))
