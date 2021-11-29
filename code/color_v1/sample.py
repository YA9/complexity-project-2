from PIL import Image
import cv2
import matplotlib.pyplot as plt
import colour
import numpy as np
import matplotlib.image as image
from extract_main_colors import remove_color_from_image, prominent_colors

# plt.plot((0, 1), (0, 1), c='orange', linewidth=20)
plt.plot((0, 1), (0, 1), c="blue", linewidth=20)
# plt.show()

# image1_rgb = cv2.imread('image1.jpeg')
# image2_rgb = cv2.imread('image2.jpeg')

# image1_lab = cv2.cvtColor(image1_rgb, cv2.COLOR_RGB2Lab)
# image2_lab = cv2.cvtColor(image2_rgb, cv2.COLOR_RGB2Lab)
# delta_E = colour.delta_E(image1_lab, image2_lab)
# delta_E = colour.delta_E([[111, 111, 111], [222, 222, 222]], [
#                          [333, 222, 222], [333, 222, 222]])
# print(delta_E)
# print(np.multiply(np.array([[1, 2, 3]]), 3))
# print(range(5) + range(8))
# n_nodes = 100
# curr_node = 20
# # print(list(range((curr_node-10) % n_nodes)) +
# #       list(range((curr_node+10) % n_nodes, n_nodes)))
# # print(list(range(n_nodes))[:curr_node-10]+list(range(n_nodes))[curr_node+10:])
# # cur_nail+1+NAILS_SKIP, cur_nail+len(nails)-NAILS_SKIP
# print(list(range(curr_node+1+10, (curr_node+n_nodes-10) * -1 % n_nodes)))

# print([[[1, 2, 3]] * 3] * 3)
# img_rgba = np.array(Image.open("../images/popeye.jpg").convert("RGBA"))
# img_rgb = image.imread("../images/popeye.jpg")
# print(base)
# img = image.imread("../images/popeye.jpg")
# remove_color_from_image(img_rgb, img_rgba, [111, 123, 254])
print(prominent_colors("../images/popeye.jpg", 3))
# print(colour.delta_E([1, 2, 3, 1], [1, 3, 5, 1]))
