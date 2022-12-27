from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import viewsets, status
from django.core import serializers
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import image
from .serializers import imageSerializers
from .forms import ImageForm
import pandas as pd
from django.core.files.storage import FileSystemStorage
from . import object_detector_model
from PIL import Image
import numpy as np
from io import BytesIO
import os
import cv2
from django.core.files.images import ImageFile
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile

class ImageView(viewsets.ModelViewSet):
    queryset = image.objects.all()
    serializer_class = imageSerializers

def detect(images):
    # machine learning model
    folder = "results/"
    imgs = []
    for img in images:
        imgs.append(img.object_image)
        imgs.append(img.background_image)
        imgs.append(img.description)
    
    object = imgs[0]
    scene = imgs[1]
    des = imgs[2]
    
    pil_obj_img = Image.open(imgs[0])
    object_img_array = np.array(pil_obj_img)

    pil_scene_img = Image.open(imgs[1])
    scene_img_array = np.array(pil_scene_img)

    result_img_pil = object_detector_model.detect(scene_img_array, object_img_array)


    buffer = BytesIO()
    result_img_pil.save(buffer, format='JPEG')
    result_image_png = ContentFile(buffer.getvalue())

    # result_image_png = self.cleaned_data['result_image_png']

    # image.objects.all().delete()

    # image.objects.create(object_image=object, background_image=scene, description=des, result_image=ContentFile(result_image_png))

    obj = image.objects.all()[0]

    obj.result_image.save("result.jpg", InMemoryUploadedFile(
        result_image_png,
        None,
        "result.jpg",
        'image/jpeg',
        result_image_png.tell,
        None
    ))

    obj.save()

    return obj




def uploadImages(request):
    if request.method == 'POST':
        image.objects.all().delete()
        oi = request.FILES.get('object-image')
        bi = request.FILES.get('background-image')
        descr = request.POST['description']
        image.objects.create(object_image=oi, background_image=bi, description=descr)
        images = image.objects.all()
        currentModel = detect(images)
        return render(request, 'results/result.html', {'images': currentModel})
    
    return render(request, 'introduction/index.html')