# -*- coding: utf-8 -*-
"""
Created on Feb 23 15:26:47 2018

@author: omerfarukkoc
"""

import cv2
import numpy as np
import sys
import time


def takePhoto(event, x, y, flags, param):
    global count

    global ix, iy

    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.imwrite("yuz%d.jpg" % count, roi_gray)

        print('yuz%d.jpg kaydedildi' % count)

        count = count + 1


count = 0
cv2.namedWindow('yuzAlgilaVeKaydet')

cv2.setMouseCallback("yuzAlgilaVeKaydet",takePhoto)

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

if cap.isOpened() == True:
    print('Kamera Açıldı')

else:
    print('HATA!! \nKamera Açılamadı!!')
    exit(1)

while (1):

    try:
        start = time.time()
        ret, frame = cap.read()

        if ret != True:
            print('HATA!! Frame Alınamıyor \nYeniden Başlatın')
            cv2.destroyAllWindows()
            cap.release()
            break
            exit(1)

        frame = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_LINEAR)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]

            cv2.imshow('roi_gray', roi_gray)


        cv2.putText(frame, "Algilanan Yuzu Kaydetmek icin Frame Uzerinde Cift Tiklayin", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
        cv2.imshow('yuzAlgilaVeKaydet', frame)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            print("Çıkış Yapıldı")
            break


    except:
        print("Beklenmedik Hata!!! ", sys.exc_info()[0])
        raise

cv2.destroyAllWindows()
cap.release()
