from PIL import Image
import numpy as np

def pixel_filter(side: int, step: int):
    length, height = len(img_arr), len(img_arr[1])
    x = 0
    while x < length:
        y = 0
        while y < height:
            result = 0
            for n, m in np.nditer([np.arange(x, x + side)[:, None], np.arange(y, y + side)]):
                result += img_arr[n][m][0] / 3 + img_arr[n][m][1] / 3 + img_arr[n][m][2] / 3
            avg_brightness = int(result) // (side * side)
            pixel_coloring(avg_brightness, x, y, side, step)
            y += side
        x += side


def pixel_coloring(x, y, side, step):
    result = 0
    for n, m in np.nditer([np.arange(x, x + side)[:, None], np.arange(y, y + side)]):
        result += img_arr[n][m][0] / 3 + img_arr[n][m][1] / 3 + img_arr[n][m][2] / 3
    avg_brightness = int(result) // (side * side)
    for n in range(x, x + side):
        for m in range(y, y + side):
            img_arr[n][m][range(3)] = int(avg_brightness // step) * step

np.seterr(over='ignore')
img_arr = np.array(Image.open("img2.jpg"))
pixel_filter(int(input()), int(input()))
filtered_img = Image.fromarray(img_arr)
filtered_img.save('res.jpg')