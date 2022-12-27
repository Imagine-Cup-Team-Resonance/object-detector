# All plots will be displayed directly below the code cell that produced it
from matplotlib import pyplot as plt
from IPython.display import clear_output
# Set inline plots size
plt.rcParams["figure.figsize"] = (16, 10) # (w, h)
# Remove grid lines
import numpy as np
import time
import cv2
import math
import scipy.stats as st
import imutils
from PIL import Image

# function to read and resize an image
def read_and_resize(filename, grayscale = False, fx= 0.5, fy=0.5):
    if grayscale:
      img_result = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    else:
      imgbgr = cv2.imread(filename, cv2.IMREAD_COLOR)
      img_result = cv2.cvtColor(imgbgr, cv2.COLOR_BGR2RGB)
    img_result = cv2.resize(img_result, None, fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
    return img_result

def showInRow(list_of_images, titles = None, disable_ticks = False):
  count = len(list_of_images)
  for idx in range(count):
    subplot = plt.subplot(1, count, idx+1)
    if titles is not None:
      subplot.set_title(titles[idx])
      
    img = list_of_images[idx]
    cmap = 'gray' if (len(img.shape) == 2 or img.shape[2] == 1) else None
    subplot.imshow(img, cmap=cmap)
    if disable_ticks:
      plt.xticks([]), plt.yticks([])
  plt.show()

# function for colors arrat generation
def generate_colors(num):
  r = lambda: np.random.randint(0,255)
  return [(r(),r(),r()) for _ in range(num)]

# TO-DO
def resizeImage(img):
  return img


# DO NOT change these codes
# scene = cv2.imread("E:\\Python Django\\Hackathon\\object_detector\\media\\uploads\\backgrounds\\scene.jpg")
# scene = cv2.cvtColor(scene, cv2.COLOR_BGR2RGB)
# object = cv2.imread("E:\\Python Django\\Hackathon\\object_detector\\media\\uploads\\objects\\object.jpg")
# object = cv2.cvtColor(object, cv2.COLOR_BGR2RGB)

# if object.size > scene.size:
#   object = resizeImage(object)

def detect(scene, object):

  # scene = cv2.imread(scene_url)
  scene = cv2.cvtColor(scene, cv2.COLOR_BGR2RGB)
  # object = cv2.imread(object_url)
  object = cv2.cvtColor(object, cv2.COLOR_BGR2RGB)

  # rotating the image and displaying it
  # rotated = imutils.rotate_bound(scene, -33)
  rotated = scene
  # showInRow([rotated])



  #@title Template matching { run: "auto" }
  
  # different template matching methods
  methods = {'TM_CCOEFF':cv2.TM_CCOEFF, 'TM_CCOEFF_NORMED':cv2.TM_CCOEFF_NORMED, 
             'TM_CCORR':cv2.TM_CCORR, 'TM_CCORR_NORMED':cv2.TM_CCORR_NORMED, 
             'TM_SQDIFF': cv2.TM_SQDIFF, 'TM_SQDIFF_NORMED':cv2.TM_SQDIFF_NORMED}

  # interactive interface
  method = "TM_CCOEFF" #@param ["TM_CCOEFF", "TM_CCOEFF_NORMED", "TM_CCORR", "TM_CCORR_NORMED", "TM_SQDIFF", "TM_SQDIFF_NORMED"]

  # initialising template and canvas for final image
  img_template = object
  img_detected = rotated.copy()

  # getting height and width 
  h, w, c = img_template.shape

  # using the matchTemplate function
  res = cv2.matchTemplate(rotated,img_template,methods[method])

  # getting max-min values and their positions
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

  # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
  if method in ['TM_SQDIFF', 'TM_SQDIFF_NORMED']:
    top_left = min_loc
  else:
    top_left = max_loc
  
  bottom_right = (top_left[0] + w, top_left[1] + h)

  # drawing rectange
  cv2.rectangle(img_detected,top_left, bottom_right, (0,0,255), 2)

  cv2.imwrite('color_img.jpg', img_detected)

  # print(type(img_detected))

  # img_detected = Image.fromarray(img_detected)

  result_img = Image.fromarray(img_detected)

  return result_img
  

# scene_url = "E:\\Python Django\\Hackathon\\object_detector\\media\\uploads\\backgrounds\\scene.jpg"
# object_url = "E:\\Python Django\\Hackathon\\object_detector\\media\\uploads\\objects\\object.jpg"

# detect(scene, object)