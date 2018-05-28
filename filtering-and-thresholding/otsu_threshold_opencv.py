from scipy.misc import imread, imsave
import util.dirhandler
import cv2
import sys

def otsu_threshold_opencv(img):
    #convert to grayscale
    img = cv2.cvtColor( img, cv2.COLOR_RGB2GRAY )
    ret, th = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return th


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
    image = otsu_threshold_opencv(image)

    imsave('data/processed-data/otsu/opencv/' + file_name, image)
