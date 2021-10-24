########################################################################
##
## CS 101 Lab
## Program 7
## Kate Rowley
## kerdn5@umsystem.edu
##
## PROBLEM : 
##       Write a program to read through a file containing information about fuel economy and output the results to a file above a threshold that the user 
##       gives. If the user wants to see all vehicles with a combined mpg greater than 50, then your program will output that information to the file of 
##       their choosing. The information is tab-delimited.
##
## ALGORITHM : 
##      1. get minimum fuel economy
##      2. get the name of the wanted input file
##      3. get the name of the wanted output file
##      4. edit the output file with each type of car with the minimum fuel economy
##
## ERROR HANDLING:
##      Use try block to filter out errors
##      Use if loop to filter out number errors
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

def get_min_mpg():  
    while True:
        try:
            mpg = float(input('Enter the minimum mpg ==> '))
            while mpg < 0 or mpg > 100:
                if mpg < 0:
                    print('Fuel economy must be greater than 0')
                elif mpg > 100:
                    print('Fuel economy must be less than 100')
                mpg = int(input('Enter the minimum mpg ==> '))
            else:
                return mpg
        except ValueError:
            print('You must enter a number for the fuel economy')

def get_input_file():
    while True:
        try:
            file_name = input('\nEnter the name of the input vehicle file ==> ')
            with open(file_name,'r') as read_file:
                return [[data.strip() for data in line.strip().split('\t')] for line in read_file.readlines()]
        except FileNotFoundError:
            print('Could not open file {}'.format(file_name))

def write_to_file(min_mpg,file_data):
    while True:
        try:
            output_f = input('\nEnter the name of the file to output to ==> ')
            with open(output_f,'w') as write_file:
                for data in file_data:
                    try:
                        if min_mpg >= float(data[7]):
                            write_file.write('{0:<5}{1:<40}{2:<40}{3:>10}\n'.format(data[0],data[1],data[2],data[7]))
                    except ValueError:
                        print('Could not convert value invalid for vehicle',data[0],data[1],data[2])
        except IOError:
            print('There is an IO Error',output_f)

def main():
    min_mpg = get_min_mpg()
    file_data = get_input_file()[1:]
    write_to_file(min_mpg,file_data)

main()

