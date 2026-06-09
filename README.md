# 🔐 Password Manager

A desktop password manager built in Python using `tkinter`. Generate strong passwords, save them alongside your website and email credentials, and look them up anytime — all stored locally on your machine.

## Features

- Generate secure random passwords with a mix of letters, symbols, and numbers
- Save website, email, and password combinations to a local JSON file
- Search for saved passwords by website name
- Auto-copies generated password to clipboard for convenience
- Alerts you if any required fields are empty before saving

## How to Run

**Requirements:** Python 3.x with `pyperclip` installed.

```bash
pip install pyperclip
python main.py
```

## How to Use

1. Enter the **website**, **email**, and **password**
2. Click **Generate Password** to create a strong random password — it copies to your clipboard automatically
3. Click **Add** to save the credentials to `data.json`
4. Use the **Search** button to retrieve a saved password by website name

## Project Structure

```
password-manager/
│
├── main.py        # All UI and logic in a single script
└── data.json      # Auto-generated file where passwords are stored locally
```

## Example Entry in data.json

```json
{
    "github.com": {
        "email": "danny@example.com",
        "password": "Xk9#mP2$vL"
    }
}
```

## About

Built as part of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp**. This project covers GUI development with `tkinter`, file handling with JSON, exception handling, and random password generation.
