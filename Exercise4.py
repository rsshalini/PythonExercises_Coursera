__author__ = 'shalini'
#define a function to compute pay given hours and rate

def computepay(hours,rate):
    hours = int(hours)
    rate = int(rate)
    if hours > 40 :
        pay = 40*rate + (hours-40)*rate*1.5
        print "Your pay is ", pay
    else :
        print "Your pay is ", (hours*rate)

computepay(45,10)

# using a function for the same prog as below


def computepay(h,r):
    return (40*r)+(h-40)*1.5*r


hrs = raw_input("Enter Hours:")
rate = raw_input("Enter Rate:")
h = float(hrs)
r= float(rate)
if h>40:
    print computepay(h,r)
else:
    print h*r

