import random
import string

reg_plate = "XX00 XXY"

letter = random.choice(string.ascii_uppercase)
while letter == "I" or letter == "Q" or letter == "Z":
    letter = random.choice(string.ascii_uppercase)

three_letters = random.choices(string.ascii_uppercase, k=3)
while "I" in three_letters or "Q" in three_letters or "Z" in three_letters:
    three_letters = random.choices(string.ascii_uppercase, k=3)

while ''.join(three_letters) in ["FUC", "SEX", "CUM", "FUK", "FCK", "DAM", "GOD", "PIS", "PRN", "PNT"]: # these are haram innit :DDDDDDD🤣
    three_letters = random.choices(string.ascii_uppercase, k=3)

three_letters = ''.join(three_letters)

while True:
    try:
        year = int(input("Enter the year your car was registered (2001 and onwards): "))
        if year >= 2001:
            break
        print("Year must be 2001 or later for this registration plate format. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid year (numbers only).")

while True:
    try:
        month = str(input("Enter the month your car was registered (E.G; September): ")).lower()
        if month in ["march", "april", "may", "june", "july", "august", "september", "october", "november", "december", "january", "february"]:
            break
        print("Month not recognized for registration plate codes. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid month (words only).")

if month in ["march", "april", "may", "june", "july", "august"]:
    year = int(str(year)[2:])
elif month in ["september", "october", "november", "december", "january", "february"]:
    year = int(str(year)[2:]) + 50

while True:
    try:
        area = str(input("Enter the area where your car was registered (E.G; London): ")).lower()
        if area in ["london", "birmingham", "manchester", "glasgow", "leeds", "cardiff",]:
            break
        print("Area not recognized for registration plate codes. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid area (United Kingdom only).")

if area == "london":
    reg_plate = reg_plate[0:1] + 'L'
elif area == "birmingham":
        reg_plate = reg_plate[0:1] + 'B' 
elif area == "manchester":
        reg_plate = reg_plate[0:1] + 'M'
elif area == "glasgow":
        reg_plate = reg_plate[0:1] + 'S'
elif area == "leeds":
    reg_plate = reg_plate[0:1] + 'Y'
elif area == "cardiff":
    reg_plate = reg_plate[0:1] + 'C'

reg_plate = reg_plate[1:2] + letter

reg_plate += reg_plate[2:3] + str(year).zfill(2)

reg_plate += " " + three_letters

print("Your generated registration plate is: " + reg_plate)
print("Thank you for using the registration plate generator!")

passcode = str(input).lower()
if passcode == "admin123":
    print("Access granted. Welcome, Admin!")

## i will add admin customization features later ##