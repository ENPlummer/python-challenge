#Importing text file.

file = '/Users/ebony/dev/Python/python-challenge/PyParagraph/Friends_Romans_Countrymen_Speech.txt'

#Open and read the file

#Counters

#Lines
num_lines = 0

#Words
num_words = 0

#Characters
num_chars = 0

with open(file,'r') as text:
    for line in file:
        words = line.split()

        num_lines += 1
        num_words += len(words)
        num_chars += len(line)
    print(num_lines)
    print(num_words)
    print(num_chars)
