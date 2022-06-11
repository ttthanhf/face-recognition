

from models.mtcnn.mtcnnDetect import crop_face, load_img

from models.arcface.arcfaceVerify import Represent
from main.alignFace import Align_face

import cv2

face_folder = 'C:\\MyData\\Code\\project\\FaceRecognition\\projectAI_F-Code\\face\\face_data'

def Process(dir):
    img = load_img(dir)
    img = Align_face(img)
    img = crop_face(img)
    img = cv2.resize(img, (112, 112))
    data = Represent(img)
    return data