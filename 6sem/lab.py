# import cv2
# import numpy as np
#
# cap = cv2.VideoCapture(0)
#
# fgbg = cv2.createBackgroundSubtractorMOG2()
#
# while True:
#     ret, frame = cap.read()
#
#     if not ret:
#         break
#
#     res = np.zeros((500, 500, 3))
#     res[:]=(0,255,0)
#
#     fgmask = fgbg.apply(frame)
#
#     fgmask = cv2.erode(fgmask, None, iterations=2)
#     fgmask = cv2.dilate(fgmask, None, iterations=2)
#
#     contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
#     for contour in contours:
#         if cv2.contourArea(contour) > 1000:
#             x, y, w, h = cv2.boundingRect(contour)
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#             res[:] = (0, 0, 255)
#
#     cv2.imshow('Motion Detection', frame)
#     cv2.imshow('res', res)
#
#     if cv2.waitKey(30) & 0xFF == 27:
#         break
#
# cap.release()
# cv2.destroyAllWindows()

import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

def lab():
    cam = cv2.VideoCapture(0)

    ret, frame1 = cam.read()
    ret, frame2 = cam.read()

    start_time = time.time()
    n=0

    while True:
        key = cv2.waitKey(30) & 0xff

        cur_time = time.time() - start_time

        if cur_time < 10 and n%2 == 0:
            frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
            frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

            frame1_gray = cv2.GaussianBlur(frame1_gray, (21, 21), 0)
            frame2_gray = cv2.GaussianBlur(frame2_gray, (21, 21), 0)

            frame_delta = cv2.absdiff(frame1_gray, frame2_gray)

            _, thresh = cv2.threshold(frame_delta, 10, 255, cv2.THRESH_BINARY)
            #thresh = cv2.erode(thresh, None, iterations=2)
            #thresh = cv2.dilate(thresh, None, iterations=2)

            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            res = np.zeros((frame1.shape))
            res[:]=(0,255,0)

            font = cv2.FONT_HERSHEY_SIMPLEX
            org = (50, 50)
            fontScale = 0.8
            thickness = 2

            for i in contours:
                if cv2.contourArea(i) > 1000:
                    x, y, w, h = cv2.boundingRect(i)
                    cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 0, 255), 5)
                    res[:] = (0, 0, 255)

        frame1 = cv2.putText(frame1, '"Red light" - motion detected', (10, 30), font, fontScale, (0,0,255), thickness, cv2.LINE_AA)
        cv2.imshow('Frame', frame1)
        cv2.imshow('Result', res)

        frame1 = frame2
        ret, frame2 = cam.read()

        if cur_time < 10 and n % 2 == 1:
            res[:] = (0, 255, 0)
            frame1 = cv2.putText(frame1, '"Green light" - no movement detected.', (10, 30), font, fontScale, (0,255,0),
                                 thickness, cv2.LINE_AA)
            #result = cv2.hconcat([frame1, res])
            cv2.imshow('Frame', frame1)
            cv2.imshow('Result', res)
            #cv2.imshow('Result', result)

        if cur_time >= 10:
            n += 1
            n = n%2
            start_time = time.time()
            frame1 = frame2

        if key == 27:
            break;

    cv2.destroyWindow('Frame')
    cap.release()

lab()