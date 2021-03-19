from utilities import random_word, get_input, insert

class Game:
    def __init__(self):
        self.secret = Word()
        self.chances = 7 + len(self.secret.word)
        self.guessed = []
        self.output = '_' * len(self.secret.word)
        self.status = False

    def __str__(self):
        return self.secret.word

    def run(self):
        '''Run the main part of the hangman game'''
        while self.check_status():
            display = Display(self.chances, self.output, self.guessed)
            display.std_output()
            user_input = get_input(self.guessed, list(self.output))
            guess = Guess(user_input, self.guessed, self.secret.word)
            index = guess.get_indices()
            if index:
                print(f"Letter \"{guess.letter}\" is in the mystery word...")
                self.output = insert(user_input, index, self.output)
            else:
                print(f"Letter \"{guess.letter}\" is NOT in the mystery word...")
                self.guessed.append(user_input)
            self.chances -= 1
        print(self.print_status())

    def check_status(self):
        if not "_" in self.output:
            self.status = True
            return False
        if self.chances < 1:
            return False
        return True

    def print_status(self):
        if self.status:
            result = "#-------------------------------------------------#\n" + \
                self.output + " is correct, congratulations! You have won!!!"
            return result
        else:
            return "Game Over! The word is " + self.secret.word + "\nYou have run out of attempts"


class Word:
    def __init__(self):
        self.word = random_word()
        self.length = len(self.word)


class Guess:
    '''Standart Input from User'''
    def __init__(self, letter, list, word):
        self.letter = letter
        self.list = list
        self.word = word

    def add_list(self):
        '''add letter to guessed list'''
        return self.list.append(self.letter)

    def get_indices(self):
        '''Check if the letter is in the word'''
        indices = [i for i, x in enumerate(self.word) if x == self.letter]
        return indices


class Display:
    '''Display the line for user input or end game messages'''
    def __init__(self, chance, output, guessed):
        # stores the display with the words filled
        self.chance = chance
        self.output = output
        self.guessed = guessed

    def std_output(self):
        '''Std output for user after each guess'''
        print("#-------------------------------------------------#")
        print("Please guess a letter, you have", self.chance, "chance(s) left:\n")
        self.print_result()
        if self.guessed:
            print("Already guessed letters: ", end="")
            for char in self.guessed:
                print(char, end=",")
            print("")
    
    def print_result(self):
        '''Print the std output for the missing and filled word'''
        for i in self.output:
            print(i, end=' ')
        print("")