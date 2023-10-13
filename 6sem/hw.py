import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def task1():
    n=0
    maski = os.listdir('maski')
    nails = os.listdir('nails')

    def search(a):
        for i in range(a, len(maski)):
            for j in range(len(maski)):
                if maski[j] == nails[i]:
                    return ('maski/' + maski[j]), ('nails/' + nails[i])

    def f(n):
        cv2.namedWindow("Result", cv2.WINDOW_NORMAL)
        img_maski, img_nails = search(n)

        maska = cv2.imread(img_maski)

        nail = cv2.imread(img_nails)

        image_gray = cv2.cvtColor(maska, cv2.COLOR_RGB2GRAY)
        _, thresh = cv2.threshold(image_gray, 200, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        image_out = nail.copy()
        image_out = cv2.drawContours(image_out, contours, -1, (0, 255, 0), 2)

        result = cv2.hconcat([maska, image_out])
        cv2.imshow('Result', result)

    f(n)
    n+=1

    while True:
        key = cv2.waitKey(10) & 0xff
        if key == 32:
            f(n)
            n+=1
        if key==27:
            break


def task2():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        key = cv2.waitKey(10) & 0xff
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Frame', gray)
        if key == 27:  # Esc
            break

    cv2.destroyWindow('Frame')
    cap.release()

task2()

