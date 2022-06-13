from main.action import Action
from scan.scan import Scan
from server.handle import List, Create_v1, Create_v2, Create_v3, Rename, Delete, createImageURL
# from delete import Delete

import time
import os

from flask import Flask, request, jsonify


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = str(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    # response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
 
@app.route('/')
def a():
    return 'This project made by Tran Tan Thanh'

@app.route('/test')
def api_result():
    start_time = time.time()

    dir = str(os.path.abspath(os.path.dirname(__file__))) + '/face/face_test/duyne.jpg'

    status, result = Action(dir)

    return {
        'status': status,
        'name': result,
        'time_excute': time.time() - start_time
    }

@app.route('/api_v1', methods=['GET','POST'])
def api1():
    start_time = time.time()
    if request.method == 'POST':
        file = request.files['file']
        filename = str(file.filename)
        if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
            path = os.path.join(app.config['UPLOAD_FOLDER'], 'image.jpg')
            file.save(path)
            path_img = str(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) + '/image.jpg'
            status, result = Action(path_img) #main handle and recieve result
            return {
                'status': status,
                'name': result,
                'time_excute': time.time() - start_time
            }
        elif filename == '':
            print('No file has been sent !')
            return {
                'status': 'No file has been sent !',
                'name': 0,
                'time_excute': time.time() - start_time
            }
        print('File is not allowed !')
        return {
            'status': 'File is not allowed !',
            'name': 0,
            'time_excute': time.time() - start_time
        }
    if request.method == 'GET':
        print('get')
        return {
            'status': 'get',
            'name': 'get'
        }

@app.route('/api_v1/create', methods=['POST'])
def create_function():
    start_time = time.time()
    file = request.files['file']
    name = request.form.get('name')
    status = Create_v1(file, name)
    return {
        'status': status,
        'time_excute': time.time() - start_time
    }

#api version 2 is using path and name to interact with server
@app.route('/api_v2', methods=['GET','POST'])
def api2():
    if request.method == 'POST':
        start_time = time.time()
        path = request.json.get('path')
        status, result = Action(str(path))
        return {
                'status': status,
                'name': result,
                'time_excute': time.time() - start_time
        }

@app.route('/api_v2/create', methods=['GET','POST'])
def api2_create():
    if request.method == 'POST':
        start_time = time.time()
        name = request.json.get('name')
        path = request.json.get('path')
        status = Create_v2(path, name)
        return {
        'status': status,
        'time_excute': time.time() - start_time
        }

#api version 3 is using url and name to interact with server
@app.route('/api_v3', methods=['GET','POST'])
def api3():
    if request.method == 'POST':
        start_time = time.time()
        url = request.json.get('url')
        path = os.path.dirname(os.path.abspath(os.path.dirname(__file__))) + '/image.jpg'
        createImageURL(path,url)
        status, result = Action(str(path))
        return {
            'status': status,
            'name': result,
            'time_excute': time.time() - start_time
        }

@app.route('/api_v3/create', methods=['GET','POST'])
def api3_create():
    if request.method == 'POST':
        start_time = time.time()
        name = request.json.get('name')
        url = request.json.get('url')
        path = os.path.dirname(os.path.abspath(os.path.dirname(__file__))) + '/image.jpg'
        createImageURL(path,url)
        status = Create_v3(path, name)
        return {    
            'status': status,
            'time_excute': time.time() - start_time
        }


#other    
@app.route('/api_v1/scan')
@app.route('/api_v2/scan')
@app.route('/api_v3/scan')
def scan_function():
    start_time = time.time()
    total, addFile, existFile = Scan()
    return {
        'total': total,
        'add': addFile,
        'exist': existFile,
        'time_excute': time.time() - start_time
    }

@app.route('/api_v1/list')
@app.route('/api_v2/list')
@app.route('/api_v3/list')
def list_function():
    list = List()
    return jsonify(list)

@app.route('/api_v1/rename', methods=['POST'])
@app.route('/api_v3/rename', methods=['POST'])
@app.route('/api_v2/rename', methods=['POST'])
def rename_function():
    start_time = time.time()
    oldname = request.json.get('oldname')
    newname = request.json.get('newname')
    status = Rename(oldname,newname)
    return {
        'status': status,
        'time_excute': time.time() - start_time
    }

@app.route('/api_v1/delete', methods=['POST'])
@app.route('/api_v3/delete', methods=['POST'])
@app.route('/api_v2/delete', methods=['POST'])
def delete_function():
    start_time = time.time()
    name = request.json.get('name')
    status = Delete(name)
    return {
        'status': status,
        'time_excute': time.time() - start_time
    }

def start():
    app.run(host="0.0.0.0") 
app.run(host="0.0.0.0")

