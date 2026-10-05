# Password Generator

A simple desktop password generator and saver built with Python and tkinter.

## Features

- Generates a strong random password (letters, numbers, symbols)
- Copies the generated password straight to the clipboard
- Saves website, email/username and password to a local file
- Warns on empty fields and asks for confirmation before saving

## Built with

- Python 3
- tkinter (GUI)
- pyperclip (clipboard access)

## How to run

1. Install the dependency: `pip install pyperclip`

2. Run the app: `python main.py`


## Note

Saved credentials are written to a local `data.txt` file, which is excluded
from version control via `.gitignore` and never uploaded. This is a learning
project — for real-world use, store credentials in a dedicated password manager.