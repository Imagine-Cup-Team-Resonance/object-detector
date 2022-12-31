# Object Detector

Object Detector is a software application that uses computer vision techniques to detect a specific object in scenes. The software will be able to accept an image as input and detect the presence of a specific object in image.  

## Scope
The Object Detector software find it’s application in various sectors such as object recognition (in image tagging and search), object tracking (can use object detection to track the movement of objects in a video, which can be useful in applications such as surveillance and robotics), object localization (can be useful in image annotation and object manipulation), scene understanding etc.

This repository is dedicated for implmentation of a software solution that would help facilitate users to upload the object and scene images and get the image of object highlighted in the scene image.

## Project Details

The project is divided into three parts:  
1. Frontend which will interact with users and facilitate upload and display images.
2. Backend which will store the images and send it to the object detector model.
3. Object Detector Model which will detect the given object in the given scene.

## Technology
1. HTML/CSS/JS
2. Bootstrap
3. Python
4. Django Framework
5. Computer Vision

## Run
1. Create a clone of this project using GIT clone.
2. Install all the dependicies from the requirements.txt using this command:
```
pip install -r requirements.txt
```
3. Start the local server on your machine using command:
```
python manage.py runserver
```
A local server will be started at the address:
```
http://127.0.0.1:8000/
```
Copy it and paste it in the browser and you will be redirected to the home page of the web application.
4. You can now upload the images and check the result after submitting.

## Interface
Our web application provide the ability of uploading the object image and the scene image and our system will do the work to run the model and show the resulted image.

<img src="statics\homepage.jpg" />  

The image uploaded will be send to the backend and will be examined by the "Object Detector" model and will be displayed in the web app like this:

<img src="statics\resultpage.jpg" />

## Demo

Link: https://www.loom.com/share/68ebf45fd12f4fdf9994065e2ffacc4b
