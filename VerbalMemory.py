#!/usr/bin/python
# -*- coding: utf-8 -*-
from PIL import Image
import pytesseract
import pyautogui
import time
import webbrowser
import sys

pytesseract.pytesseract.tesseract_cmd = \
    r'C:\Program Files\Tesseract-OCR\tesseract'  # need to install tesseract, windows installer: https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-3.05.02-20180621.exe

allWords = []

webbrowser.open('https://www.humanbenchmark.com/tests/verbal-memory',
                new=2)

time.sleep(3)  # time it takes for webbrowser to open, change this to match your pc
xStart = 951  # x pos center of the start button, change if you are using different res
yStart = 507  # y pos center of the start button, change if you are using different res
xSeen = 911  # x pos center of the seen button, change if you are using different res
ySeen = 441  # y pos center of the seen button, change if you are using different res
xNew = 1012  # x pos center of the new button, change if you are using different res
yNew = 441  # y pos center of the new button, change if you are using different res
delay = 1.0  # change this for delay in seconds between each round
lvls = 100  # change this to match how many lvls you want the bot to do

pyautogui.click(xStart, yStart)
time.sleep(.5)

color = pyautogui.pixel(xStart, yStart)
hexColor = '%02x%02x%02x' % color
pyautogui.moveTo(xStart, yStart)
for num in range(lvls):

    # takes picture of the word

    im1 = pyautogui.screenshot(region=(685, 333,
                                1235, 420))

    # converts image of word into text

    word = pytesseract.image_to_string(im1)
    print("check:",word)
    print(allWords)
    if word != "":        
        # checks if word is in the list of stored words and acts accordingly
        if word not in allWords:
            allWords.append(word)
            pyautogui.click(xNew, yNew)
        else:
            pyautogui.click(xSeen, ySeen)

    time.sleep(delay)