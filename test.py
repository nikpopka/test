from ctypes import windll, Structure, c_long, byref

import time
# import cv2
# import mss
# import numpy as np

import pyautogui




def click():
    pyautogui.mouseDown()
    time.sleep(0.01)
    pyautogui.mouseUp()

def zabros():
    pyautogui.press('A')

def lovit():
    pyautogui.press('a')
time.sleep(2)
n = 10.5
while True:

    # пробуждаем лост
    pyautogui.moveTo(570, 145)
    click()

    # переводим курсор в воду
    pyautogui.moveTo(570, 800)
    time.sleep(0.1)


    pyautogui.press('a') # забросил удочку
    print('старт',time.time())
    print('закинул...')
    time.sleep(0.1)

    # переход
    pyautogui.moveTo(3000, 150)
    click()
    pyautogui.moveTo(570, 145)
    click()



    time.sleep(n)
    pyautogui.moveTo(570, 145)
    click()
    time.sleep(0.1)
    pyautogui.press('a')  # достал
    print('стоп',time.time())
    pyautogui.moveTo(3000, 150)
    time.sleep(30)

