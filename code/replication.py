from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as image
from skimage.draw import line
import math
import random

random.seed(10)

# img = image.imread("images/mona-lisa.jpg")
# print(img.shape)
# plt.imshow(img)
# plt.show()

img2 = Image.open("images/mona-lisa.jpg")
# img2.show()
draw = ImageDraw.Draw(img2)
draw.line((100, 200, 150, 300), fill=128)
# img2.show()
newline = line(50, 75, 100, 100)
# print(newline)
# plt.plot(newline[0], newline[1])
# plt.show()


class node():
    def __init__(self, x, y):
        self.x = x
        self.y = y


def pixel_pos_to_pixel_values(input_positions, img):
    ys = input_positions[0]
    xs = input_positions[1]
    result = []

    # img = image.imread(url)
    for y, x in zip(ys, xs):
        val = img[y][x]
        # img[y][x] = np.array([255, 255, 255])
        # Converting rgb color to grayscale
        grayscale_val = (np.dot(val, [0.2989, 0.5870, 0.1140]))
        result.append(grayscale_val)
    # return img, result
    return result


def pixel_pos_to_draw(input_positions, img):
    ys = input_positions[0]
    xs = input_positions[1]

    for y, x in zip(ys, xs):
        img[y][x] = np.array([255, 255, 255])


class stringArt():
    def __init__(self, url, n_nodes=100, n_strings=10, width=0.1):
        self.nodes_y = []
        self.nodes_x = []
        self.string_attachments = []
        self.url = url
        self.img = image.imread(url)
        self.n_nodes = n_nodes
        self.n_strings = n_strings
        self.width = width
        self.mean_darkness_list = []

    def create_nodes(self):
        img = image.imread(self.url)
        self.shape_y = img.shape[0]
        self.shape_x = img.shape[1]
        self.shape_z = img.shape[2]
        self.center_y = (self.shape_y // 2)
        self.center_x = (self.shape_x // 2)
        self.radius = min(self.shape_x, self.shape_y) // 2 - 2
        angle = (2 * np.pi) / self.n_nodes
        for i in range(self.n_nodes):
            curr_angle = angle * i
            # line_ = line(self.center_y, self.center_x, self.radius + int(self.radius *
            #              math.sin(curr_angle)), self.radius + int(self.radius * math.cos(curr_angle)))
            line_ = line(self.center_y, self.center_x, self.center_y + int(self.radius *
                         math.sin(curr_angle)), self.center_x + int(self.radius * math.cos(curr_angle)))
            # self.nodes.append(node(line[0][-1], line[1][-1]))
            self.nodes_y.append(line_[0][-1])
            self.nodes_x.append(line_[1][-1])
        # plt.imshow(img)
        # plt.scatter(self.nodes_x, self.nodes_y, s=20)
        # plt.show()

    def optimize_strings(self):
        curr_node = random.randrange(0, self.n_nodes)
        self.string_attachments.append(curr_node)
        for i in range(self.n_strings):
            # print(i)
            max_darkness = 255
            max_darkness_node = 0
            max_darkness_line = 0
            for test_node in range(self.n_nodes):
                line_ = line(self.nodes_y[curr_node], self.nodes_x[curr_node],
                             self.nodes_y[test_node], self.nodes_x[test_node])

                pixel_vals = pixel_pos_to_pixel_values(
                    line_, self.img)
                mean_pixel_val = np.mean(pixel_vals)
                if mean_pixel_val < max_darkness:
                    max_darkness = mean_pixel_val
                    max_darkness_node = test_node
                    max_darkness_line = line_
            self.mean_darkness_list.append(max_darkness)
            print(i, max_darkness)
            pixel_pos_to_draw(max_darkness_line, self.img)

            self.string_attachments.append(max_darkness_node)
            curr_node = max_darkness_node
        # plt.imshow(self.img, alpha=0.2)
        # plt.imshow(self.img, alpha=1)

    def draw_string_art(self):
        image = np.zeros((self.radius * 2, self.radius * 2))
        curr_node = self.string_attachments[0]
        for i in range(1, self.n_strings):
            target_node = self.string_attachments[i]
            line_ = line(self.nodes_y[curr_node], self.nodes_x[curr_node],
                         self.nodes_y[target_node], self.nodes_x[target_node])
            plt.plot((line_[1][0], line_[1][-1]),
                     (line_[0][0], line_[0][-1]), c="black", linewidth=self.width)
            # pixel_pos_to_draw(line_, image)

            curr_node = target_node

        plt.imshow(self.img, alpha=0)
        plt.scatter(self.nodes_x, self.nodes_y, s=20)
        plt.axis('equal')
        plt.savefig("../images/Figure_29.1.png")
        plt.figure()

        # plt.plot(image)
        plt.imshow(self.img, alpha=1)
        plt.scatter(self.nodes_x, self.nodes_y, s=20)
        plt.savefig("../images/Figure_29.2.png")
        plt.figure()

        plt.plot(self.mean_darkness_list)
        plt.savefig("../images/Figure_29.3.png")
        plt.show()


if __name__ == '__main__':
    # art = stringArt("images/mona-lisa.jpg", n_nodes=300,
    #                 n_strings=2500, width=0.1)
    # art = stringArt("images/tiffany.jpg", n_nodes=250,
    #                 n_strings=2500, width=0.1)
    # art = stringArt("images/aysha_cropped.jpg",
    # n_nodes=50, n_strings=1600, width=0.1)
    art = stringArt("images/popeye.jpg",
                    n_nodes=350, n_strings=3000, width=0.035)
    art.create_nodes()
    art.optimize_strings()
    art.draw_string_art()
    # print(art.shape)
    # print(np.pi)
