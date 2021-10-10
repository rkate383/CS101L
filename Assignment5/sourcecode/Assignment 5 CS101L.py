########################################################################
##
## CS 101 Lab
## Program 5
## Kate Rowley
## kerdn5@umsystem.edu
##
## PROBLEM : The Linda Hall library wants to come up with a new library card numbering 
## system for students. The card number’s first 5characters areA-Z, which will normally 
## be the first five characters of the student’sname. The next character at index 5 is a 
## string value either 1, 2, or 3 which represents the different schools; SCE, 
## School of Law, or College of arts and Sciences. The character at index 6is either
## 1, 2, 3, or 4. These are the grade levels; Freshman, Sophomore, Junior, and Senior.
## The next 2 characters are 0-9, and the last character at index 9 is the check digit 
## to verify the previous values. The last character is also 0-9.
##
## ALGORITHM : 
##      1. Define functions
##      2. Get card number
##      3. Check if valid
## 
## ERROR HANDLING:
##      Check for incorrect inputs for certain indexes in the card number
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

import string

def character_value(char : str) -> int:
    ''' Returns 0 for A, 1 for B, etc. '''
    value = string.ascii_uppercase.index(char)
    return value
    
def get_check_digit(value, idnumber : str) -> int:
    ''' Returns the check digit for the name and sid. '''
    index = 0
    for i in idnumber:
        digit = (index + 1) * value
        index += 1
    check_digit = digit % 10
    return check_digit

def is_valid(idnumber : str) -> tuple:
    ''' returns 2 values bool and a string with errors if bool is False '''
    if len(idnumber) != 10:
        return False, 'The length of the number given must be 10'
    elif idnumber[:4].isalpha() == False:
        return False, 'The first 5 characters must be A-Z'
    elif idnumber[7:].isdigit() == False:
        return False, 'The last 3 character must 0-9'
    elif 0 > idnumber[5] > 3:
        return False, 'The sixth character must be 1, 2, or 3'
    elif 0 > idnumber[6] > 4:
        return False, 'The seventh character must be 1, 2, 3, or 4'
    else:
        return True, ''

def verify_check_digit(check_digit, idnumber : str) -> tuple:    
    ''' returns True if the check digit is valid, False if not '''
    if check_digit == idnumber[9]:
        return True, ''
    else:
        return False, 'Check digit',idnumber[9],'does not match calculated value', check_digit
    
def get_school(idnumber : str) -> str:    
    ''' Returns the school the 5th index or 6th character is for. '''
    if 0 < idnumber[5] > 4:
        if idnumber[5] == 1:
            return 'School of Computing and Engineering SCE'
        elif idnumber[5] == 2:
            return 'School of Law'
        else:
            return 'College of Arts and Sciences'
    else:
        return 'Invalid school'
  
def get_grade(idnumber : str) -> str:   
    '''Returns the grade for index 6'''
    if 0 < idnumber[6] > 5:
        if idnumber[6] == 1:
            return 'Freshman'
        elif idnumber[6] == 2:
            return 'Sophomore'
        elif idnumber[6] == 3:
            return 'Junior'
        else:
            return 'Senior'
    else:
        return 'Invalid Grade'
    
if __name__ == "__main__":    
    print("{:^60}".format("Linda Hall"))
    print("{:^60}".format("Library Card Check"))    
    print("="*60)    
    
    while True:        
        print()        
        card_num = input("Enter Libary Card.  Hit Enter to Exit ==> ").upper().strip()        
        if card_num == "":
            break
        result, error = verify_check_digit(card_num)        
        if result == True:            
            print("Library card is valid.")            
            print("The card belongs to a student in {}".format(get_school(card_num)))            
            print("The card belongs to a {}".format(get_grade(card_num)))        
        else:            
            print("Libary card is invalid.")            
            print(error)