import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import datetime
import time

cg = cv2.imread('candy_ghost.png')[:, :, ::-1]
pg = cv2.imread('pampkin_ghost.png')[:, :, ::-1]
sg = cv2.imread('scary_ghost.png')[:, :, ::-1]
phone = cv2.imread('lab7.png')[:, :, ::-1]

def search_point(img1, img2):
    orb = cv2.ORB_create()
    queryKP, queryDes = orb.detectAndCompute(img1, None)
    trainKP, trainDes = orb.detectAndCompute(img2, None)
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = matcher.match(queryDes, trainDes)
    matches = sorted(matches, key=lambda x: x.distance)

    #final_img = cv2.drawMatches(img1, queryKP, img2, trainKP, matches[:100], None)

    good_matches = matches

    query_pts = np.float32([queryKP[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    train_pts = np.float32([trainKP[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

    H, _ = cv2.findHomography(query_pts, train_pts, cv2.RANSAC, 5.0)

    h, w = img1.shape[:2]
    object_corners = np.array([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]], dtype=np.float32).reshape(-1, 1, 2)

    s = cv2.perspectiveTransform(object_corners, H)

    l = np.copy(img2)
    img_with_object_highlighted = cv2.polylines(l, [np.int32(s)], isClosed=True, color=(0, 255, 0), thickness=2)

    # final_img = cv2.resize(final_img, (1000, 650))
    # plt.imshow(final_img)
    # plt.show()
    return len(matches)
    # plt.imshow(img_with_object_highlighted)
    # plt.show()
    #return img_with_object_highlighted


def search_contours(img):
    im = img.copy()
    im = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
    im = cv2.GaussianBlur(im, (25,25), 0)
    _, thresh = cv2.threshold(im, 190, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    arr = []
    for i in contours:
        if cv2.contourArea(i)>1100:
            arr.append(i)
    contours = arr.copy()

    for i in range(len(contours)):
        for j in range(len(contours) - i - 1):
            if cv2.contourArea(contours[j]) > cv2.contourArea(contours[j+1]):
                contours[j], contours[j+1] = contours[j+1], contours[j]

    buf = []

    for i in contours[::-1]:
        flag = 0
        x1,y1,w1,h1 = cv2.boundingRect(i)
        for j in contours[::-1]:
            x2, y2, w2, h2 = cv2.boundingRect(j)
            if x2<x1 and y2<y1 and x2+w2 > x1+w1 and y2+h2 > y1+h1:
                flag=1
                break
        if flag==0:
            buf.append(i)

    res_arr = []

    for i in buf:
        if cv2.contourArea(i)<37000:
            x, y, w, h = cv2.boundingRect(i)
            res_arr.append((x,y,w,h))
            #cv2.rectangle(res, (x, y), (x + w, y + h), (0, 0, 255), 5)
            arr.append(i)

    return res_arr

def f(arr):
    x,y,w,h = arr
    result = phone[y-20:y+h+20, x-20:x+w+20]
    # plt.imshow(result)
    # plt.show()
    return result

def g(p,s,c):
    if p>s and p>c:
        return 'p'
    if s>c and s>p:
        return 's'
    if c>s and c>p:
        return 'c'

def task():
    arr = search_contours(phone)
    img = phone.copy()

    res = {'p':(0, 255, 255), 's':(0, 0, 255), 'c':(0, 255, 0)}

    for i in range(len(arr)):
        crop=f(arr[i])
        p = search_point(pg, crop)
        s = search_point(sg, crop)
        c = search_point(cg, crop)

        x, y, w, h = arr[i]
        color = res[g(p,s,c)]
        img = cv2.rectangle(img, (x - 20, y - 20), (x + w + 20, y + h), color, 3)

    img = cv2.resize(img[:,:,::-1], (1280, 720))
    cv2.imshow('Ghosts on picture', img)

    cv2.waitKey(0)

task()