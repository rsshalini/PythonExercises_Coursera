__author__ = 'shalini'
# assesment 9.4 from dictionaries
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
file_handle = open(name)
address_book = dict()

for line in file_handle:
    if not line.startswith("From "): continue
    email_address = ((line.rstrip()).split())[1]
    if email_address not in address_book:
        address_book[email_address] = 1
    else:
        address_book[email_address] = address_book[email_address] + 1


bigaddress_book = None
bigemail_address = None
for key, value in address_book.items():
    if bigaddress_book is None or value > bigaddress_book:
        bigemail_address = email_address
        bigaddress_book = value

print bigemail_address, bigaddress_book