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
