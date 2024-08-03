import cv2
import os
import numpy as np
import shutil
from detect_face_new import DetectFace
from color_extract_new import extract_color_features

# Define paths
image_dir = "images"
output_dir = "ab"
no_face_dir = "no_face"

# Create output directories
for season in ["spring", "summer", "fall", "winter"]:
    os.makedirs(os.path.join(output_dir, season), exist_ok=True)
os.makedirs(no_face_dir, exist_ok=True)


def load_images(image_dir):
    images = []
    labels = []
    original_labels = []
    for root, _, files in os.walk(image_dir):
        for filename in files:
            if filename.endswith(".jpg") or filename.endswith(".png"):
                filepath = os.path.join(root, filename)
                image = cv2.imread(filepath)
                if image is not None:
                    images.append(image)
                    labels.append(filepath)
                    original_label = os.path.basename(root)
                    original_labels.append(original_label)
                else:
                    print(f"Warning: Unable to load image {filepath}")
    return images, labels, original_labels


def check_color_palette(h_mean, v_s):
    # Determine season based on H and V-S
    if h_mean is None or v_s is None:
        return None
    if 20 <= h_mean <= 210:
        if v_s >= 68.25:
            return "spring"
        else:
            return "fall"
    elif (0 <= h_mean < 20) or (210 < h_mean <= 360):
        if v_s >= 68.75:
            return "summer"
        else:
            return "winter"
    return None


def organize_images(labels, features, original_labels, output_dir, no_face_dir):
    for label, feature, original_label in zip(labels, features, original_labels):
        h_mean, v_s = feature
        predicted_season = check_color_palette(h_mean, v_s)

        if predicted_season is None:
            filename = os.path.basename(label)
            destination = os.path.join(no_face_dir, filename)
            print(f"Moving {label} to {destination} (no face detected)")
            shutil.move(label, destination)
        elif predicted_season == original_label:
            filename = os.path.basename(label)
            destination = os.path.join(output_dir, predicted_season, filename)
            print(f"Copying {label} to {destination}")
            shutil.copy(label, destination)
        else:
            print(
                f"Deleting {label} (original: {original_label}, predicted: {predicted_season})"
            )
            os.remove(label)


# Load images
images, labels, original_labels = load_images(image_dir)
print(f"Loaded {len(images)} images.")
# Extract features from cheek regions
features = []
for image_path in labels:
    df = DetectFace(image_path)
    right_cheek, left_cheek = df.get_cheek_regions()
    if right_cheek is not None and left_cheek is not None:
        if (
            isinstance(right_cheek, np.ndarray)
            and isinstance(left_cheek, np.ndarray)
            and right_cheek.size != 0
            and left_cheek.size != 0
        ):
            h_mean_right, v_s_right = extract_color_features(right_cheek)
            h_mean_left, v_s_left = extract_color_features(left_cheek)
            h_mean = (h_mean_right + h_mean_left) / 2
            v_s = (v_s_right + v_s_left) / 2
            features.append([h_mean, v_s])
        else:
            print(f"Invalid cheek regions for image {image_path}")
            features.append([None, None])
    else:
        print(f"No face detected for image {image_path}")
        features.append([None, None])

# Organize images
organize_images(labels, features, original_labels, output_dir, no_face_dir)
