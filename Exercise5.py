__author__ = 'shalini'
largest = None
smallest = None

while True:
    number = raw_input("Enter a number: ")
    if number == "done" : break
    try:
        ival = int(number)
    except:
        ival=-1
    if ival>0:
        num = int(number)
        if largest is None:
            largest = num
        elif num > largest:
            largest = num
        if smallest is None:
            smallest = num
        elif num < smallest:
            smallest = num

    else :
        print "Invalid input"

print "Maximum", largest
print "Minimum", smallest

# printing largest and smallest numbers after getting some numeric inputs


