import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import datetime
import time

# def find_counturs(img):
#   img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#   T, thresh_img = cv2.threshold(img_gray, 70, 255, cv2.THRESH_BINARY)
#   cnts, _ = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#   image_out = np.zeros_like(img.shape)
#   image_out = cv2.drawContours(image_out, cnts, -1, (0, 255, 0), 2)
#   plt.imshow(image_out)

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

	final_img = cv2.drawMatches(img1, queryKP,
								img2, trainKP, matches[:53], None)

	good_matches = matches

	query_pts = np.float32([queryKP[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
	train_pts = np.float32([trainKP[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

	H, _ = cv2.findHomography(query_pts, train_pts, cv2.RANSAC, 5.0)

	h, w = img1.shape[:2]
	object_corners = np.array([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]], dtype=np.float32).reshape(-1, 1, 2)

	s = cv2.perspectiveTransform(object_corners, H)

	l = np.copy(img2)
	img_with_object_highlighted = cv2.polylines(l, [np.int32(s)], isClosed=True, color=(0, 255, 0), thickness=2)

	#final_img = cv2.resize(final_img, (1000, 650))
	# plt.imshow(final_img)
	# plt.show()
	# plt.imshow(img_with_object_highlighted)
	# plt.show()
	return img_with_object_highlighted


def search_and_highlight_object(img1, img2):
    sift = cv2.SIFT_create()

    keypoints_ghost, descriptors_ghost = sift.detectAndCompute(img1, None)

    keypoints_scene, descriptors_scene = sift.detectAndCompute(img2, None)

    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(descriptors_ghost, descriptors_scene, k=2)

    good_matches = []
    for m, n in matches:
        if m.distance < 0.5 * n.distance:
            good_matches.append(m)

    res = []
    while len(good_matches) > 1:
        src_pts = np.float32([keypoints_ghost[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
        dst_pts = np.float32([keypoints_scene[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
        H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

        h, w = img1.shape[:2]
        ghost_corners = np.array([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]], dtype=np.float32).reshape(-1, 1, 2)

        ghost_on_scene = cv2.perspectiveTransform(ghost_corners, H)
        res.append(ghost_on_scene)

        img_with_object_highlighted = img2.copy()
        cv2.polylines(img_with_object_highlighted, [np.int32(ghost_on_scene)], isClosed=True, color=(0, 255, 0),
                      thickness=2)

        good_matches = [match for i, match in enumerate(good_matches) if mask[i][0] == 0]

    img_with_object_highlighted = img2.copy
    for ghost_on_scene in res:
        cv2.polylines(img_with_object_highlighted, [np.int32(ghost_on_scene)], isClosed=True, color=(0, 255, 0),
                      thickness=2)

    return img_with_objects_highlighted


def search_and_highlight_objects2(img1, img2):
    sift = cv2.SIFT_create()
    keypoints_ghost, descriptors_ghost = sift.detectAndCompute(img1, None)
    keypoints_scene, descriptors_scene = sift.detectAndCompute(img2, None)

    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(descriptors_ghost, descriptors_scene, k=2)

    good_matches = []
    for m, n in matches:
        if m.distance < 0.5 * n.distance:
            good_matches.append(m)

    objects_on_scene = []  # Здесь будем хранить координаты объектов

    src_pts = np.float32([keypoints_ghost[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([keypoints_scene[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

    H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

    h, w = img1.shape[:2]
    ghost_corners = np.array([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]], dtype=np.float32).reshape(-1, 1, 2)
    ghost_on_scene = cv2.perspectiveTransform(ghost_corners, H)

    objects_on_scene.append(ghost_on_scene)

    img_with_objects_highlighted = img2.copy()

    for ghost_on_scene in objects_on_scene:
        cv2.polylines(img_with_objects_highlighted, [np.int32(ghost_on_scene)], isClosed=True, color=(0, 255, 0),
                      thickness=2)

    return img_with_objects_highlighted

phone = search_point(cg, phone)
phone = search_point(pg, phone)
phone = search_point(pg, phone)
plt.imshow(phone)
plt.show()