# Basic-reg-generator

A simple Python script that generates **UK-style vehicle registration plates** (post-2001 format) based on user input such as registration year, month, and area.

This project was created as a **basic practice script** to experiment with conditional logic, input validation, and constrained random generation.

---

## Features

- Generates UK-style registration plates (2001 onwards)
- Interactive command-line input for:
  - Registration year
  - Registration month
  - Registration area (limited set)
- Randomly generates plate letters while:
  - Excluding invalid characters (`I`, `Q`, `Z`)
  - Filtering out predefined offensive letter combinations
- Automatically calculates correct year codes based on UK plate rules
- Single-file, standalone script

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

- **First letter**: Registration area (simplified mapping)
- **Second letter**: Random letter (excluding I, Q, Z)
- **Two digits**: Year code  
  - March–August → last two digits of year  
  - September–February → last two digits + 50  
- **Last three letters**: Random letters with filters applied  

All logic is contained within a single Python file and runs sequentially.

---

## Requirements

- Python 3.x  
- Standard library only (`random`, `string`)

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Basic-reg-generator.git

2. Navigate to the project folder:
   cd Basic-reg-generator
3. Run the script:
   python Registration.py


## Limitations

- Implemented as a **single-file, procedural script**
- Registration areas are limited to a small predefined list
- Plate generation logic is simplified and not fully DVLA-accurate
- No persistence, configuration files, or reusable functions
- Designed for interactive CLI use only

---

## Disclaimer

This project is for **educational purposes only** and does not generate real or officially registered vehicle registration plates.
