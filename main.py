MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/' ,
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    "'": '.----.',
    '!': '-.-.--',
    '(': '-.--.',
    ')': '-.--.-',
    '&': '.-...',
    ':': '---...',
    ';': '-.-.-.',
    '=': '-...-',
    '+': '.-.-.',
    '-': '-....-',
    '_': '..--.-',
    '"': '.-..-.',
    '$': '...-..-',
    '@': '.--.-.',
}

def text_to_morse(text):
    text = text.upper()
    morse_chars = []
    for char in text:
        if char in MORSE_CODE:
            morse_chars.append(MORSE_CODE[char])
        # silently skip characters not in the dictionary (like punctuation)
    return ' '.join(morse_chars)

def morse_to_text(morse):
    morse_words = morse.split('/')
    text_words = []
    for morse_word in morse_words:
        morse_chars = morse_word.strip().split()
        text_chars = []
        for morse_char in morse_chars:
            for key, value in MORSE_CODE.items():
                if value == morse_char:
                    text_chars.append(key)
                    break
        text_words.append(''.join(text_chars))
    return ' '.join(text_words)


if __name__ == "__main__":

    while True:
        choice = input("Choose an option:\n1. Text to Morse\n2. Morse to Text\n3. Exit\nEnter 1, 2, or 3: ")

        if choice == "1":
            user_input = input("Enter text to convert to Morse code: ")
            print(text_to_morse(user_input))
        elif choice == "2":
            user_input = input("Enter Morse code to convert to text: ")
            print(morse_to_text(user_input))
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")