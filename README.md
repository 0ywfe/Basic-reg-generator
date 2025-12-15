# Basic-reg-generator

A simple Python script that generates **UK-style vehicle registration plates** (post-2001 format) based on user input such as registration year, month, and area.

This project is intended as a **basic practice script** for input handling, validation, and random generation.

---

## Features

- Generates UK-style registration plates (2001 onwards)
- User inputs:
  - Registration year
  - Registration month
  - Registration area (limited set)
- Randomly generates plate letters while:
  - Excluding invalid characters (`I`, `Q`, `Z`)
  - Filtering out offensive letter combinations
- Automatically calculates correct year codes
- Simple command-line interface

---

## Example Output

Enter the year your car was registered (2001 and onwards): 2018
Enter the month your car was registered (E.G; September): March
Enter the area where your car was registered (E.G; London): London

Your generated registration plate is: AL18 XYZ
Thank you for using the registration plate generator!


---

## How It Works

UK registration plates follow the format:

AA## AAA

- **First letter**: Registration area
- **Second letter**: Random letter (excluding I, Q, Z)
- **Two digits**: Year code
  - March–August → last two digits of year
  - September–February → last two digits + 50
- **Last three letters**: Random letters with filters applied

---

## Requirements

- Python 3.x  
- No external libraries required

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Basic-reg-generator.git

2. Navigate to the project folder:
  cd Basic-reg-generator
3. Run the script:
  python registration.py

## Limitations

---

Area codes are limited to a small predefined list

No persistence or file output

Admin functionality is not implemented

Plate generation is simplified and not fully DVLA-accurate

## Future Improvements

---

Expand area code coverage

Refactor logic into functions

Add proper admin/customisation features

Add automated tests

Improve validation and structure

## Disclaimer

This project is for educational purposes only and does not generate real or officially registered vehicle plates.


## Speed / curiosity project, took me 2 hours (Week 3, Foundation Year)




