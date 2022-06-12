import time
import os
def test_zone():
    
    from main.action import Action
    start_time = time.time()
    dir = 'C:\\MyData\\Code\\project\\FaceRecognition\\FaceRecognition\\face\\face_test\\7.jpg'
    result = Action(dir)
    print(result)
    print(time.time() - start_time)
# test_zone()

# from handle.action import Action
# start_time = time.time()
# result = Action('C:/MyData/Code/project/FaceRecognition/projectAI_FCode/face/face_test/duyne.jpg')
# print(time.time() - start_time)
# print(result)

# from keras.models import load_model
# model = load_model('./model/arcface_model.h5', compile=False)
# model.summary()

# import sys
# print(sys.path.append('C:\\MyData\\Code\\project\\FaceRecognition\\projectAI_FCode'))
# print(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# face_folder = str(os.path.abspath(os.path.dirname(__file__))) + '\\face\\face_data'
# for root, dirs, files in os.walk(face_folder):
#     print(files)
# path = 'C:\\MyData\\Code\\project\\FaceRecognition\\projectAI_FCode\\model'
# isExist = os.path.exists('a.jpg')
# print(isExist)

# from multiface.action import Action

# a = Action('C:\\MyData\\myDesktop\\gdsa.jpg')

# print(a)

# print(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import requests
