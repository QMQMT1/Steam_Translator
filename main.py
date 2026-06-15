import keyboard
import pyclip
import pyautogui
from pyautogui import sleep
from deep_translator import GoogleTranslator

import pyperclip
# hello
def eng_to_russian_or_vice_versa():
    def chek(copy_text,dict_trans):
        global copy
        finished_text = ""
        for char in copy_text:
            if char in dict_trans:
                finished_text = finished_text + dict_trans[char]
            elif char not in dict_trans:
                finished_text = finished_text + char
        print(finished_text)
        return finished_text


    try:
        sleep(0.2)
        pyautogui.hotkey('ctrl', 'c')
        sleep(0.2)
        copy = pyperclip.paste()
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
            '`': 'ё', '~': 'Ё',
        }
        qwerty_from_russian = {v:k for k, v in qwerty_to_russian.items()}

        if set(copy).intersection(set(qwerty_from_russian.keys())):
            copy =chek(copy, qwerty_from_russian)
        elif set(copy).intersection(set(qwerty_to_russian.keys())):
            copy = chek(copy,qwerty_to_russian)


        pyperclip.copy(copy)
        sleep(0.5)
        pyautogui.hotkey("ctrl", "v")

    except Exception as e:
        print(e)


def copy_translate_paste():
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



        print(copy_text)
        transleted_text = GoogleTranslator(source='auto', target='en').translate(copy_text)
        print(transleted_text)

        pyperclip.copy(transleted_text)

        pyautogui.hotkey("ctrl", "v")
    except Exception as e:
        print(e)
def translate_highlighted_text():#in window

    sleep(0.2)
    pyautogui.hotkey("ctrl", "c")
    sleep(0.2)
    copy_text = pyperclip.paste()
    transleted_text = GoogleTranslator(source='en', target='ru').translate(copy_text)
    sleep(0.5)
    pyautogui.alert(text=transleted_text, title='Translator', button='OK', timeout=10000)

keyboard.add_hotkey("right shift", lambda :copy_translate_paste())
keyboard.add_hotkey("ctrl+right shift", lambda :eng_to_russian_or_vice_versa())
keyboard.add_hotkey(
    "win+right shift", lambda :translate_highlighted_text(), )
keyboard.wait("right")
keyboard.wait("right")
keyboard.wait("right")
