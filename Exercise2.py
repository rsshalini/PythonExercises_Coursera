__author__ = 'shalini'
hours = raw_input("Enter number of hours: ")
try:
    ival = int(hours)
except:
    ival = -1

if ival >0:
    rate = raw_input("Enter hourly rate: ")
    try:
        ival = int(rate)
    except:
        ival=-1
    if ival>0:
        hours = int(hours)
        rate = int(rate)
        if hours > 40 :
            pay = 40*rate + (hours-40)*rate*1.5
            print "Your pay is ", pay
        else :
            print "Your pay is ", (hours*rate)
    else:
        print 'Please enter numeric input'
else:
    print 'Please enter numeric input'
    
#print pay given hours and hourly rate. if worked > 40 hrs, hourly rate is 1.5 times more for each hour.
# use try and except to identify incorrect numeric inputs
