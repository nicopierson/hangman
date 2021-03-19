from game import Game
''' Main class for the hangman command line game 

TO DO: 
1. add definitions to each word to learn the definitions
2. turn into a web application using flask
3. add a figure using a person
4. add hints to help user
5. add different dictionaries
6. add emojis
'''


def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()