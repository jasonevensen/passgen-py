# passgen-py

A secure, simple, and fast command-line password generator written in Python.  
Supports optional clipboard copy that auto-clears after 10 seconds — great for privacy-conscious devs.

---

## Features

- ✅ Uses `secrets` module for cryptographically secure random passwords
- ✅ Optional clipboard copy with timed auto-clear (10 seconds)
- ✅ Fully interactive CLI — choose length and copy behavior
- ✅ Lightweight and works in a virtual environment

---

## Demo

```bash
$ python3 passgen.py
Enter password length (default 12): 16
Generated password: 8n@QbL2^v9r&zWxY
Copy to clipboard? (Y/n): y
Password copied to clipboard for 10 seconds...
Clipboard cleared.
```

## Requirements

Python 3.6+
pyperclip module
On Linux, xclip or xsel (install with: sudo apt install xclip if using ubuntu/debian)

## Installation

### Clone the repo
git clone https://github.com/https://github.com/jasonevensen/passgen-py
cd passgen-py

### Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

### Install required package
pip install pyperclip

## Usage

`python3 passgen.py

- Press Enter to accept the defualt password length (12) or type a number to change the length
- Type `y` or just press `Enter`
- Clipboard clears after 10 seconds

## Why This Matters

Many password generators rely on pseudo-random methods that aren’t secure.
This script uses Python's `secrets` module — designed specifically for generating cryptographically strong random numbers suitable for managing passwords, account authentication, and security tokens.

## License

MIT — use it, modify it, share it. Just don’t blame me if you forget your password. 😅

## Author

Made with 🔧 and ☕ by [Jason Evensen](https://github.com/jasonevensen)

[website](http://jasonevensen.com)

Inspired by the pursuit of clean tools, better security, and leveling up one line at a time.
