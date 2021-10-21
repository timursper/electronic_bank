cards = ["0912 7771 1828 0000", "3717 1382 0101 1111", "1019 1019 2373 2222"]
mmdd = ["12/24", "10/22", "11/21"]
names = ["EKATIRINA POPOVA", "DANIL MILOKHIN", "VIKTOR COY"]
cvc = ["109", "053", "530"]
balance = ["100.6$", "10$", "102$"]

name = input("Your name from card: ")
card = input("Your room from the card: ")
srokgodnosti = input("Your MM/DD from card: ")
cvc2 = input("Your cvc from back card: ")

if name == names[0] and card == cards[0] and srokgodnosti == mmdd[0] and cvc2 == cvc[0]:
    print(f"Welcome {names[0]} to bank!")
    print(f"Your balance: {balance[0]}")
elif name == names[1] and card == cards[1] and srokgodnosti == mmdd[1] and cvc2 == cvc[1]:
    print(f"Welcome {names[1]} to bank")
    print(f"Your balance: {balance[1]}")
elif name == names[2] and card == cards[2] and srokgodnosti == mmdd[2] and cvc2 == cvc[2]:
    print(f"Welcome {names[2]} to bank!")
    print(f"Your balance: {balance[2]}")