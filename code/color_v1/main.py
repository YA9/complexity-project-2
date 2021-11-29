from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as image
from skimage.draw import line
import math
import random
from extract_main_colors import prominent_colors, remove_color_from_image
import colour

random.seed(10)

# img = image.imread("images/mona-lisa.jpg")
# print(img.shape)
# plt.imshow(img)
# plt.show()

# img2 = Image.open("images/mona-lisa.jpg")
# # img2.show()
# draw = ImageDraw.Draw(img2)
# draw.line((100, 200, 150, 300), fill=128)
# # img2.show()
# newline = line(50, 75, 100, 100)
# # print(newline)
# # plt.plot(newline[0], newline[1])
# # plt.show()


def pixel_pos_to_pixel_dist(input_positions, img, input_color):
    ys = input_positions[0]
    xs = input_positions[1]
    result = []
    vals = []

    # img = remove_color_from_image(img, input_color, threshold)

    # img = image.imread(url)
    for y, x in zip(ys, xs):
        val = img[y][x]
        vals.append(val)
        # img[y][x] = np.array([255, 255, 255])
        # Converting rgb color to grayscale
        # grayscale_val = (np.dot(val, [0.2989, 0.5870, 0.1140]))
        # dist = colour.delta_E(val, input_color)
        # dist = np.sqrt(np.power(val[0] - input_color[0], 2) +
        #                np.power(val[1] - input_color[1], 2) +
        #                np.power(val[2] - input_color[2], 2))
        # result.append(dist)
    input_colors = [input_color] * len(xs)
    dist = colour.delta_E(vals, input_colors)
    # print("dist:", np.mean(dist))
    # return img, result
    return np.mean(dist)


def pixel_pos_to_draw(input_positions, img, color):
    ys = input_positions[0]
    xs = input_positions[1]

    for y, x in zip(ys, xs):
        img[y][x] = color


class stringArt():
    def __init__(self, url, i, n_nodes=100, n_strings=10, width=0.1, threshold=100):
        self.nodes_y = []
        self.nodes_x = []
        self.string_attachments = []
        self.url = url
        self.img = image.imread(url)
        self.n_nodes = n_nodes
        self.n_strings = n_strings
        self.width = width
        self.threshold = threshold
        self.mean_darkness_list = []
        self.i = i

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

    def optimize_strings(self, test_color):
        self.img = remove_color_from_image(
            self.img, test_color, self.threshold)
        inverse_color = 255 - test_color
        curr_node = random.randrange(0, self.n_nodes)
        self.string_attachments.append(curr_node)
        for i in range(self.n_strings):
            # print(i)
            max_darkness = np.inf
            max_darkness_node = 0
            max_darkness_line = 0
            for test_node in range(self.n_nodes):
                line_ = line(self.nodes_y[curr_node], self.nodes_x[curr_node],
                             self.nodes_y[test_node], self.nodes_x[test_node])

                mean_pixel_dist = pixel_pos_to_pixel_dist(
                    line_, self.img, test_color)
                if mean_pixel_dist < max_darkness:
                    max_darkness = mean_pixel_dist
                    max_darkness_node = test_node
                    max_darkness_line = line_
            self.mean_darkness_list.append(max_darkness)
            print(self.i, i)
            pixel_pos_to_draw(max_darkness_line, self.img, inverse_color)

            self.string_attachments.append(max_darkness_node)
            curr_node = max_darkness_node
        # plt.imshow(self.img, alpha=0.2)
        # plt.imshow(self.img, alpha=1)

    def draw_string_art(self, color):
        image = np.zeros((self.radius * 2, self.radius * 2))
        curr_node = self.string_attachments[0]
        for i in range(1, self.n_strings):
            target_node = self.string_attachments[i]
            line_ = line(self.nodes_y[curr_node], self.nodes_x[curr_node],
                         self.nodes_y[target_node], self.nodes_x[target_node])
            plt.plot((line_[1][0], line_[1][-1]),
                     (line_[0][0], line_[0][-1]), c=color/255, linewidth=self.width)
            # pixel_pos_to_draw(line_, image)

            curr_node = target_node

        # --------------------------------------------------
        # delete this part
        # plt.imshow(self.img, alpha=1)
        # plt.scatter(self.nodes_x, self.nodes_y, s=20)
        # plt.figure()
        # --------------------------------------------------

        plt.imshow(self.img, alpha=0)
        # plt.scatter(self.nodes_x, self.nodes_y, s=20)
        # plt.axis('equal')
        # plt.savefig("../images/Figure_30.1.png")
        # plt.figure()

        # plt.imshow(self.img, alpha=1)
        # plt.scatter(self.nodes_x, self.nodes_y, s=20)
        # plt.savefig("../images/Figure_30.2.png")
        # plt.figure()

        # plt.plot(self.mean_darkness_list)
        # plt.savefig("../images/Figure_30.3.png")
        # plt.show()


def main(url, n_nodes=350, n_strings=2500, width=0.035, n_colors=3, threshold=60):
    colors = prominent_colors(url, n_colors)
    # colors = colors[1:]
    # n_colors -= 1

    # plt.imshow(art.img, alpha=0)
    # plt.scatter(art.nodes_x, art.nodes_y, s=20)
    # plt.axis('equal')
    # art = stringArt(url, 1, n_nodes=n_nodes,
    #                 n_strings=n_strings, width=width, threshold=threshold)

    # Order is black, skin, blue
    # Order is brown, skin, black
    order = [0, 1, 2]
    # n_strings = [1000, 1500, 2500]
    # n_strings = [3, 1, 1]

    # for idx, i in enumerate(order):
    for idx, i in enumerate(reversed(range(n_colors))):
        # i = 1
        # art = stringArt(url, idx,  n_nodes=n_nodes,
        #                 n_strings=int(n_strings*colors[n_colors-1-i][0]), width=width, threshold=threshold)
        art = stringArt(url, idx,  n_nodes=n_nodes,
                        n_strings=int(n_strings*colors[i][0]), width=width, threshold=threshold)
        # art = stringArt(url, n_nodes=n_nodes,
        #                 n_strings=n_strings, width=width, threshold=threshold)
        # art = stringArt(url, idx, n_nodes=n_nodes,
        #                 n_strings=n_strings[idx], width=width, threshold=threshold)
        art.create_nodes()
        art.optimize_strings(colors[i][1])
        art.draw_string_art(colors[i][1])
        # break
    plt.savefig(f"../../images/color_figure_39.png")
    plt.show()


if __name__ == '__main__':
    # prominent_colors("../images/tuta2_cropped.jpg", 5, show=True)
    main("../images/tuta3_cropped.jpg", n_nodes=500,
         n_strings=18000, width=0.03, n_colors=5, threshold=40)
