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
        writer.writerow(["right_eyebrow_1", "right_eyebrow_2", "right_eyebrow_3",
                         "left_eyebrow_1", "left_eyebrow_2", "left_eyebrow_3",
                         "right_eye_1", "right_eye_2", "right_eye_3",
                         "left_eye_1", "left_eye_2", "left_eye_3",
                         "right_cheek_1", "right_cheek_2", "right_cheek_3",
                         "left_cheek_1", "left_cheek_2", "left_cheek_3",
                         "mouth_1", "mouth_2", "mouth_3",
                         "nose_1", "nose_2", "nose_3",
                         "jaw_1", "jaw_2", "jaw_3", "label"])

        for file in files:
            images = []
            for (dirpath, dirname, filenames) in walk(f"../src/{file}"):
                images.extend(filenames)
                break
            # print(images)
            for image in images:
                parts = DetectFace((f"../src/{file}/{image}")).get_face_parts()
                color_number = []
                for part in parts:
                    if len(part) > 0:
                        colors = DominantColors(part)
                        # colors.plotHistogram()
                        color, hist = colors.getHistogram()
                        while len(color) < 3:
                            color.append(0)
                        color_number.extend(color)
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