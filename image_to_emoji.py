# coding: utf-8

import sys
import os

from PIL import Image, ImageDraw, ImageFont

CANVAS_SIZE = 128


def main():
    params = sys.argv
    if len(params) != 2:
        print("[使い方 例]: python {} hoge.png".format(params[0]))
        return
    filename = params[1]

    img = Image.open(filename)
    img = img.resize((int(CANVAS_SIZE * img.width / img.height), CANVAS_SIZE))
    for x in range(int(img.width / img.height) + 1):
        save_file = "{}.png".format(x)
        cropped = img.crop((x * CANVAS_SIZE, 0, (x + 1) * CANVAS_SIZE, CANVAS_SIZE))
        cropped.save(save_file)
        print(save_file)

if __name__ == '__main__':
    main()
