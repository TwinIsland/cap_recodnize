# method based on https://github.com/will4906/CaptchaRecognition/blob/master/sipo2/README.md

import numpy as np
import PIL.Image as Image


def convert_black(image):
    width = image.shape[0]
    height = image.shape[1]

    for i in range(width-1):
        for ii in range(height-1):
            if image[i,ii] >= 150:
                image[i,ii] = 255
            else:
                image[i,ii] = 0

def remove_noise_line(image):

    width = image.shape[1]
    height = image.shape[0]
    for w in range(width):
        count = 0
        for h in range(height):
            if image[h][w] < 60:
                count += 1
            else:
                if 2 > count > 0:
                    for c in range(count):
                        image[h - c - 1][w] = 255
                count = 0

    for h in range(height):
        count = 0
        for w in range(width):
            if image[h][w] < 100:
                count += 1
            else:
                if 2 > count > 0:
                    for c in range(count):
                        image[h][w - c - 1] = 255
                count = 0
    return image


def split_letters(image):
    letters = [image[:, : 50], image[:, 50: 100], image[:, 100: 150], image[:, 150: 200]]
    return letters


def clean_photo(image_addr):
    '''

    :param image_addr: image address
    :return: [letter data]
    '''
    image = Image.open(image_addr)

    image = image.convert('L')

    image = np.asarray(image)
    image.flags.writeable = True

    convert_black(image)
    remove_noise_line(image)
    letters = split_letters(image)
    return letters

