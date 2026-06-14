from time import sleep

import keyboard
import pyclip
import pyautogui
from deep_translator import GoogleTranslator

import pyperclip
def chek_qwerty(copy_text):

    return copy_text

def copy_translate_paste(chek=False):
    try:
        steam_input = pyautogui.locateOnScreen("img_5.png")
        cntr = pyautogui.center(steam_input)
        pyautogui.moveTo(cntr[0] - 30, cntr[1])

        pyautogui.click()
        sleep(0.2)
        pyautogui.hotkey("ctrl", "a")
        sleep(0.2)
        pyautogui.hotkey('ctrl', 'c')
        copy_text = pyperclip.paste()
        qwerty_to_russian = {
            # Строка 1
            'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з',
            # Строка 2
            'a': 'ф', 's': 'ы', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д',
            # Строка 3
            'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь',

            # Заглавные
            'Q': 'Й', 'W': 'Ц', 'E': 'У', 'R': 'К', 'T': 'Е', 'Y': 'Н', 'U': 'Г', 'I': 'Ш', 'O': 'Щ', 'P': 'З',
            'A': 'Ф', 'S': 'Ы', 'D': 'В', 'F': 'А', 'G': 'П', 'H': 'Р', 'J': 'О', 'K': 'Л', 'L': 'Д',
            'Z': 'Я', 'X': 'Ч', 'C': 'С', 'V': 'М', 'B': 'И', 'N': 'Т', 'M': 'Ь',

            # Символы
            '[': 'х', ']': 'ъ',
            ';': 'ж', "'": 'э',
            ',': 'б', '.': 'ю', '/': '.',
            '`': 'ё', '~': 'Ё',"&":"?",'@': '"' ,"#":"№", "$":";" ,"^":":",
        }
        if set(copy_text).intersection(set(qwerty_to_russian.keys())):
            finished_text = ""
            for char in copy_text:
                if char in qwerty_to_russian:
                    finished_text = finished_text + qwerty_to_russian[char]
                elif char not in qwerty_to_russian:
                    finished_text = finished_text + char
            copy_text = finished_text



        print(copy_text)
        transleted_text = GoogleTranslator(source='auto', target='en').translate(copy_text)
        print(transleted_text)

        pyperclip.copy(transleted_text)

        pyautogui.hotkey("ctrl", "v")
    except pyautogui.ImageNotFoundException:
        print("Image not found")

keyboard.add_hotkey("right shift", copy_translate_paste)
keyboard.add_hotkey("ctrl+right shift", copy_translate_paste(chek=True))
while True:
    pass
