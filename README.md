# Modern Password Generator (Python)

A secure, customizable password generator with a modern GUI built using Python's Tkinter.  
Easily generate strong passwords with letters, numbers, and symbols, evaluate their strength, and save them with descriptive labels.

## Features
- Custom password length with selectable character types (letters, numbers, symbols)
- Ensures at least one character of each selected type is included
- Password strength evaluation with color-coded feedback (Weak / Moderate / Strong)
- Clipboard copy functionality
- Show/Hide password option
- Saves labeled passwords to `passwords.txt` for easy organization
- User-friendly, modern GUI interface

## Technologies
- Python 3
- Tkinter for GUI
- `secrets`, `string`, `re` for secure password generation
- `pyperclip` for clipboard support

## Installation & Usage
1. Clone the repository:
```bash
git clone https://github.com/yourusername/password-generator.git
cd password-generator
