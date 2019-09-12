# -*- coding: utf-8 -*-
"""
Created on Feb 24 19:27:07 2018

@author: omerfarukkoc
"""

import cv2
import numpy as np
import sys

#import RPi.GPIO as GPIO
from time import sleep
#GPIO.setmode(GPIO.BOARD)
#gpioPin = 10
#GPIO.setup(gpioPin, GPIO.OUT)

cap = cv2.VideoCapture(0)

if cap.isOpened() == True:
    print('Kamera Açıldı')

else:
    print('HATA!! \nKamera Açılamadı!!')
    exit(1)

while (1):

    try:
        ret, frame = cap.read()

        if ret != True:
            print('HATA!! Frame Alınamıyor \nYeniden Başlatın')
            cv2.destroyAllWindows()
            cap.release()
            break
            exit(1)
        
        #GPIO.output(gpioPin, GPIO.LOW)
        #frame = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_LINEAR)
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        template = cv2.imread('yuz0.jpg', 0)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.7
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
            #GPIO.output(gpioPin, GPIO.HIGH)
            cv2.putText(frame, "Yuz Algilandi", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)

        
        #GPIO.output(gpioPin, GPIO.LOW)
        cv2.imshow('kaydedilenYuzuTara', frame)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            print("Çıkış Yapıldı")
            #GPIO.output(gpioPin, GPIO.LOW)
            #GPIO.cleanup()
            break

    except:
        print("Beklenmedik Hata!!! ", sys.exc_info()[0])
        raise

cv2.destroyAllWindows()
cap.release()
