__author__ = 'shalini'
text = "X-DSPAM-Confidence:    0.8475";
text1 = text[text.find(" "): ]
text2 = text1.lstrip()
print float(text2)

#getting 0.8475 to print given a string.