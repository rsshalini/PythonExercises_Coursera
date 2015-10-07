__author__ = 'shalini'

fname = raw_input("Enter file name: ")
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    print line.upper()

#reads a txt file and prints them with caps letters.
