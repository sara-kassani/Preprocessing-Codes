import numpy as np           
from scipy import ndimage, misc
import sys
import skimage
from skimage import feature, data, io
from skimage.morphology import disk
from scipy.misc import imread, imsave
import util.dirhandler
try:
    from skimage import filters
except ImportError:
    from skimage import filter as filters

# http://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python
def to_gray(img):
    if len(img.shape) == 2 or img.shape[2] == 1:
        #Already gray
        return img
    r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]

    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray


def roberts_skimage(img):
    img = to_gray(img)
    img = img.astype(np.uint8)
    edges=filters.roberts(img)

    return edges

"""
Get name images to preprocessing
--------------------------------
"""
input_path = 'data/train/'
input_extension = 'jpg'

inputs_files = sorted(util.dirhandler.get_file_name_dir(input_path, input_extension))

print('*************************************************************')
print('********************* Preprocessing *************************')
print('*************************************************************')

"""
Iterate over the list of images
-------------------------------
"""
cont = 1

for file_name in inputs_files:
    print('Preprocessing: ' + file_name + ': ' + str(cont))
    cont += 1
    # Get the image
    image = imread(input_path + file_name)

    print('\tfiltering...')
    # Median filter
    image = roberts_skimage(image)

    imsave('data/processed-data/roberts/' + file_name, image)
