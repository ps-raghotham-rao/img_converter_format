# By sending single image objects. You can get in return a .jpeg format numpy array which can be used for training the dataset.

import glob
from PIL import Image
from io import BytesIO
import cv2
import numpy as np

def image_converter(im):
    with BytesIO() as f:
        im.save(f, format="JPEG")

        #Change file handle again.
        f.seek(0)
        
        ima_jpg = Image.open(f)

        pil_image = ima_jpg.convert('RGB')

    open_cv_image = np.array(pil_image) 

    # To Convert RGB to BGR 
    open_cv_image = open_cv_image[:, :, ::-1].copy() 

    # cv2.imwrite('helo.jpeg',open_cv_image)
    # cv2.waitKey()

    # cv2.imshow("image",open_cv_image)
    # cv2.waitKey()
    
    # print(type(open_cv_image))
    # print(open_cv_image)
    return open_cv_image

im = Image.open(r'C:\Users\raghotham\Documents\stargan\dbz.tif')    
# print(im)

print(image_converter(im))
