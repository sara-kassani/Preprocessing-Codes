from scipy.misc import imread, imsave        
import util.dirhandler
import cv2
import sys

def canny_opencv(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 100, 300)

    return canny
    # img = cv2.medianBlur(img, kernal)
    # return img


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
    image = canny_opencv(image)

    imsave('data/processed-data/canny/' + file_name, image)
