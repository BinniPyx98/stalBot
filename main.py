# import keyboard
# import time
import time

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


def getPath():
    path = os.getcwd()
    return path


def createDir(dirName):
    path = getPath()
    os.mkdir(path + '\\' + dirName)


def checkScreensDir():
    dirs = os.listdir()
    found = False
    for i in range(len(dirs)):
        if dirs[i] == 'screens':
            found = True
            break
    if not found:
        createDir('screens')


def create_screenshot():
    path = getPath()
    fullPath = path + '/screens'
    screenName = 'screen.png'
    screenshot = pyautogui.screenshot()
    screenshot.save(fullPath + '/' + screenName)


def loading_displaying_saving():
    img = cv2.imread('proto.png', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('girl', img)
    cv2.waitKey(0)
    cv2.imwrite('graygirl.jpg', img)


def findProto(pathToProtoTmp):
    found = pyautogui.locateOnScreen(pathToProtoTmp, grayscale=True, confidence=0.8)
    print(found)

checkScreensDir()
path = getPath()
pathToProtoTmp = path + '/screens/proto.png'

start = True
while start:
    # create_screenshot()
    try:
        findProto(pathToProtoTmp)
    except pyautogui.ImageNotFoundException:
        print("Image not found")
        time.sleep(10)
    else:
        print('Image found')
        time.sleep(140)

