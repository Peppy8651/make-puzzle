# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Team Names:   Dante Fuentes
#               Sangharsha Dhakal
#               Marlon Galindo
#               Conner Katzenberger
# Section:      578
# Assignment:   Lab 9 Team
# Date:         10/23/26

def print_puzzle(puzzle):
    """ Print puzzle as a long division problem. """
    puzzle = puzzle.split(",")
    for i in range(len(puzzle)):
        if i == 1:
            print(f"{len(puzzle[i].split('|')[1]) * '_': >16}")
        print(f"{puzzle[i]: >16}")
        if i > 1 and i % 2 == 0:
            print(f"{'-'*len(puzzle[i]): >16}")
# function 1

def get_valid_letters(puzzleString): # returns one string of 10 unique letters from puzzle string
    '''Returns one string of 10 unique letters from the puzzle string.'''
    letters = '' # set up empty list of letters
    nonLetters = ',|1234567890' # characters that can't be included
    for char in puzzleString: # check each character in the puzzlestring and find a unique letter
        if not(char in letters) and not(char in nonLetters) and (char != ' '):
            letters += char # add this unique letter to the string list
    return letters

# function 3
def check_user_guess(dividend, quotient, divisor, remainder):
    '''Only returns true if the dividend is equal to the quotient * divisor + remainder.'''
    guessTrue = (dividend == quotient * divisor + remainder)
    return guessTrue

# function 6

def main():
    puzzleInput = input("Enter a word arithmetic puzzle: ")
    print_puzzle()
    uniqueLetters = get_valid_letters(puzzleInput)
    guessInput = input("Enter your guess, for example ABCDEFGHIJ: ")
    validGuess = is_valid_guess(uniqueLetters, guessInput)
    if (validGuess):
        dividend, quotient, divisor, remainder = make_numbers(puzzleInput, guessInput)
        doubleCheck = check_user_guess(dividend, quotient, divisor, remainder)
        if (doubleCheck):
            print("Good job!")
        else:
            print("Try again!")
    else:
        print("Your guess should contain exactly 10 unique letters used in the puzzle.")

if __name__ == "__main__":
    main()

