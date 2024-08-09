from imutils import face_utils
import numpy as np
import dlib
import cv2
import urllib
import os


def url_to_image(image_path_or_url):
    # Check if the input is a URL or a file path
    if os.path.isfile(image_path_or_url):
        # If it's a file path, read the image using OpenCV
        image = cv2.imread(image_path_or_url)
    else:
        # If it's a URL, read the image from the URL
        resp = urllib.request.urlopen(image_path_or_url)
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    
    return image


class DetectFace:
    def __init__(self, image):
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

        # self.img = cv2.imread(image)
        self.img = url_to_image(image)
        # cv2.imshow("image", self.img)
        # cv2.waitKey(0)

        self.right_eyebrow = []
        self.left_eyebrow = []
        self.right_eye = []
        self.left_eye = []
        self.right_cheek = []
        self.left_cheek = []
        self.mouth = []
        self.nose = []
        self.jaw = []
        self.face = []

        self.detect_face()

        # self.detect_face_part()

    def get_face_parts(self):
        return (
            self.right_eyebrow,
            self.left_eyebrow,
            self.right_eye,
            self.left_eye,
            self.right_cheek,
            self.left_cheek,
            self.mouth,
            self.nose,
        )

    def get_face(self):
        return self.face

    def detect_face(self):
        try:
            rect = self.detector(cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY), 1)[0]
        except IndexError:
            print("No face detected")
            return

        shape = self.predictor(cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY), rect)
        shape = face_utils.shape_to_np(shape)

        self.face = self.img[shape[29][1] : shape[51][1], shape[37][0] : shape[46][0]]
        # self.face = cv2.cvtColor(self.face, cv2.COLOR_BGR2HSV)

        # cv2.imshow("rect", self.face)
        # cv2.waitKey(0)

    def detect_face_part(self):
        face_parts = [[], [], [], [], [], [], [], []]
        # detect faces in the grayscale image
        try:
            rect = self.detector(cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY), 1)[0]
        except IndexError:
            print("No face detected")
            return

        shape = self.predictor(cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY), rect)
        shape = face_utils.shape_to_np(shape)

        # cv2.imshow("rect", self.img)
        # cv2.waitKey(0)

        idx = 0
        # loop over the face parts individually
        for _, (i, j) in face_utils.FACIAL_LANDMARKS_IDXS.items():
            face_parts[idx] = shape[i:j]
            idx += 1
        # face_parts = face_parts[1:5]
        # set the variables
        # Caution: this coordinates fits on the RESIZED image.

        self.mouth = self.extract_face_part(face_parts[0])
        self.right_eyebrow = self.extract_face_part(face_parts[2])
        self.left_eyebrow = self.extract_face_part(face_parts[3])
        self.right_eye = self.extract_face_part(face_parts[4])
        self.left_eye = self.extract_face_part(face_parts[5])
        self.nose = self.extract_face_part(face_parts[6])
        # self.jaw = self.extract_face_part(face_parts[7])
        # Cheeks are detected by relative position to the face landmarks
        self.left_cheek = self.img[
            shape[29][1] : shape[33][1], shape[4][0] : shape[48][0]
        ]
        self.right_cheek = self.img[
            shape[29][1] : shape[33][1], shape[54][0] : shape[12][0]
        ]
        cv2.imshow("right_eyebrow", self.right_eye)
        cv2.waitKey(0)
        cv2.imshow("right_eyebrow", self.left_cheek)
        cv2.waitKey(0)
        cv2.imshow("right_eyebrow", self.right_cheek)
        cv2.waitKey(0)

    def extract_face_part(self, face_part_points):
        (x, y, w, h) = cv2.boundingRect(face_part_points)
        crop = self.img[y : y + h, x : x + w]
        adj_points = np.array(
            [np.array([p[0] - x, p[1] - y]) for p in face_part_points]
        )

        # Create an mask
        mask = np.zeros((crop.shape[0], crop.shape[1]))
        cv2.fillConvexPoly(mask, adj_points, 1)
        mask = mask.astype(bool)
        crop[np.logical_not(mask)] = [255, 0, 0]

        return crop


def main():
    DetectFace(
        "https://www.instyle.com/thmb/4kl8LIbmTL4eFZNUkYtWX2HY3Nc=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/071122-buccal-facial-lead-2000-12ca4fa1d38841239d34d467b5f0c05f.jpg"
    )
    # DetectFace("src/fall/05_jiho0621.jpg")
    # image = url_to_image("https://picsum.photos/200/300")
    # cv2.imshow("image", image)
    # cv2.waitKey(0)


if __name__ == "__main__":
    main()
