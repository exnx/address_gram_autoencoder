# -*- coding: utf-8 -*-

import os
from PIL import Image, ImageFont, ImageDraw
import sys
import random

'''
A script to create random ID numbers for font style analysis

Format of license ID numbers:  one upper case letter, followed by 6 numbers

'''


# create a directory to store all image data
root = './address_grams'
if not os.path.exists(root):
    os.mkdir(root)


# seed = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-'
chars = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-,        '  # adding space to randomize spacing
# chars = '000'  # adding space to randomize spacing

datasets = ['train', 'val', 'test']
font_list_names = ['arial.ttf', 'vera.ttf', 'arialbold.ttf', 'arialitalic.ttf']
font_names = ['arial', 'vera', 'arialbold', 'arialitalic']
# font_names = ['arial']

# store font file name in a dictionary, key=font_name, value=font_filename
font_filename = {}

for index, font_name in enumerate(font_names):
    font_filename[font_name] = font_list_names[index]

# place number of samples per dataset type here
data_type_num_samples = {'train':4000, 'val':1000, 'test':1000}

# dimensions of ID
height = 224
width = 224
factor = 1  # select a scaling factor for sizing the image/letters

line_length = 12  # num chars in line
font_size = 25  # font size of chars

# create image samples per font
for font in font_names:

    font_path = os.path.join(root, font)

    # create font dir
    if not os.path.exists(font_path):
        os.mkdir(font_path)

    # create a train and test set
    for data_type in datasets:

        img_index = 0  # reset for each font

        # create a train/test font dir for images
        data_set_path = './address_grams/{}/{}'.format(font, data_type)

        if not os.path.exists(data_set_path):
            os.mkdir(data_set_path)

        # create the corresponding number of samples for datatype
        for num in range(data_type_num_samples[data_type]):    

            # create an image as rgb
            im = Image.new("RGB", (width * factor, height * factor), (255, 255, 255))

            # select font file and create font object
            font_obj = ImageFont.truetype(font_filename[font], font_size * factor)

            # creates a draw object for im, to allow you to write on the image
            draw_object = ImageDraw.Draw(im)

            first_line = ''
            second_line = ''

            # for number of letters in a line
            for i in range(line_length):

                #  choose a random char
                letter = random.choice(chars)
                first_line += letter

                letter = random.choice(chars)
                second_line += letter

            # draw lines at positions near center
            draw_object.text((10, 80), first_line, font=font_obj, fill="#000000")
            draw_object.text((10, 110), second_line, font=font_obj, fill="#000000")

            img_index += 1  # increment img index

            # add padding to name and same path name
            img_name = '{}_{}.png'.format(font, str(img_index).zfill(5))

            # save image
            img_path = os.path.join(data_set_path, img_name)
            im.save(img_path)




