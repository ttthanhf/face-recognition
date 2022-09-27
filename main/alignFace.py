
from main.distance import euclideanDistance
from models.mtcnn.mtcnnDetect import Detect_face
from PIL import Image
import math
import numpy as np

def align_eye(img, left_eye, right_eye):

	left_eye_x, left_eye_y = left_eye
	right_eye_x, right_eye_y = right_eye

	#find rotation direction
	if left_eye_y > right_eye_y:
		point_3rd = (right_eye_x, left_eye_y)
		direction = -1 
	else:
		point_3rd = (left_eye_x, right_eye_y)
		direction = 1 #rotate inverse direction of clock

	a = euclideanDistance(np.array(left_eye), np.array(point_3rd))
	b = euclideanDistance(np.array(right_eye), np.array(point_3rd))
	c = euclideanDistance(np.array(right_eye), np.array(left_eye))

	if b != 0 and c != 0: #this multiplication causes division by zero in cos_a calculation

		cos_a = (b*b + c*c - a*a)/(2*b*c)
		angle = np.arccos(cos_a) #angle in radian
		angle = (angle * 180) / math.pi #radian to degree

		if direction == -1:
			angle = 90 - angle

		img = Image.fromarray(img)
		img = np.array(img.rotate(direction * angle))

	return img

def Align_face(image):
  detections = Detect_face(image)
  for detect in detections:
    keypoints = detect["keypoints"]
    r_eye = keypoints['right_eye']
    l_eye = keypoints['left_eye']
    face_align = align_eye(image, l_eye, r_eye)
    return face_align