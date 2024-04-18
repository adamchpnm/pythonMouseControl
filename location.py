import pytesseract
import pyautogui
import time
import webbrowser
import sys

pytesseract.pytesseract.tesseract_cmd = \
    r'C:\Program Files\Tesseract-OCR\tesseract'  # need to install tesseract, windows installer: https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-3.05.02-20180621.exe

while True:
    time.sleep(1)
    print(pyautogui.position())
    im1 = pyautogui.screenshot(region=(685, 333,
                                1235, 420))

    # converts image of word into text

    word = pytesseract.image_to_string(im1)
    print("check:",word)