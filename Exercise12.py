__author__ = 'shalini'
# ass 10.2 from tuples
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
file_handle = open(name)
hour_book = dict()

for line in file_handle:
    if not line.startswith("From "): continue
    time = ((line.rstrip()).split())[6]
    hour = (time.split(':'))[0]
    if hour not in hour_book:
        hour_book[hour] = 1
    else:
        hour_book[hour] = hour_book[hour] + 1


lst = list()
for key,value in hour_book.items():
    lst.append( (key,value) )

lst.sort()

for key,value in lst[:]:
    print key,value

# Exercise 10.2 This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.