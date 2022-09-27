from models.ultralight.ultralightDetect import crop_face, load_img, Detect_face
from models.arcface.arcfaceVerify import Represent
from main.distance import cosineDistance
from numpy import load
import cv2
import os

face_folder = str(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) + '/face/face_data'

def Process(dir):
    data_array = []
    img = load_img(dir)
    boxes, status = Detect_face(img)
    if(status):
        for box in boxes:
            img = crop_face(img, box)
            img = cv2.resize(img, (112, 112))
            data = Represent(img) #spend most time execute # optimized best
            data_array.append(data)
        return data_array, True
    else:
        return 0, False
    

def Action(dir):
    data_label = []
    data_img, status = Process(dir)
    # if(status):
        # #each person data load cost 0.001s
        # for root, dirs, files in os.walk(face_folder):
        #     for file in files:
        #         if file.endswith('.npy'):
        #             label = os.path.basename(root)
        #             data = load(str(root) + '/' + 'data.npy')
        #             distance_cosine = cosineDistance(data_img, data)
        #             if(distance_cosine < 0.4):
        #                 data_label.append(label)
    return data_img