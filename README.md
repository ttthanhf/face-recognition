This is the project face recognition using mtcnn to handle scan function, ultralight to detect faster and arcface to recognition.

! => To avoid unexpected errors, use the python version 3.7.9 <= !

How to setup!
> Do "git clone https[]()://github.com/ttthanhf/face-recognition.git"

>Run "pip3 install -r requirements.txt"
>>> Download weights : [Click here to download weights](https://drive.google.com/drive/folders/1uimIp4K-AAjk5EQBuVI8j9OYBgJCSUES?usp=sharing) (Put arcface_h5 folder and ultralight_onnx folder in weights folder)

To start server:
> Run "py main.py server start" (It will start with port 5000)

>*~If your computer has 16gb ram or more you can use docker to run this model !~*



-----

**Api:**

To verify face: 
>localhost:5000/api_v3 (Method: POST, Json: {url: "your url"})
>> => Output {
    status,
    name,
    execute_time,
}

To create new face: 
>localhost:5000/api_v3/create (Method: POST, Json: {url: "your url", name: "your name"})
>> => Output {
    status
    execute_time
}

To scan face: 
>localhost:5000/api_v3/scan (Method: GET)
>> => Output {
    add
    exist
    total
    execute_time
}

To get list: 
>localhost:5000/api_v3/list (Method: GET)
>> => Output {
    *json list*
}

To rename face: 
>localhost:5000/api_v3/rename (Method: POST, Json: {oldname: "your oldname", newname: "your newname"})
>> => Output {
    status
    execute_time
}

To delete face: 
>localhost:5000/api_v3/delete (Method: POST, Json: {name: "your name"})
>> => Output {
    status
    execute_time
}

*Example in folder webapp (it using fetch or axios)

*You can using Postman ! (set body to raw and using method and send it with json)
>ex: 
{
    "name": "Baka"
}

! You need to scan face before create new face !
! You can use test.py if you know :) !

if you have any problem, you can contact to me ! :)

Link source: https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB, https://github.com/ipazc/mtcnn, https://github.com/serengil/deepface, https://github.com/davidsandberg/facenet/




