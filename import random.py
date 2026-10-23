def get_valid_letters(puzzleString):
    letters = ''
    nonLetters = ',|1234567890' # 
    for char in puzzleString:
        if not(char in letters) and not(char in nonLetters) and (char != ' '):
            letters += char
    return letters

print(get_valid_letters("RUE,EAR | RUMORS,UEII  ,UKTR ,EAR ,KEOS,KAIK,USA"))