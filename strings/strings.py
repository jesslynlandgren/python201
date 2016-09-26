def up(string):
    return string.upper()


def cap(string):
    return string[0].upper() + string[1:len(string)]

def rev(string):
    return string[::-1]

def cCipher(string):
    cip = 'nopqrstuvwxyzabcdefghijklm'
    abc = 'abcdefghijklmnopqrstuvwxyz'
    stringNew = ''

    for letter in string:
        if letter == "m":
            stringNew += 'z'
        elif letter not in abc:
            stringNew += ' '
        else:
            i = cip.index(letter)
            letterNew = abc[i]
            stringNew += letterNew
    return stringNew

def leetSpk(string):
    string = string.upper()
    stringNew = ''
    leetDict = {'A':'4', 'E':'3', 'G':'6', 'I':'1', 'O': '0', 'S':'5', 'T':'7'}
    for letter in string:
        if leetDict.has_key(letter):
            leet = leetDict[letter]
            stringNew += leet
        else:
            stringNew += letter
    return stringNew


def llVowels(string):
    stringNew = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    i = 0
    while i < len(string):
        letter = string[i]
        if (i == len(string) - 1) and (letter in vowels):
            i += 1
            break
        elif (i == len(string) - 1):
            stringNew += letter
            i += 1
        else:
            if (letter == string[i+1]) and (letter in vowels):
                longVowel = 5*letter
                stringNew += longVowel
                i += 2
            else:
                stringNew += letter
                i += 1
    return stringNew

    # string = string.lower()
    # vowelDict = {'aa':'aaaaa','ee':'eeeee','ii':'iiiii','oo':'ooooo','uu':'uuuuu']
    # string.replace()
    # return string

exStr = 'dog'
print up(exStr)
print cap(exStr)
print rev(exStr)
print cCipher('lbh zhfg hayrnea jung lbh unir yrnearq')
print leetSpk('noob')
print llVowels(exStr)
print llVowels('Good')
print llVowels('Chee')
