__author__ = 'shalini'
s = raw_input("Enter a score between 0.0 and 1.0 : ")
score=float(s)
if score <0.0:
    print "Score is out of range"
elif score >1.0:
    print "Score is out of range"
elif score >=0.9:
    print "Grade A"
elif score >=0.8:
    print "Grade B"
elif score >=0.7:
    print "Grade C"
elif score >=0.6:
    print "Grade D"
else:
    print "Grade F"


# using if else statement to print grades given the scores.


