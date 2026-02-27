import random
from dictionary import words
import check_input

def main():
    while True:
        choice = input("Want to play hangman? (Y/N): ").upper()   #Ask the user if they wanrt to play
        if choice == "Y":
            word = random.choice(words)     #randomly choose a word from the dictionary
            incorrect = []
            correct = ["_"] * 5       #create a list of _ to represent the amount of letters in random word
            guessed_letters = []     #use to store the guessed letters
            num_incorrect = 0
            
            
            
           
            while num_incorrect < 6 and "_" in correct:    
                
                display_gallows(num_incorrect)
                print("Word: " + " ".join(correct))
                print("Incorrect letters: " + " ".join(incorrect))
                print("Letters remaining: ", end="")
                display_letters(get_letters_remaining(incorrect, correct))
                print()
                
                
                guess = input("Guess a letter: ").upper()
                
                
                if len(guess) != 1 or not guess.isalpha():
                    print("Please enter a single letter.")
                    continue
                    
                if guess in correct:
                    print("You already guessed that letter.")
                    continue
                    
                guessed_letters.append(guess)
                
                
                if guess in word:
                    print(f"Good guess! '{guess}' is in the word.")
                    
                    for i, letter in enumerate(word):
                        if letter == guess:
                            correct[i] = guess
                else:
                    print(f"Sorry, '{guess}' is not in the word.")
                    incorrect.append(guess)
                    num_incorrect += 1
            
            
            display_gallows(num_incorrect)
            print("Word: " + " ".join(correct))
            
            if "_" not in correct:
                print(f"Congratulations! You guessed the word '{word}'!")
            else:
                print(f"Game over! The word was '{word}'.")
            print()
            
        elif choice == "N":
            print("Goodbye!")
            break
        else:
            print("Please enter Y or N.")
        
        
    
    
    
def display_gallows(num_incorrect):   #print gallows based on number of incorrect guesses.
    print("========")
    print("||/   |")

    if num_incorrect == 0:
        print("||")
        print("||")
        print("||")
        print("||")
    elif num_incorrect == 1:
        print("||    O")
        print("||     ")
        print("||     ")
        print("||     ")
    elif num_incorrect == 2:
        print("||    O")
        print("||    |")
        print("||     ")
        print("||     ")
    elif num_incorrect == 3:
        print("||    O")
        print("||   \|")
        print("||     ")
        print("||     ")
    elif num_incorrect == 4:
        print("||    O")
        print("||   \|/")
        print("||     ")
        print("||     ")
    elif num_incorrect == 5:
        print("||    O")
        print("||   \|/")
        print("||   / ")
        print("||     ")
    elif num_incorrect == 6:
        print("||    O")
        print("||   \|/")
        print("||   / \\")
        print("||     ")


def display_letters(letters):    #display letters
    for letter in letters:
        print(letter, end=" ")

def get_letters_remaining(incorrect, correct):
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    remaining = []                    #empty list to store remaining letters
    for letter in letters:            #for each letters in the alphabet it check if the letter is correct                                         to the random word then it will append to remaining list
        if letter not in correct:
            remaining.append(letter)
    return remaining

if __name__ == "__main__":
    main()