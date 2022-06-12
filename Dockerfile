FROM python:3.7.9

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY requirements.txt .
RUN pip3 install -r requirements.txt

WORKDIR /project/faceRecognition

ENV PORT 5000

COPY . /project/faceRecognition

CMD [ "python", "main.py", "server", "start" ]

