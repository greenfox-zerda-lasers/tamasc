import datetime
from random_words import RandomWords
import os
rw = RandomWords()



class Player():
    def __init__(self, name):
        self.name = name

class hangman():

    def __init__(self, player):
        self.player = player
        self.start()

    def start(self):
        self.guess_me = list(rw.random_words()[0])
        self.current_guesses = list('_'*len(self.guess_me))
        self.incorrect_guesses = 0
        self.incorrect_guessed_charachters = []
        self.state = 'playing'
        self.game_loop()

    def game_loop(self):
        os.system('clear')
        self.hangman_graphic(self.incorrect_guesses)
        print(' '.join(self.current_guesses))
        print(' '.join(self.guess_me))
        while self.incorrect_guesses < 6 and self.state == 'playing':
            input_char = self.input_guess()
            indexes, incorrect_guess = self.check_input(input_char)
            self.incorrect_guesses += incorrect_guess
            for i in indexes:
                self.current_guesses[i] = input_char
            self.hangman_graphic(self.incorrect_guesses)
            print(' '.join(self.current_guesses))
            print('Wrong guesses: ' + ' '.join(self.incorrect_guessed_charachters))
            if self.guess_me == self.current_guesses:
                self.win()
        self.lose()

    def lose(self):
        print('You lost, you have hanged!')
        self.game_state = 'lost'
        self.new_game()

    def win(self):
        print('Congratulation, you have survived!')
        self.game_state = 'won'
        self.new_game()

    def new_game(self):
        want_to_play_again = input('Would you like to play again? (yes/no)\n')
        self.state == 'finished'
        if want_to_play_again == 'yes':
            self.start()
        else:
            return

    def check_input(self, input_char):
        indexes = [i for i, char in enumerate(self.guess_me) if input_char == char]
        incorrect_guess = 0
        if len(indexes) == 0:                                                   # check if the guess is incorrect
            incorrect_guess = 1
            self.incorrect_guessed_charachters.append(input_char)
        return indexes, incorrect_guess

    def input_guess(self):
        input_char = input('\n type a charachter: ')
        if len(input_char) != 1:
            print('Please enter a letter!\n')
            return self.input_guess()
        return input_char

    def hangman_graphic(self, guesses):
        os.system('clear')
        if guesses == 0:
            print("________      ")
            print("|      |      ")
            print("|             ")
            print("|             ")
            print("|             ")
            print("|             ")
        elif guesses == 1:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|             ")
            print("|             ")
            print("|             ")
        elif guesses == 2:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /       ")
            print("|             ")
            print("|             ")
        elif guesses == 3:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|      ")
            print("|             ")
            print("|             ")
        elif guesses == 4:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|             ")
            print("|             ")
        elif guesses == 5:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|     /       ")
            print("|             ")
        else:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\  <--{}".format(self.player))
            print("|     / \     ")
            print("|             ")
            print("GAME OVER!    ")

player = ('Tomi')
game = hangman(player)
