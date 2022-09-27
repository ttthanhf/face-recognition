import os
from utilities.generate import getTimeStamp

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
            count_jpg = 0
            count_npy = 0
            for file in files:
                if file.endswith(".jpg"):
                    count_jpg += 1
                else:
                    count_npy += 1
            if(count_jpg > count_npy):
                totalJpgNotData = count_jpg - count_npy
                lengthFolder = len(files)
                for i in range(lengthFolder-totalJpgNotData,lengthFolder):
                    path = os.path.join(root, files[i])
                    data = Process(path)
                    save(str(root) + '/' + files[i] + '.npy', data)
                    addFile += 1
            else:
                existFile += 1
    print('Finish !')
    return totalFolder, addFile, existFile