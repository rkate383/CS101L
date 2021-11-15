#############################################################################
##
## CS101 Lab
## Assignment 10
## Kate Rowley
## kerdn5@mail.umkc.edu
## 
## PROBLEM: The program will ask the user for a text file to read. You’ll want to read 
## all the words and output a count of the words that are used the most. ( We’ll only 
## be concerned with words that have a length greater than 3 )
##
## ALGORITHM:
##      1. use while loop to circle back to try block when needed
##      2. use try block to open and read the file and raise exception when user 
##         enters wrong file name
##      3. use a for loop to create one list for all words
##      4. use another for loop to create list of words with length greater than 3
##      5. filter out the punctuation in the word list
##      6. use for loop to create dictionary for counting words
##      7. output word frequency table
##      8. output the number unique words and the number words that only occur once
##
## ERROR HANDLING:
##      1. Use of try block to filter out bad file names
##
## OTHER COMMENTS:
##
#############################################################################


import string

while True:
    try:
        file_name = input('\nEnter the name of the file to open ==> ')
        with open(file_name, 'r') as o_file:
            lines = o_file.readlines()
            words = [] 
            letters = []
            for word in lines:
                words.append(word.lower().split())
            for word in words:
                for letter in word:
                    if len(letter) > 3:
                        letters.append(letter)   
            letters = [''.join(c for c in s if c not in string.punctuation) for s in letters]
            letters = [s for s in letters if s]
            
        break
    except FileNotFoundError:
        print('Could not open file {}'.format(file_name))
        print('Please try again')
word_count = {}
for word in letters:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
word_count = {word: count for word, count in sorted(word_count.items(), key = lambda item: item[1], reverse = True)}
print('\nMost frequently used words')
print(' {:<12}{:<18}{}'.format('#','Word','Freq.'))
print('='*36)
n = 1
for word in word_count:
    print(' {:<12}{:<21}{}'.format(n,word,word_count[word]))
    n += 1
once = 0
for word in word_count:
    if word_count[word] == 1:
        once += 1
print('\nThere are {} words that occur only once'.format(once))
print('There are {} unique words in the document\n'.format(n-1))

