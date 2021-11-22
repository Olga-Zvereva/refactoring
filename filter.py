from PIL import Image
import numpy as np

def pixel_filter(side: int, step: int):
    length, height = len(img_arr), len(img_arr[1])
    x = 0
    while x < length:
        y = 0
        while y < height:
            result = 0
            for x in range(x, x + side):
                for y in range(y, y + side):
                    result += sum(img_arr[x][y][range(3)] / 3)
            avg_brightness = int(result) // (side * side)
            pixel_coloring(avg_brightness, x, y, side, step)
            y += side
        x += side


def pixel_coloring(avg_brightness, x, y, side, grayscale):
    for x in range(x, x + side):
        for y in range(y, y + side):
            img_arr[x][y][range(3)] = int(avg_brightness // grayscale) * grayscale

np.seterr(over='ignore')
img_arr = np.array(Image.open("img2.jpg"))
pixel_filter(int(input()), int(input()))
filtered_img = Image.fromarray(img_arr)
filtered_img.save('res.jpg')