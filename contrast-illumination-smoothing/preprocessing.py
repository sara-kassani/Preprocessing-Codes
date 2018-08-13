# Import util methods
from scipy.misc import imread, imsave      
import util.dirhandler
from preprocessing.smoothing import median_filter_
from preprocessing.illumination_enhancement import shading_attenuation_method
from preprocessing.contrast_enhancement import shades_of_gray_method
import os

"""
Get name images to preprocessing
--------------------------------
"""
melanoma_path = 'train/'
melanoma_extension = 'jpg'

all_melanoma = sorted(util.dirhandler.get_file_name_dir(melanoma_path, melanoma_extension))

# Parameters
extract = 50
margin = 10
gamma = 1/2.2

print('*************************************************************')
print('********************* Preprocessing *************************')
print('*************************************************************')
print('extract: ' + str(extract) + '\tmargin: ' + str(margin) + '\tgamma: ' + str(gamma) + '\n\n')

"""
Iterate over the list of images
-------------------------------
"""
cont = 1

for img_name in all_melanoma:
    print('Preprocessing: ' + img_name + ': ' + str(cont))
    cont += 1
    # Get the image
    image = imread(melanoma_path + img_name)

    print('\tfiltering...')
    # Median filter
    image = median_filter_(image)

    print('\tweaking shadows...')
    # weak effect of nonuniform illumination or shadow
    image = shading_attenuation_method(image, extract=extract, margin=margin)

    print('\tcolor normalization...')
    # Color normalization
    image = shades_of_gray_method(image, gamma=gamma)
    imsave('preprocessed-data/' + img_name, image)
