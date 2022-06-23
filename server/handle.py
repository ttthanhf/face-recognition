import os
import cv2
import shutil
import requests
from utilities.generate import getTimeStamp

face_folder = str(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) + '/face/face_data'

def List():
    labels = []
    for root, dirs, files in os.walk(face_folder):
        if(os.path.basename(root) != os.path.basename(face_folder)):
            label = os.path.basename(root)
            labels.append(label)
    return labels

def Rename(oldname, newname):
    path = face_folder + '/' + oldname
    if os.path.exists(path):
        if not oldname == newname:
            os.rename(path , face_folder + '/' + newname)
            return 'Rename sucess'
        else:
            return 'oldname and newname are the same'
    else:
        return 'oldname does not exist'
    
def Delete(name):
    name = str(name).replace(" ", "")
    if not name == "":
        if not '/' in name:
            if not '\\' in name:
                path = face_folder + '/' + name
                if os.path.exists(path):
                    shutil.rmtree(path)
                    return 'Delete sucess'
                else:
                    return 'name not exist'
            else:
                return 'Name can not contain \\ '
        else:
            return 'Name can not contain / '
    else:
        return 'Name can not be empty'

def Create_v1(file, name):
    if not '.' in name:
        path = face_folder + '/' + name
        if not os.path.exists(path):
            os.mkdir(path)
            file.save(path + '/' + getTimeStamp() + '.jpg')
            return 'Create success !'
        else:
            return 'name already exist !'
    else:
        return 'Name contain . is not allowed'

def Create_v2(path_input, name):
    if not '.' in name:
        path = face_folder + '/' + name
        if not os.path.exists(path):
            os.mkdir(path)
            img_src = cv2.imread(path_input)
            cv2.imwrite(path + '/' + getTimeStamp() + '.jpg', img_src)
            return 'Create success !'
        else:
            return 'name already exist !'
    else:
        return 'Name contain . is not allowed'

def Create_v3(path_input, name):
    if not '.' in name:
        path = face_folder + '/' + name
        if not os.path.exists(path):
            os.mkdir(path)
            img_src = cv2.imread(path_input)
            cv2.imwrite(path + '/' + getTimeStamp() + '.jpg', img_src)
            return 'Create success !'
        else:
            return 'name already exist !'
    else:
        return 'Name contain . is not allowed'

def createImageURL(path, url):
    img_data = requests.get(url).content
    with open(path, 'wb') as handler:
        handler.write(img_data)
    return 0

def Add_v3(path_input, name):
    if not '.' in name:
        path = face_folder + '/' + name
        if os.path.exists(path):
            img_src = cv2.imread(path_input)
            cv2.imwrite(path + '/' + getTimeStamp() + '.jpg', img_src)
            return 'Add success !'
        else:
            return 'name not exist !'
    else:
        return 'Name contain . is not allowed'

            
            