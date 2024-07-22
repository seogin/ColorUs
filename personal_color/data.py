import cv2
import csv
import numpy as np
from sklearn.cluster import KMeans
from sklearn import svm
from os import walk
from detect_face import DetectFace
from color_extract import DominantColors
from color_converter import rgb2lab
from colorsys import rgb_to_hsv


def get_data():

    files = []
    for _, dirname, filenames in walk("src"):
        files.extend(dirname)
        break
    # print(files)

    # create csv file
    with open("data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "b1",
                "s1",
                "b2",
                "s2",
                "label",
            ]
        )

        for file in files:
            images = []
            for _, dirname, filenames in walk(f"src/{file}"):
                images.extend(filenames)
                break
            for image in images:
                if image == ".DS_Store":
                    continue
                face = DetectFace((f"src/{file}/{image}")).get_face()
                if len(face) > 0:
                    colors, _ = DominantColors(face).getHistogram()
                    data = []
                    for color in colors:
                        lab = rgb2lab(color)
                        hsv = rgb_to_hsv(*color)
                        # data.append(lab[1] / 128)
                        data.append(lab[2] / 128)
                        data.append(((hsv[1] * 255) - 128) / 255)
                        # data.append((hsv[2] - 128) / 255)
                        # print(data)
                    if len(data) == 4:
                        data.append(file)
                        print(len(data))
                        writer.writerow(data)
                    else:
                        print("no data")

                # parts = DetectFace((f"../src/{file}/{image}")).get_face_parts()
                # color_number = []
                # for part in parts:
                #     if len(part) > 0:
                #         colors = DominantColors(part)
                #         # colors.plotHistogram()
                #         color, hist = colors.getHistogram()
                #         while len(color) < 1:
                #             color.append([-1, -1, -1])
                #         # if len(color) == 0:
                #         #     color_number = []
                #         #     break
                #         color_number.extend(color[0])
                #         # print(color)
                # if len(color_number) > 0:
                #     print(len(color_number))
                #     color_number.append(file)
                #     writer.writerow(color_number)

    # for file in files:
    #     images = []
    #     for (dirpath, dirname, filenames) in walk(f"../src/{file}"):
    #         images.extend(filenames)
    #         break
    #     # print(images)
    #     for image in images:
    #         parts = DetectFace((f"../src/{file}/{image}")).get_face_parts()
    #         for part in parts:
    #             if len(part) > 0:
    #                 colors = DominantColors(part)
    #                 # colors.plotHistogram()
    #                 colors, hist = colors.getHistogram()
    #                 print(colors, hist)


if __name__ == "__main__":
    get_data()
