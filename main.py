# import keyboard
# import time
import cv2
import pyautogui
import os


# start = True
# while start:
#     keyboard.press('w')
#     keyboard.press('shift')
#     print('w')
#     time.sleep(6)
#     keyboard.release('w')
#     start = False

def create_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save(r'/screen.png')


def getPath():
    path = os.getcwd()
    return path


def createDir(dirName):
    path = getPath()
    os.mkdir(path+'\\'+dirName)

def loading_displaying_saving():
    img = cv2.imread('proto.png', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('girl', img)
    cv2.waitKey(0)
    cv2.imwrite('graygirl.jpg', img)


createDir('screens')
# create_screenshot()
