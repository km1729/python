fin = open('file/words.txt')

line = fin.readline()
word = line.strip()
print(word)

def word_more_than_20(word):
    #9.1
    if len(word) >= 20:
        print(word)

def has_no_e(word):
    #9.2
    for letter in word:
        if letter == 'e':
            return False
    return True

def avoids(word):
    '''
    9.3 take a word and a string of forbidden letters,
    Return True if the word doesn't use any of the forbidden letters
    '''
    letters = input("forbidden lettters? ")
    for letter in letters:
        if letter in word:
            return False
    return True

def uses_only(word):
    return True

def uses_all(word):
    return True

def is_abecedarian(word):
    return True
