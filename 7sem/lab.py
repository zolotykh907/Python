import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import datetime
import time

cg = cv2.imread('candy_ghost.png')[:,:,::-1]
pg = cv2.imread('pampkin_ghost.png')[:,:,::-1]
sg = cv2.imread('scary_ghost.png')[:,:,::-1]
phone = cv2.imread('lab7.png')[:,:,::-1]

def search_contours(img):
	im = img.copy()
	im = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
	im = cv2.GaussianBlur(im, (39,39), 0)
	_, thresh = cv2.threshold(im, 120, 255, cv2.THRESH_BINARY)
	contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	return thresh

def search_points(img1, img2):
	MIN_MATCH_COUNT = 10
	# orb = cv2.ORB_create()
	# queryKP, queryDes = orb.detectAndCompute(img1,None)
	# trainKP, trainDes = orb.detectAndCompute(img2,None)

	# orb = cv2.ORB_create()
	# kp1, des1 = orb.detectAndCompute(img1,None)
	# kp2, des2 = orb.detectAndCompute(img2,None)
	# matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
	# matches = matcher.match(des1,des2)
	# matches = sorted(matches, key = lambda x:x.distance)

	sift = cv2.SIFT_create()
	# Используйте SIFT, чтобы найти ключевые точки и дескрипторы
	kp1, des1 = sift.detectAndCompute(img1, None)
	kp2, des2 = sift.detectAndCompute(img2, None)

	FLANN_INDEX_KDTREE = 1
	index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
	search_params = dict(checks=50)
	flann = cv2.FlannBasedMatcher(index_params, search_params)
	matches = flann.knnMatch(des1, des2, k=2)

	good = []
	for m, n in matches:
		if m.distance < 0.7 * n.distance:
			good.append(m)

	if len(good) > MIN_MATCH_COUNT:
		# Получить положение совпадающей точки в исходном изображении и целевом изображении
		# kp1: особенности исходного изображения
		# m.queryIdx: индекс совпадающей точки в характерной точке исходного изображения.
		# .pt: координаты характерной точки.
		src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
		dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
		# Получить матрицу преобразования, используя алгоритм RANSAC
		M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
		matchesMask = mask.ravel().tolist()
		# Преобразование изображения, преобразовать исходное изображение в форму, соответствующую обнаруженному изображению
		# Получить исходный размер изображения
		h, w, d = img1.shape
		# Используйте полученную матрицу преобразования для преобразования четырех углов исходного изображения, чтобы получить соответствующие координаты на целевом изображении.
		pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]
						 ).reshape(-1, 1, 2)
		# Трансформируем угловые точки
		dst = cv2.perspectiveTransform(pts, M)
		# Нарисуйте границу
		img2 = cv2.polylines(img2, [np.int32(dst)], True, 255, 5, cv2.LINE_AA)
	else:
		print("Not enough matches are found - {}/{}".format(len(good), MIN_MATCH_COUNT))
		matchesMask = None

	# Нарисуйте совпадающие точки
	draw_params = dict(matchColor=(0, 255, 0),  # draw matches in green color
					   singlePointColor=None,
					   matchesMask=matchesMask,  # draw only inliers
					   flags=2)
	img3 = cv2.drawMatches(img1, kp1, img2, kp2, good, None, **draw_params)
	plt.imshow(img3), plt.title('Result'),

	# final_img = cv2.drawMatches(img1, queryKP, img2, trainKP, matches[:50],None)
	#
	# final_img = cv2.resize(final_img, (1000,650))
	# plt.imshow(final_img)
	# plt.show()

im = search_contours(phone)
plt.imshow(im, cmap='gray')
plt.show()

f = phone[100:200, 200:500]
plt.imshow(f)
plt.show()