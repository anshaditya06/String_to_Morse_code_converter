# Text to Morse Code Converter

A simple Python project that converts text to Morse code and Morse code back to text.

## Features

- Convert plain text into Morse code
- Convert Morse code back into readable text
- Supports uppercase and lowercase input
- Handles spaces between words using `/`
- Includes a basic test suite

## Project Files

- `main.py` - Contains the Morse code mapping and conversion functions
- `test.py` - Contains unit tests for the converter

## How It Works

The program uses a dictionary of characters mapped to their Morse code equivalents. It provides two main functions:

- `text_to_morse(text)` converts text to Morse code
- `morse_to_text(morse)` converts Morse code back to text

## Example

### Text to Morse

Input:

```text
SOS
```

Output:

```text
... --- ...
```

### Morse to Text

Input:

```text
.... .. / - .... . .-. .
```

Output:

```text
HI THERE
```

## How to Run

Run the script with Python:

```bash
python main.py
```

You will be prompted to choose one of the following options:

1. Convert text to Morse code
2. Convert Morse code to text
3. Exit the program

## Running Tests

Run the tests with:

```bash
python -m unittest -v
```

## Notes

- Unsupported characters are ignored during conversion.
- The program currently supports standard English letters, digits, and common punctuation.
