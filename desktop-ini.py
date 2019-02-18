import os

dir = 'data/ISIC2018/train/non-melanoma/'
my_file = dir + 'desktop.ini'
if os.path.exists(my_file):
    os.remove(my_file)