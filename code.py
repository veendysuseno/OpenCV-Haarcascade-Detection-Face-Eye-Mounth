import numpy as np
import cv2

# Load the Haar cascades for face, eye, and mouth detection
face_cascade = cv2.CascadeClassifier('D:/A/OpenCV-Haarcascade/dataset/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('D:/A/OpenCV-Haarcascade/dataset/haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('D:/A/OpenCV-Haarcascade/dataset/haarcascade_mcs_mouth.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        mouths = mouth_cascade.detectMultiScale(roi_gray, 1.7, 11)
        for (mx, my, mw, mh) in mouths:
            # Adjust the y-position for the mouth to avoid false positives
            if my > h / 2:
                cv2.rectangle(roi_color, (mx, my), (mx + mw, my + mh), (0, 0, 255), 2)
                break

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == ord('e'):  # Press 'e' to exit
        break

cap.release()
cv2.destroyAllWindows()
