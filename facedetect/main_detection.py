""""
Web Academy
FaceDetection
Version 1.0
Autor: Aleksii Savchenko
Kiev
-------------------------
First step:
pip3 install numpy
pip3 install opencv-python
pip3 install opencv-contrib-python
pip3 install Pillow

"""
from time import sleep

import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while 1:
    if not cap.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass

    ret, face_detection = cap.read()
    gray = cv2.cvtColor(face_detection, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(face_detection, (x, y), (x + w, y + h), (255, 0, 0), 1)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = face_detection[y:y + h, x:x + w]
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(face_detection, 'Your face is nice', (x - 15, y - 15), font, 0.6, (0, 255, 0), 1, cv2.LINE_AA)

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 1)

    cv2.imshow('FaceDetection', face_detection)
    k = cv2.waitKey(30) & 0xff  # Keyboard ESC
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
