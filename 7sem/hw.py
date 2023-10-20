import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

path_nails = 'nails'
path_labels = 'maski'
nails = os.listdir(path_nails)
#labels = os.listdir(path_labels)

def task(length):
  def func_selection(img1, img2, ind):
    #ind = np.random.randint(0,4)
    def rotate(img1, img2):
      angle = np.random.randint(0,361)
      h, w, d = img1.shape
      center = (h / 2, w / 2)

      rot_mat = cv2.getRotationMatrix2D(center, angle, 1.0)

      rotated1 = cv2.warpAffine(img1, rot_mat, (h, w))
      rotated2 = cv2.warpAffine(img2, rot_mat, (h, w))

      return rotated1, rotated2

    def flip(img1,img2):
      axis = np.random.randint(0,2)
      flip1 = cv2.flip(img1, axis)
      flip2 = cv2.flip(img2, axis)

      return flip1, flip2

    def crop(img1, img2):
      h, w, d = img1.shape
      bbox = np.random.randint(0, min(h,w), size=4)  # x, y, w, h
      crop1 = img1[bbox[1]:bbox[1] + bbox[3], bbox[0]:bbox[0] + bbox[2]]
      crop2 = img2[bbox[1]:bbox[1] + bbox[3], bbox[0]:bbox[0] + bbox[2]]

      return crop1, crop2

    def blur(img1, img2):
      k = np.random.randint(0,30) * 2 + 1
      blur1 = cv2.GaussianBlur(img1, (k,k), 3)
      blur2 = cv2.GaussianBlur(img2, (k,k), 3)

      return blur1, blur2

    f = [rotate(img1,img2), flip(img1,img2), crop(img1,img2), blur(img1,img2)]
    return f[ind]

  def generator(l, nails):
    arr = nails.copy()
    np.random.shuffle(arr)
    _nails = []
    _labels = []
    ind = np.random.randint(0,4)
    for i in range(l):
      path_label = path_labels + '/' + arr[i]
      path_nail = path_nails + '/' + arr[i]
      im2 = cv2.imread(path_label)
      im1 = cv2.imread(path_nail)
      im1,im2 = func_selection(im1,im2, ind)
      _nails.append(im1)
      _labels.append(im2)

    return _nails, _labels

  n, l = generator(length, nails)
  for i in range(length):
    n[i] = cv2.resize(n[i], dsize=(640, 480))
    l[i] = cv2.resize(l[i], dsize=(640, 480))
    result = cv2.hconcat([n[i],l[i]])
    cv2.imshow('Result', result)
    key = cv2.waitKey(0)
    if key == 32:
      continue

l=5
task(l)

while True:
  key = cv2.waitKey(0)
  if key == 32:
    task(l)
  if key == 27:
    break
