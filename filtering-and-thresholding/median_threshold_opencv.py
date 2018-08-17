from scipy.misc import imread, imsave            
import util.dirhandler
import cv2
import sys

def median_opencv(img, kernal=3):
    img = cv2.medianBlur(img, kernal)
    return img


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
    image = median_opencv(image)

    imsave('data/processed-data/median/opencv/' + file_name, image)
