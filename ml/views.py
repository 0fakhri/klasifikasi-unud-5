from django.http.response import JsonResponse
from django.shortcuts import render
import os
import tensorflow
from tensorflow.keras.models import load_model

import requests
from io import BytesIO 
from PIL import Image
import numpy as np

#def function here
def predictNab(clf, img):
    input_size = (300,300) # Bisa kalian ganti#define input shape
    channel = (3,)
    input_shape = input_size + channel
    #define labels
    labels = ['jahe', 'kunyit']

    def preprocess(img,input_size):
        nimg = img.convert('RGB').resize(input_size, resample= 0)
        img_arr = (np.array(nimg))/255
        return img_arr

    def reshape(imgs_arr):
        return np.stack(imgs_arr, axis=0)

    # read image
    pil_image_obj = Image.open(model_instance.image_field)
    im = Image.open('/content/drive/MyDrive/WhatsApp Image 2021-08-17 at 12.27.34.jpeg')
    print(im)
    X = preprocess(im,input_size)
    X = reshape([X])
    y = clf.predict(X)
    nab = labels[np.argmax(y)]
    # print('akurasi :', np.max(y))
    # print('label :', labels[np.argmax(y)])
  return nab

# Create your views here.
def index(request):
    context = {
        'css': 'ini link css'
    }
    return render(request, 'index.html', context)

def predictnab(request):
    img = request.FILES['my_uploaded_file'].read()
    img = float(request.POST['ihsg'])
    # print >>sys.stderr, 'Goodbye, cruel world!'
    print (img)
    # unit = float(request.POST['unit'])
    model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'my_model_herbal.h5')
    clf = load_model(model_path)
    result = predictNab(clf, img)
    print('result = ', result)
    return JsonResponse({
        'result': str(result[0])
    })