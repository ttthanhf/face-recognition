# Face Regconition
<br>
<div align='center'>
<img src="https://img.shields.io/badge/Python-3.7.9-blue"> <img src="https://img.shields.io/badge/Build-Passing-green"> <img src="https://img.shields.io/badge/Docker-Yes-green"> <img src="https://img.shields.io/badge/Test_In_Server-Yes-green"> <img src="https://img.shields.io/badge/Testing-Done-green"> <img src="https://img.shields.io/badge/API-Yes-green">
</div>
<br>

This is the project face recognition using MTCNN to handle scan function, ultralight to detect face and arcface to recognition.



<br>

# How to setup!
- Do "git clone https[]()://github.com/ttthanhf/face-recognition.git"
- cd to the folder "face-recognition"
- Run "pip3 install -r requirements.txt"
- Download weights : [Click here to download weights](https://drive.google.com/drive/folders/1uimIp4K-AAjk5EQBuVI8j9OYBgJCSUES?usp=sharing) (Put arcface_h5 folder and ultralight_onnx folder in weights folder)
<br><br><br>

# To start server:
- cd to your folder "face-recognition"
- Run "py main.py server start" (It will start with port 5000)

>*~If your computer has 16gb ram or more you can use docker to run this model !~*

<br>

# API
> using json in body web request.

- api_v1 : using upload image.
- api_v2 : using path of image in local. (Body: Json: {path: "your url", name: "your name"})
- api_v3 : using url of image. (Body: Json: {url: "your url", name: "your name"})

<hr>
<br>

- / (method: POST) : recognition face
> Input: (*look*)
```
=> Output { status , 
            name , 
            execute_time 
          }
```
<br>

- /create (method: POST) : insert new image
```
=> Output { status , 
            execute_time
          }
```
<br>

- /add (method: POST) : add more image
```
=> Output { status , 
            execute_time 
          }
```
<br>

- /delete (method POST) : delete data user
> Input: json ({name: "your name"})

> => Output { status , execute_time }
<br>

- /scan (method: GET) : generate data face
> => Output { add , exist , total , execute_time }
<br>

- /list (method: GET) : show all user
> => Output { *json list* }
<br>

- /rename (method POST) : rename user in database
> Input: Json ({oldname: "your oldname", newname: "your newname"})

> => Output { status , execute_time }
<br>

# Example


*Example in folder webapp (it using fetch or axios)

*You can using Postman ! (set body to raw and using method and send it with json)
>ex: 
{
    "name": "Baka"
}

# Note
! You need to scan face before create new face !
<br><br>
! => To avoid unexpected errors, use the python version 3.7.9 <= !
<br>

# Reference : 
- https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB
- https://github.com/ipazc/mtcnn
- https://github.com/serengil/deepface
- https://github.com/davidsandberg/facenet/
- https://viblo.asia/p/paper-explained-some-face-recognition-approaches-facenet-arcface-cosface-Do754zgLZM6

# Contact
if you have any problem, you can contact to me ! :)




