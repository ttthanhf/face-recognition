import os

from scan.action import Process
from numpy import save

face_folder = str(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) + '/face/face_data'

def Scan():
    totalFolder = 0
    addFile = 0
    existFile = 0
    print('Scanning...')
    for root, dirs, files in os.walk(face_folder):
        if(os.path.basename(root) != os.path.basename(face_folder)):
            totalFolder += 1
            if(len(files) == 1):
                for file in files:
                    path = os.path.join(root, file)
                    data = Process(path)
                    save(str(root) + '/' + 'data.npy', data)
                addFile += 1
            else:
                existFile += 1
    print('Finish !')
    return totalFolder, addFile, existFile
# Scan()