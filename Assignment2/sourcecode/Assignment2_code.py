#CS101L
#Program 2
#Kate Rowley
#kerdn5@umsystem.edu

#print welcome message
print('**** Welcome to the LAB grade calculator! ****\n')

#get user input
name = input('Who are we calculating grades for? --> ')
lab = int(input('\nEnter the Labs grade --> '))
if lab > 100:
    lab = 100
    print('The lab value should be 100 or less. It has been changed to 100.')
elif lab < 0:
    lab = 0
    print('The lab value should be 0 or greater. It has been changed to 0.')
exam = int(input('\nEnter the Exams grade --> '))
if exam > 100:
    exam = 100
    print('The exam value should be 100 or less. It has been changed to 100.')
elif exam < 0:
    exam = 0
    print('The exam value should be 0 or greater. It has been changed to 0.')
attend = int(input('\nEnter the Attendance grade --> '))
if attend > 100:
    attend = 100
    print('The attendance value should be 100 or less. It has been changed to 100.')
elif attend < 0:
    attend = 0
    print('The attendance value should be 0 or greater. It has been changed to 0.')

#calculate and print grade
grade = (lab * .7) + (exam * .2) + (attend * .1)
print('\nThe weighted grade for',name,'is',round(grade,2))

#print letter grade
if grade >= 90 and grade <= 100:
    print(name,'has a letter grade of A')
elif grade >= 80 and grade < 90:
    print(name,'has a letter grade of B')
elif grade >= 70 and grade < 80:
    print(name,'has a letter grade of C')
elif grade >= 60 and grade < 70:
    print(name,'has a letter grade of D')
else:
    print(name,'has a letter grade of F')

#print thank you message
print('\n**** Thanks for using the Lab grade calculator ****')

