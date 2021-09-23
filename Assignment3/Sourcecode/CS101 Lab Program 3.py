#CS101 Lab
#Program 3
#Kate Rowley
#kerdn5@umsystem.edu

#welcome message
print('Welcome to the Flarsheim Guesser!\n')

#think of number
print('Please think of a number 1 through 100\n')

#get remainders
rem1 = int(input('What is the remainder when your number is divided by 3? '))
while rem1 >= 3 or rem1 < 0:
    if rem1 >= 3:
        print('The value entered must be less than 3')
    elif rem1 < 0:
        print('The value entered must be 0 or greater')
    rem1 = int(input('What is the remainder when your number is divided by 3? '))
else:
    rem2 = int(input('\nWhat is the remainder when your number is divided by 5? '))
while rem2 >= 5 or rem2 < 0:
    if rem2 >= 5:
        print('The value entered must be less than 5')
    elif rem2 < 0:
        print('The value entered must be 0 or greater')
    rem2 = int(input('What is the remainder when your number is divided by 5? '))
else:
    rem3 = int(input('\nWhat is the remainder when your number is divided by 7? '))
while rem3 >= 7 or rem3 < 0:
    if rem2 >= 7:
        print('The value entered must be less than 7')
    elif rem2 < 0:
        print('The value entered must be 0 or greater')
    rem3 = int(input('What is the remainder when your number is divided by 7? '))

#calulate number
for i in range (1,111):
    if i % 3 == rem1 and i % 5 == rem2 and i % 7 == rem3:
        print('Your number was',i)
        print('How amazing is that?\n')

#get user continue choice
user_input = input('Do you want to play again? Y to continue, N to quit ==> ')
while user_input != 'y' and user_input != 'Y' and user_input != 'n' and user_input != 'N':
    user_input = input('Do you want to play again? Y to continue, N to quit ==> ')

while user_input == 'y' or user_input == 'Y':
    print('\nPlease think of a number 1 through 100\n')
    rem1 = int(input('What is the remainder when your number is divided by 3? '))
    while rem1 >= 3 or rem1 < 0:
        if rem1 >= 3:
            print('The value entered must be less than 3')
        elif rem1 < 0:
            print('The value entered must be 0 or greater')
        rem1 = int(input('What is the remainder when your number is divided by 3? '))
    else:
        rem2 = int(input('\nWhat is the remainder when your number is divided by 5? '))
    while rem2 >= 5 or rem2 < 0:
        if rem2 >= 5:
            print('The value entered must be less than 5')
        elif rem2 < 0:
            print('The value entered must be 0 or greater')
        rem2 = int(input('What is the remainder when your number is divided by 5? '))
    else:
        rem3 = int(input('\nWhat is the remainder when your number is divided by 7? '))
    while rem3 >= 7 or rem3 < 0:
        if rem2 >= 7:
            print('The value entered must be less than 7')
        elif rem2 < 0:
            print('The value entered must be 0 or greater')
        rem3 = int(input('What is the remainder when your number is divided by 7? '))
    for i in range (1,101):
        if i % 3 == rem1 and i % 5 == rem2 and i % 7 == rem3:
            print('Your number was',i)
            print('How amazing is that?\n')
    user_input = input('Do you want to play again? Y to continue, N to quit ==> ')
    while user_input != 'y' and user_input != 'Y' and user_input != 'n' and user_input != 'N':
        user_input = input('Do you want to play again? Y to continue, N to quit ==> ')
    