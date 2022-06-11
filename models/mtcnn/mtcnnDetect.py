import cv2
from mtcnn import MTCNN
# import time

def load_img(dir):
  img = cv2.imread(dir)
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  return img

detector = MTCNN()

def Detect_face(image):
  faces = detector.detect_faces(image)
  return faces

def crop_face(image): 
  detections = Detect_face(image)
  for detection in detections:
    box = detection['box']            
    img_crop = image[box[1]: box[1] + box[3], box[0]: box[0] + box[2]] #img[x1:x2, y1:y2]
  return img_crop