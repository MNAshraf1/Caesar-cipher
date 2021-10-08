logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
def encrypt(key,user_input):
    user_input = user_input.lower()
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    result = ""

    for letter in user_input:
        if letter in alphabet: #if the letter is actually in the list
            letter_cipher = (alphabet.index(letter) + key) % len(alphabet)#represents the position of the letter in alphabet
            result = result + alphabet[letter_cipher]#new decrypted letter.
        elif letter not in alphabet:
            result = result + letter#to include anything which is not a alphabet like @,1,2,)

    return result

def decrypt(key,user_input):
    user_input = user_input.lower()
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    result = ""
    for letter in user_input:
        if letter in alphabet: #if the letter is actually in the list
            #find the ciphertext letter in the alphabet
            letter_cipher = (alphabet.index(letter) - key) % len(alphabet)#represents the position of the letter in alphabet
            result = result + alphabet[letter_cipher]#new decrypted letter.
        elif letter not in alphabet:
            result = result + letter
    return result

def caesar():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == 'encode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypted = encrypt(shift,text)
        print(encrypted)
    elif direction == 'decode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypted = decrypt(shift,text)
        print(decrypted)
    else:
        print('Invalid')
        caesar()
    play_again = input("Play Again ? \n Enter yes to play again or type anything to exit \n").lower()
    if play_again == "yes":
        caesar()
