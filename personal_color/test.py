from os import walk
from detect_face import DetectFace
from color_extract import DominantColors
from color_converter import rgb2lab
from colorsys import rgb_to_hsv
import pickle


def main():
    path = "test"

    files = []
    for _, dirname, filenames in walk(path):
        files.extend(dirname)
        break

    for file in files:
        images = []
        for _, dirname, filenames in walk(f"{path}/{file}"):
            images.extend(filenames)
            break
        for image in images:
            if image == ".DS_Store":
                continue
            face = DetectFace((f"{path}/{file}/{image}")).get_face()
            if len(face) > 0:
                colors, _ = DominantColors(face).getHistogram()
                data = []
                for color in colors:
                    lab = rgb2lab(color)
                    hsv = rgb_to_hsv(*color)

                    data.append(lab[2] / 128)
                    data.append(((hsv[1] * 255) - 128) / 255)
                    data.append((hsv[2] - 128) / 255)

                if len(data) == 3:
                    pickle_in = open("personalColor.pickle", "rb")
                    model = pickle.load(pickle_in)
                    predict = model.predict([data])
                    print(f"Actual: {file}      Prediction: {predict}")
                else:
                    print("no data")


if __name__ == "__main__":
    main()
