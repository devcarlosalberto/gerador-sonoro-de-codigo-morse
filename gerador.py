from winsound import Beep
from time import sleep
from os import system

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def translate_text_to_morse_code(text):
    text = text.split(' ')
    morse_code = ''
    for word in text:
        for char in word:
            if char.upper() in MORSE_CODE_DICT:
                morse_code += MORSE_CODE_DICT[char.upper()]
            morse_code += ' '
        morse_code += ' '
    return morse_code.strip()


def execute_sound_code_morse(morse_code, print_morse_codes=False):
    words = morse_code.split(' ')
    for word in words:
        if print_morse_codes:
            if word != '':
                print(f'Código sendo reproduzido:', word)
            else:
                print('Código sendo reproduzido: (nenhum)')
        for char in word:
            if char == '-':
                dash_sound()
            elif char == '.':
                dot_sound()
            sleep(0.2)
        sleep(0.7)


def dash_sound():
    Beep(450, 400)


def dot_sound():
    Beep(450, 200)


while True:
    system('cls')
    text = input('Escreva o texto para gerar seu respectivo código morse: ')
    morse_code = translate_text_to_morse_code(text)

    system('cls')
    print('Código morse completo:', morse_code, '\n')
    execute_sound_code_morse(morse_code, print_morse_codes=True)
    print()
    if input('Gerar novo código morse? (y/n): ').lower() != 'y':
        break
