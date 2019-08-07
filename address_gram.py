# -*- coding: utf-8 -*-

import os
from PIL import Image, ImageFont, ImageDraw
import sys
import random


root = './repeat_grams'
if not os.path.exists(root):
    os.mkdir(root)


# seed = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-'
# chars = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-,        '  # adding space to randomize spacing
chars = '000'  # adding space to randomize spacing
font_list_names = ['arial.ttf', 'vera.ttf', 'arialbold.ttf', 'arialitalic.ttf']
# font_names = ['arial']
# font_names = ['arial', 'vera', 'arialbold', 'arialitalic']
font_names = ['arial']

# store font file name in a dictionary, key=font_name, value=font_filename
font_filename = {}

for index, font_name in enumerate(font_names):
    font_filename[font_name] = font_list_names[index]


num_samples = 2000  # num of address grams to make

width = 224
height = 224
factor = 1  # select a scaling factor for sizing the image/letters

line_length = 12
font_size = 20

for font in font_names:

    img_index = 0  # reset for each font

    # create a new font dir for images
    root = './repeat_grams/{}'.format(font)
    if not os.path.exists(root):
        os.mkdir(root)

    for num in range(num_samples):

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
        draw_object.text((40, 80), first_line, font=font_obj, fill="#000000")
        draw_object.text((40, 110), second_line, font=font_obj, fill="#000000")

        img_index += 1  # increment img index

        # add padding to name and same path name
        img_name = '{}_{}.png'.format(font, str(img_index).zfill(3))

        # save image
        img_path = os.path.join(root, img_name)

        im.save(img_path)




