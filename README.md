For change balance, change list "balance".
For change room card, change list "cards".
For change name, change list "names".

For create account, add new name
names = ["EKATIRINA POPOVA", "DANIL MILOKHIN", "VIKTOR COY", "NEW ACCOUNT"]
Add new room card
cards = ["0912 7771 1828 0000", "3717 1382 0101 1111", "1019 1019 2373 2222", "0000 0000 0000 0000"]
Add new MM/DD
mmdd = ["12/24", "10/22", "11/21", "25/12"]
Add new cvc
cvc = ["109", "053", "530", "605"]
Add new balance
balance = ["100.6$", "10$", "102$", "1$"]
And create here line:
elif name == names[3] and card == cards[3] and srokgodnosti == mmdd[3] and cvc2 == cvc[3]:
    print(f"Welcome {names[3]} to bank!")
    print(f"Your balance: {balance[3]}")