#############################################################################
##
## CS101 Lab
## Assignment 9
## Kate Rowley
## kerdn5@mail.umkc.edu
## 
## PROBLEM: The program should ask the user for the file, use a try except so if 
## the read_in_file function throws an error you can loop and ask for a filename 
## again. It should then output the month that has the highest crime rate. The 
## offense that occurs the most, and then ask for an offense and output a formatted 
## report of the zip code and howmany times that offense occurs in that zip code. 
## It should use the dictionaries created from the functions already given.
##
## ALGORITHM:
##      1. define given functions
##      2. define function to find max month, find max offense, and print offense by zipcode table
##      3. use while loop and try block to ask user for file name
##      4. output max month and number of offenses
##      5. ouput max offense and number of offenses
##      6. use while loop and if else loop to ask the user for an offense
##      7. output offense by zip code table
##
## ERROR HANDLING:
##      1. Use of try block to filter out bad file names
##      2. Use of if else loop to filter out bad month numbers
##      3. Use of if else loop to filter out bad offense inputs
##
## OTHER COMMENTS:
##
#############################################################################

import csv

def month_by_number(number):
    months = {
        1 : 'January', 
        2 : 'Febuary', 
        3 : 'March',
        4 : 'April', 
        5 : 'May',
        6 : 'June',
        7 : 'July',
        8 : 'August',
        9 : 'September',
        10 : 'October',
        11 : 'November',
        12 : 'December'
        }
    
    if number not in months:
        print('Month must be between 1-12.')
    
    return months[number]

def read_in_file(file_name):
    with open(file_name,'rt') as file:
        file_csv = csv.reader(file)
        lst_of_lsts = []
        for lst in file_csv:
            lst_of_lsts.append(lst)
        del lst_of_lsts[0]
    return lst_of_lsts
    
def create_reported_date_dict(lst_of_lsts):
    date_count = {}
    for lst in lst_of_lsts:
        if lst[1] in date_count:
            date_count[lst[1]] += 1
        else:
            date_count[lst[1]] = 1
    return date_count

def create_reported_month_dict(lst_of_lsts):
    month_count = {}
    for lst in lst_of_lsts:
        month_1 = lst[1].split('/')
        month = month_1[0].replace('0','')
        month = int(month)
        if month in month_count:
            month_count[month] += 1
        else:
            month_count[month] = 1
    return month_count

def create_offense_dict(lst_of_lsts):
    offense_count = {}
    for lst in lst_of_lsts:
        if lst[7] in offense_count:
            offense_count[lst[7]] += 1
        else:
            offense_count[lst[7]] = 1
    return offense_count

def create_offense_by_zip(lst_of_lsts):
    offense_by_zip = {}
    for lst in lst_of_lsts:
        if lst[7] in offense_by_zip:
            zip_count = offense_by_zip[lst[7]]
            if lst[13] in zip_count:
                zip_count[lst[13]] += 1
            else:
                zip_count[lst[13]] = 1
        else:
            offense_by_zip[lst[7]] = {lst[13]:1}
    return offense_by_zip

def max_month_offense(month_count):
    months = list(month_count.keys())
    counts = list(month_count.values())
    max_count = max(counts)
    month = months[counts.index(max_count)]
    string_month = month_by_number(month)
    max_month_offense = [string_month,max_count]
    return max_month_offense

def max_offense(offense_count):
    offenses = list(offense_count.keys())
    counts = list(offense_count.values())
    max_count = max(counts)
    offense = offenses[counts.index(max_count)]
    max_offense = [offense,max_count]
    return max_offense

def create_offense_table(offense):
    offense_by_zip = create_offense_by_zip(lst_of_lsts)
    print('\n{} offenses by Zip Code'.format(offense))
    print('{:20}{:10}'.format('Zip Code', '# Offenses'))
    print('=' * 30)
    for offenses, zipcode in offense_by_zip[offense].items():
        print('{:<20}{:>10}'.format(offenses, zipcode))

         
if __name__ == "__main__":
    while True:
        try:
            file_name = input('\nEnter the name of the crime data file ==> ')
            lst_of_lsts = read_in_file(file_name)
            break
        except FileNotFoundError:
            print('Could not find file specified. {} not found'.format(file_name))
            continue

    months = create_reported_month_dict(lst_of_lsts)
    offenses = create_offense_dict(lst_of_lsts)
    max_month = max_month_offense(months)
    print('\nThe month with the highest number of crimes was {} with {} offenses'.format(max_month[0],max_month[1]))
    max_offense = max_offense(offenses)
    print('The offense with the highest number of crimes is {} with {} offenses'.format(max_offense[0],max_offense[1]))

    while True:
        offense = input('\nEnter an offense ==> ').title()
        if offense in offenses:
            break
        else:
            print('Offense not found, please try again')

    create_offense_table(offense)

    

    






