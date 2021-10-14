############################################################################ 
##
## CS 101 Lab
## Program 6
## Kate Rowley
## kerdn5@umsystem.edu
##
## PROBLEM : Describe the problem
##      write a utility that encodes and decodes a cipher using the Ceaser Cipher method
##
## ALGORITHM : 
##      1. get whether the user wants to encode, decode, or quit
##      2. if user chooses 1 encode text using encrypt function
##      3. if user chooses 2 decode text using decrypt function
##      4. if user choose Q quit program and output goodbye message, else return error
##      5. output encrypted or decryted message
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##########################################################################

import string 

def Encrypt(string_text, int_key):     
    '''Caesar-encrypts string using specified key.''' 
    letters = string.ascii_uppercase
    result = ''
    for i in range(len(string_text)):
        char = string_text[i]
        if char in letters:
            result += chr(ord(char) + int_key)
        else:
            result += char
    return result

def Decrypt(string_text, int_key):   
    ''' Decrypts Caesar-encrypted string with specified key. ''' 
    letters = string.ascii_uppercase
    translated = ''
    for i in string_text:
        if i in letters:
            translated += chr(ord(i) - int_key)
        else:
            translated += i
    return translated

def Get_input():   
    '''Interacts with user. Returns one of: '1', '2', '3', '4'.'''
    Print_menu()
    number = input('Enter your selection ==> ').upper()
    return number

def Print_menu():  
    '''Prints menu. No user interaction. '''
    print('MAIN MENU:')
    print('1) Encode a string')
    print('2) Decode a string')
    print('Q) Quit')

    
def main():   
    Again = True   
    while Again:     
        Choice = Get_input() 
        while Choice != '1' and Choice != '2' and Choice != 'Q':
            print('Error: must be 1, 2, or Q')
            Choice = Get_input()     
        if Choice == '1':      
            Plaintext = input("Enter (brief) text to encrypt: ").upper()       
            Key = int(input("Enter the number to shift letters by: "))      
            Ciphertext = Encrypt(Plaintext, Key)      
            print("Encrypted:", Ciphertext)     
        elif Choice == '2':       
            Ciphertext = input("Enter (brief) text to decrypt: ").upper()       
            Key = int(input("Enter the number to shift letters by: "))      
            Plaintext = Decrypt(Ciphertext, Key)      
            print("Decrypted:", Plaintext)
        else:       
            print("Have an ordinary day.")       
            Again = False


# our entire program: 
main() 