import random
#define a function and parameter passed
def hangman(item):
    """
    This function accepts a word from the computer
    and the user has to guess the word.
    Anytime the user guesses incorrectly,
    part of the hangman is drawn.
    The game will end if the user guess the word before the
    hangman is completely displayed. 
    """

    #initialize wrong to zero
    wrong = 0
    #define the hangman drawing as list, each item on the list is a part of the hangman
    stages = ["",
              "_______       ",
              "|             ",
              "|      |      ",
              "|      0      ",
              "|     /|\     ",
              "|     / \     ",
              "|             "
              ]
    #get the word to be guessed
    word = item[1]
    #get the hint relating to the word to be guessed
    hint = item[0]
    #save the letters of the word in a list
    rletters = list(word)
    #defines the length of the board, i.e. how many letters the user has to guess 
    board = ["_"] * len(word)
    #initialize win to False
    win = False
    #Display Welcome message
    print("Welcome to Hangman")
    print("Hint!!!", hint)
    #loop will run once the number of wrong guesses are less than the number of parts for the hangman remaining
    while wrong < len(stages) - 1:
        #prints a new line
        print("\n")
        #defines a variable used for a message to the player
        msg = "Guess a letter "
        #takes the input which is a letter from the user
        char = input(msg)
        #checks if the letter entered is in the list of the letters of the word 
        if char in rletters:
            #if true get the index of the letter entered 
            cind = rletters.index(char)
            #place the letter entered on the board at the index retrieved 
            board[cind] = char
            #replaced the letter found in the word list with another character
            rletters[cind] = '$'
        #letter entered is not found
        else:
            #increment wrong vasriable by 1
            wrong +=1
        #display current board
        print((" ".join(board)))
        #variable that stores the value of the number of wrong guesses plus 1
        e = wrong + 1
        #prints the hangman figure based on the index range of the first index i.e. 0 and ends at the value in variable e
        print("\n".join(stages[0: e]))
        #checks if there are any more empty spaces 
        if "_" not in board:
            #displays message stating user wins
            print("You win!")
            #displays the word on the board
            print(" ".join(board))
            #sets win to true
            win = True
            #stops the loop
            break
    #checks if win is False
    if not win:
        #displays full hangman 
        print("\n".join(stages[0:wrong]))
        #displays the word 
        print("You lose! It was {}.".format(word))

#call the method
#hangman("cat")
#list of words
list_of_words = [["Flower","rose"], ["Toy","ball"], ["Fruit", "apple"], ["Animal","dog"]]
#generate a random number which can be one of the index of the list
random_num = random.randrange(0,len(list_of_words)-1)
#sends the word and hint to be guessed 
hangman(list_of_words[random_num])
