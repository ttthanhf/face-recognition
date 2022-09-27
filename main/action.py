from models.ultralight.ultralightDetect import crop_face, load_img, Detect_face
from models.arcface.arcfaceVerify import Represent
from main.distance import cosineDistance
import cv2
import os
from numpy import load
# import time

# from models.mtcnn.mtcnnDetect import crop_face, load_img
# from main.alignFace import Align_face

face_folder = str(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) + '/face/face_data'

def Process(dir):
    #ultralight
    img = load_img(dir)
    # img = Align_face(img)
    boxes, status = Detect_face(img)
    if(status):
        img = crop_face(img, boxes)
        img = cv2.resize(img, (112, 112))
        data = Represent(img) #spend most time execute # optimized best
        return data, True
    else:
        return 0, False
        
    #mtcnn
    # img = load_img(dir)
    # img = Align_face(img)
    # img = crop_face(img)
    # img = cv2.resize(img, (112, 112))
    # data = Represent(img)
    # return data, True


def Action(dir):
    data_img, status = Process(dir)
    if(status):
        # #each person data load cost 0.001s
        for root, dirs, files in os.walk(face_folder):
            for file in files:
                if file.endswith('.npy'):
                    data = load(str(root) + '/' + file)
                    distance_cosine = cosineDistance(data_img, data)
                    if(distance_cosine < 0.4):
                        label = os.path.basename(root)
                        return 'Not thing wrong' ,label
        return 'Cannot find face in data', 0
    return 'Cannot detect face', 0