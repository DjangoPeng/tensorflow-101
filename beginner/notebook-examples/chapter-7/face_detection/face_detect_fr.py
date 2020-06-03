# -*- coding: utf-8 -*-

import cv2
import sys

import face_recognition


# Get user supplied values
imagePath = sys.argv[1]

# Load the image with face_recognition
image = face_recognition.load_image_file(imagePath)
# Detect faces in the image
face_locations = face_recognition.face_locations(image)

print("Found {0} faces!".format(len(face_locations)))


# Read the image with openCV
image = cv2.imread(imagePath)

# Draw a rectangle around the faces
for (top, right, bottom, left) in face_locations:
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)


cv2.imshow("Faces found", image)
cv2.waitKey(0)