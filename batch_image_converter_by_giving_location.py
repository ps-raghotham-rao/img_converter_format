# By giving the location of the directory. It recursively goes through all the images and without saving converts it into jpeg format from tif format. 
# An OpenCV compatible numpy array is returned (dataset).

import glob
from typing import Iterator
from PIL import Image
from io import BytesIO
import cv2
import numpy as np

def image_converter(img_dir):
    list_of_tif_images_path = glob.glob(img_dir+"\*.tif")
    ls=[]
    resulting_list_array=[]
    # adding backslash to the file path. As raw string does not allow direct '\' adding at the end. So, import os can be used or directly we can append.
    for tif_img_loc in list_of_tif_images_path:
        img_object = Image.open(tif_img_loc)
        with BytesIO() as f:
            img_object.save(f, format="JPEG")

            # Change file handle again.
            f.seek(0)
            
            ima_jpg = Image.open(f)

            pil_image = ima_jpg.convert('RGB')

        open_cv_image = np.array(pil_image) 

        # To Convert RGB to BGR 
        open_cv_image = open_cv_image[:, :, ::-1].copy() 

        # For testing that it correctly outputs in jpeg format.
        # cv2.imwrite('helo.jpeg',open_cv_image)
        # cv2.waitKey()

        
        # For testing that it correctly outputs in jpeg format.
        # cv2.imshow("image",open_cv_image)
        # cv2.waitKey()
        
        # print(type(open_cv_image))
        # print(open_cv_image)
        resulting_list_array.append(open_cv_image)
    resulting_numpy_array=np.asarray(resulting_list_array)
    return resulting_numpy_array

img_dir = r'C:\Users\raghotham\Music'
# print(img_object)
resulting_numpy_array=image_converter(img_dir)
print(resulting_numpy_array)
        
