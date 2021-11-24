from collections import Counter
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import PIL
from sklearn.cluster import KMeans


def show_img_compar(img_1, img_2):
    f, ax = plt.subplots(1, 2, figsize=(10, 10))
    ax[0].imshow(img_1)
    ax[1].imshow(img_2)
    ax[0].axis('off')  # hide the axis
    ax[1].axis('off')
    f.tight_layout()
    plt.show()


img = cv.imread("../images/popeye.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

dim = (500, 300)
# resize image
img = cv.resize(img, dim, interpolation=cv.INTER_AREA)

# show_img_compar(img, img_2)


clt = KMeans(n_clusters=5)


def palette(clusters):
    """
    Shows color palette without percentage of each color
    """
    width = 300
    palette = np.zeros((50, width, 3), np.uint8)
    steps = width/clusters.cluster_centers_.shape[0]
    for idx, centers in enumerate(clusters.cluster_centers_):
        palette[:, int(idx*steps):(int((idx+1)*steps)), :] = centers
    return palette


# clt_1 = clt.fit(img.reshape(-1, 3))
# show_img_compar(img, palette(clt_1))

# ------------------------------------------------------


def palette_perc(k_cluster):
    """
    Shows color palette and percentage of each color
    """
    width = 300
    palette = np.zeros((50, width, 3), np.uint8)

    n_pixels = len(k_cluster.labels_)
    counter = Counter(k_cluster.labels_)  # count how many pixels per cluster
    perc = {}
    for i in counter:
        perc[i] = np.round(counter[i]/n_pixels, 2)
    perc = dict(sorted(perc.items()))

    # for logging purposes
    # print(perc)
    # print(k_cluster.cluster_centers_)
    step = 0

    # print(k_cluster.cluster_centers_)
    for idx, centers in enumerate(k_cluster.cluster_centers_):
        print(centers)
        palette[:, step:int(step + perc[idx]*width+1), :] = centers
        step += int(perc[idx]*width+1)

    # print(palette.shape)
    return palette


# clt_1 = clt.fit(img.reshape(-1, 3))
# show_img_compar(img, palette_perc(clt_1))

def prominent_colors(url, n_colors):
    img = cv.imread(url)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    dim = (500, 300)
    img = cv.resize(img, dim, interpolation=cv.INTER_AREA)

    clt = KMeans(n_clusters=n_colors)

    k_cluster = clt.fit(img.reshape(-1, 3))

    width = 300
    palette = np.zeros((50, width, 3), np.uint8)

    n_pixels = len(k_cluster.labels_)
    counter = Counter(k_cluster.labels_)  # count how many pixels per cluster
    perc = {}
    for i in counter:
        perc[i] = np.round(counter[i]/n_pixels, 2)
    perc = dict(sorted(perc.items()))

    # for logging purposes
    print(perc)
    print(k_cluster.cluster_centers_)


prominent_colors("../images/popeye.jpg", 5)
