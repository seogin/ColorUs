import cv2
import csv
import numpy as np
from sklearn.cluster import KMeans
from sklearn import svm
from os import walk
from detect_face import DetectFace
from color_extract import DominantColors

def get_data():
    
    files = []
    for (dirpath, dirname, filenames) in walk("../src"):
        files.extend(dirname)
        break
    # print(files)

    # create csv file
    with open("data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["right_eyebrow_1_red", "right_eyebrow_1_green", "right_eyebrow_1_blue",
                         "left_eyebrow_1_red", "left_eyebrow_1_green", "left_eyebrow_1_blue",
                         "right_eye_1_red", "right_eye_1_green", "right_eye_1_blue",
                         "left_eye_1_red", "left_eye_1_green", "left_eye_1_blue",
                         "right_cheek_1_red", "right_cheek_1_green", "right_cheek_1_blue",
                         "left_cheek_1_red", "left_cheek_1_green", "left_cheek_1_blue",
                         "mouth_1_red", "mouth_1_green", "mouth_1_blue",
                         "nose_1_red", "nose_1_green", "nose_1_blue", "label"])

        for file in files:
            images = []
            for (dirpath, dirname, filenames) in walk(f"../src/{file}"):
                images.extend(filenames)
                break
            for image in images:
                if image == ".DS_Store":
                    continue
                parts = DetectFace((f"../src/{file}/{image}")).get_face_parts()
                color_number = []
                for part in parts:
                    if len(part) > 0:
                        colors = DominantColors(part)
                        # colors.plotHistogram()
                        color, hist = colors.getHistogram()
                        while len(color) < 1:
                            color.append([-1,-1,-1])
                        # if len(color) == 0:
                        #     color_number = []
                        #     break
                        color_number.extend(color[0])
                        # print(color)
                if len(color_number) > 0:
                    print(len(color_number))
                    color_number.append(file)
                    writer.writerow(color_number)

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