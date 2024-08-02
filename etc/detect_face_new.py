import cv2
import dlib
import numpy as np
from imutils import face_utils

class DetectFace:
    def __init__(self, image_path):
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor("personal_color/shape_predictor_68_face_landmarks.dat")

        self.img = cv2.imread(image_path)
        if self.img is None:
            print(f"Warning: Unable to load image {image_path}")
            return

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

        self.detect_face_parts()

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

    def get_cheek_regions(self):
        return self.right_cheek, self.left_cheek

    def detect_face_parts(self):
        try:
            rect = self.detector(cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY), 1)[0]
        except IndexError:
            print("No face detected")
            return

        shape = self.predictor(cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY), rect)
        shape = face_utils.shape_to_np(shape)

        self.mouth = self.extract_face_part(shape[48:68])
        self.right_eyebrow = self.extract_face_part(shape[17:22])
        self.left_eyebrow = self.extract_face_part(shape[22:27])
        self.right_eye = self.extract_face_part(shape[36:42])
        self.left_eye = self.extract_face_part(shape[42:48])
        self.nose = self.extract_face_part(shape[27:36])
        self.left_cheek = self.img[shape[29][1]:shape[33][1], shape[4][0]:shape[48][0]]
        self.right_cheek = self.img[shape[29][1]:shape[33][1], shape[54][0]:shape[12][0]]

    def extract_face_part(self, face_part_points):
        (x, y, w, h) = cv2.boundingRect(face_part_points)
        crop = self.img[y:y + h, x:x + w]
        adj_points = np.array([np.array([p[0] - x, p[1] - y]) for p in face_part_points])

        # Create a mask
        mask = np.zeros((crop.shape[0], crop.shape[1]), dtype=np.uint8)
        cv2.fillConvexPoly(mask, adj_points, 1)
        mask = mask.astype(bool)
        crop[np.logical_not(mask)] = [255, 0, 0]

        return crop

def main():
    df = DetectFace("src/fall/1.jpg")
    right_cheek, left_cheek = df.get_cheek_regions()
    if right_cheek is not None:
        cv2.imshow("Right Cheek", right_cheek)
        cv2.waitKey(0)
    if left_cheek is not None:
        cv2.imshow("Left Cheek", left_cheek)
        cv2.waitKey(0)

if __name__ == "__main__":
    main()
