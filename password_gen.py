import string
import random

def length():
    # Getting password length
    length = int(input("Enter password length: "))

    print('''Choose character set for password from these : 
            1. Letters
            2. Digits
            3. Special characters
            4. Exit''')
    
    return length
    
def characters():
    characterList = ""

    # Getting characters for password
    while (True):
        choice = int(input("Pick a number "))
        if (choice == 1):

            # Adding letters to possible characters
            characterList += string.ascii_letters
        elif (choice == 2):

            # Adding digits to possible characters
            characterList += string.digits
        elif (choice == 3):

            # Adding special characters to possible
            characterList += string.punctuation
        elif (choice == 4):
            break
        else:
            print("Please pick a valid option!")
            
    return characterList

def generate(characterList, length):
    password = []

    for i in range(length):

        randomchar = random.choice(characterList)

        password.append(randomchar)

    print("The random password is " + "".join(password))

if __name__ == '__main__':
    length =length()
    characterList = characters()
    generate(characterList, length)