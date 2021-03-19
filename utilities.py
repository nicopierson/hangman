''' Utility functions to access words and display '''
import random

def load_words():
    '''Load words line by line from text file'''
    words = [line.rstrip() for line in open("words.txt", "r")]
    word_list = list(map(lambda x: x.upper(), words))
    return word_list
    
def random_word():
    ''' Choose a random word from the main list'''
    words = load_words()
    rand = random.randint(0,len(words))
    word = words[rand]
    return word

def get_input(list, output):
    '''Get user input and check if it is an alpha character'''
    usr_input = input('')
    alpha = True
    while alpha:
        if usr_input.isalpha() and len(usr_input) == 1:
            if not in_list(usr_input.upper(), list) and not in_list(usr_input, output):
                alpha = False
            else:
                letter = usr_input
                print(f"Letter \"{letter.upper()}\" has already been guessed.")
                usr_input = input("Please try again:\n")
        else:
            usr_input = input("Incorrect Format. Please enter a single alpha character:\n")
    return usr_input.upper()

def in_list(letter, list):
    '''Check if the letter has already been used'''
    if letter in list:
        return True
    return False

def insert(letter, index, string):
    '''Insert letter into string at specific indices'''
    temp = list(string)
    for i in index:
        temp[i] = letter
    string = "".join(temp)
    return string