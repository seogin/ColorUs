import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from itertools import compress

class DominantColors:

    CLUSTERS = None
    IMAGE = None
    COLORS = None
    LABELS = None

    def __init__(self, image, clusters=1):
        self.CLUSTERS = clusters
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.IMAGE = img.reshape((img.shape[0] * img.shape[1], 3))

        # using k-means to cluster pixels
        kmeans = KMeans(n_clusters=self.CLUSTERS)
        kmeans.fit(self.IMAGE)

        # the cluster centers are our dominant colors.
        self.COLORS = kmeans.cluster_centers_
        self.LABELS = kmeans.labels_

    # Return a list in order of color that appeared most often.
    def getHistogram(self):
        numLabels = np.arange(0, self.CLUSTERS + 1)
        # create frequency count tables
        (hist, _) = np.histogram(self.LABELS, bins=numLabels)
        hist = hist.astype("float")
        hist /= hist.sum()

        colors = self.COLORS
        # descending order sorting as per frequency count
        colors = colors[(-hist).argsort()]
        hist = hist[(-hist).argsort()]
        for i in range(self.CLUSTERS):
            colors[i] = colors[i].astype(int)
        # Blue mask 제거
        fil = [colors[i][2] < 250 and colors[i][0] > 10 for i in range(self.CLUSTERS)]
        colors = list(compress(colors, fil))
        return colors, hist

    def plotHistogram(self):
        colors, hist = self.getHistogram()
        # creating empty chart
        chart = np.zeros((50, 500, 3), np.uint8)
        start = 0

        # creating color rectangles
        for i in range(len(colors)):
            end = start + hist[i] * 500
            r, g, b = colors[i]
            # using cv2.rectangle to plot colors
            cv2.rectangle(chart, (int(start), 0), (int(end), 50), (r, g, b), -1)
            start = end

        # display chart
        plt.figure()
        plt.axis("off")
        plt.imshow(chart)
        plt.show()

        return colors

def extract_color_features(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h_channel = hsv_image[:, :, 0]
    s_channel = hsv_image[:, :, 1]
    v_channel = hsv_image[:, :, 2]
    h_mean = np.mean(h_channel)
    v_s = np.mean((v_channel + s_channel) / 2)
    return h_mean, v_s
