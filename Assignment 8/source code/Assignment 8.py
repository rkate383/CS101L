########################################################################
##
## CS 101 Lab
## Program 8
## Kate Rowley
## kerdn5@umsystem.edu
##
## PROBLEM : Describe the problem
##      program will allow the user to enter 2 types of grades; Tests and Programs. Each of our scores is assumed to be out of 100, 
##      so we only need the users score. The tests are 60% of a student’sgrade, while the assignments are 40%. In order to calculate 
##      the final score, we multiply the mean score of the tests by 0.6 and add it to the mean of assignments multiplied by 0.4. When
##      we display scores we will also show them the low, high, mean, and standard deviation of their tests and assignments
##
## ALGORITHM :
##      1. create functions to output option menu, add a test or assignment score, remove a test or assignment score, clear all test or
##         assignment scores, find standard deviations, and display scores.
##      2. create the test score list and the assignment score list
##      3. use function to output option menu
##      4. ask user for their choice from the option menu
##      5. use while loop to keep the program going until the user quits
##      6. use if else loop to tell the program which function to use
##
## ERROR HANDLING :
##      1. Try block to filter out value errors with the remove function
##      2. Divide by zero error, use if else block with display function
##      3. If else loop to make scores higher than 0
##      4. use the upper function to make the choice answer only upper case letters
##
## SPECIAL COMMENTS :
##      
########################################################################


import math

def print_menu():
    print('\n{:>22}'.format('Grade Menu'))
    print('1 - Add Test')
    print('2 - Remove Test')
    print('3 - Clear Tests')
    print('4 - Add Assignment')
    print('5 - Remove Assignment')
    print('6 - Clear Assignments')
    print('D - Display Scores')
    print('Q - Quit')

def add_test(lst,score):
    lst.append(score)
    return lst

def remove_test(lst,score):
    try:
        lst.remove(score)
    except ValueError:
        print('Could not find that score to remove')
    return lst

def clear_tests(lst):
    lst.clear()
    return lst

def add_assignment(lst2,score):
    lst2.append(score)
    return lst2

def remove_assignment(lst2,score):
    try:
        lst2.remove(score)
    except ValueError:
        print('Could not find that score to remove')
    return lst2

def clear_assignments(lst2):
    lst2.clear()
    return lst2

def std_test(lst,avg1):
    v = (sum([((x - avg1)**2) for x in lst]))/len(lst)
    std1 = math.sqrt(v)
    return std1

def std_assignment(lst2,avg2):
    v = (sum([((x - avg2)**2) for x in lst2]))/len(lst2)
    std2 = math.sqrt(v)
    return std2

def display(lst,lst2):
    print('Type\t\t#\tmin\tmax\tavg\tstd')
    print('=' * 52)
    if len(lst) == 0:
        print('Tests\t\t{}\tn/a\tn/a\tn/a\tn/a'.format(len(lst)))
        print('Programs\t{}\tn/a\tn/a\tn/a\tn/a'.format(len(lst2)))
        grades = round(0, 2)
        print('\nThe weighted score is {:<23}'.format(grades))
    else:
        avg1 = sum(lst)/len(lst)
        avg2 = sum(lst2)/len(lst2)
        print('Tests\t\t{}\t{:.1f}\t{:.1f}\t{:.2f}\t{:.2f}'.format(len(lst),min(lst),max(lst),avg1,std_test(lst,avg1)))
        print('Programs\t{}\t{:.1f}\t{:.1f}\t{:.2f}\t{:.2f}'.format(len(lst2),min(lst2),max(lst2),avg2,std_assignment(lst2,avg2)))
        grades = round((avg1 * 0.6) + (avg2 * 0.4), 2)
        print('\nThe weighted score is {:<23}'.format(grades))
    

lst = []
lst2 = []
print_menu()
choice = input('\n==> ').upper()
while choice != 'Q':
    if choice == '1':
        score = int(input('\nEnter the new test score 0-100 ==> '))
        if score < 0:
            print('Score must be greater than 0')
        else:
            add_test(lst,score)
    elif choice == '2':
        score = int(input('\nEnter the test score to remove ==> '))
        remove_test(lst,score)
    elif choice == '3':
        clear_tests(lst)
    elif choice == '4':
        score = int(input('\nEnter the new assignment score 0-100 ==> '))
        if score < 0:
            print('Score must be greater than 0')
        else:
            add_assignment(lst2,score)
    elif choice == '5':
        score = int(input('\nEnter the assignment score to remove ==> '))
        remove_assignment(lst2,score)
    elif choice == '6':
        clear_assignments(lst2)
    elif choice == 'D':
        display(lst,lst2)
    print_menu()
    choice = input('\n==> ').upper()
