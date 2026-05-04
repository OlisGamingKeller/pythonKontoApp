# Konto

A small Python console application for managing bank accounts. The project is built as an object-oriented programming exercise and uses a `Konto` class together with a menu-driven main program.

## Features

- Create bank accounts
- Review account data before saving
- Manage multiple accounts in a list
- Search accounts by account number or account holder name
- Select an account when multiple matches are found
- Display account details
- Deposit money
- Withdraw money
- Prevent withdrawals when the balance is too low
- Calculate interest and add it to the account balance
- Clear the console after menu actions
- Accept numbers with either a dot or a comma

## Project Structure

```text
PythonOOP/
+-- Konto/
|   +-- konto.py   # Konto class with account logic
|   +-- main.py    # Console menu and user interaction
+-- .gitignore
+-- README.md
```

## Run

Run this command from the project folder:

```powershell
python Konto/main.py
```

## Usage

After starting the program, the main menu is shown:

```text
1) Konto anlegen
2) Konto anzeigen
3) Beenden
```

After searching for an account, a submenu for the selected account is opened:

```text
1) Kontodaten anzeigen
2) Geld einzahlen
3) Geld auszahlen
4) Zinsen berechnen
5) Zurueck
```

## Notes

- In Python, `input()` always returns text. The program converts numeric input with `int()` or `float()`.
- For amounts and interest rates, commas are automatically converted to dots.
- Accounts are only stored during the current program run. They are not persisted after the program exits.
- Console clearing currently uses the Windows command `cls`.

## Learning Goals

- Use classes and objects
- Call methods on objects
- Manage lists containing objects
- Use `for` loops for searching
- Handle invalid input with `try`/`except`
- Improve program structure with helper functions
