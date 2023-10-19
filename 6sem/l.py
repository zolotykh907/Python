import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import datetime
import time

cg = cv2.imread('/content/drive/MyDrive/Colab_Notebooks/python/ghosts/candy_ghost.png')[:,:,::-1]
pg = cv2.imread('/content/drive/MyDrive/Colab_Notebooks/python/ghosts/pampkin_ghost.png')[:,:,::-1]
sg = cv2.imread('/content/drive/MyDrive/Colab_Notebooks/python/ghosts/scary_ghost.png')[:,:,::-1]
phone = cv2.imread('/content/drive/MyDrive/Colab_Notebooks/python/ghosts/lab7.png')[:,:,::-1]

def search_contours(img):
	im = img.copy()
	im = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
	#im = cv2.GaussianBlur(im, (21,21), 0)
	_, thresh = cv2.threshold(im, 80, 255, cv2.THRESH_BINARY)
	contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	res = img.copy()
	return res

def search_points(img1, img2):
	orb = cv2.ORB_create()
	queryKP, queryDes = orb.detectAndCompute(img1,None)
	trainKP, trainDes = orb.detectAndCompute(img2,None)

	orb = cv2.ORB_create()
	queryKP, queryDes = orb.detectAndCompute(img1,None)
	trainKP, trainDes = orb.detectAndCompute(img2,None)
	matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
	matches = matcher.match(queryDes,trainDes)
	matches = sorted(matches, key = lambda x:x.distance)
	final_img = cv2.drawMatches(img1, queryKP,
                            img2, trainKP, matches[:50],None)

	final_img = cv2.resize(final_img, (1000,650))
	plt.imshow(final_img)
	plt.show()

#search_contours(cg)
search_points(cg, phone)
search_points(pg, phone)
search_points(sg, phone)
plt.show()