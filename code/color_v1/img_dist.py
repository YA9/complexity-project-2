import matplotlib.pyplot as plt
import matplotlib.image as image
from skimage.draw import line
import numpy as np
import math
from PIL import Image, ImageDraw
from IPython.display import display


def make_circle(img, n_nodes):
    # shape_y = img.shape[0]
    # shape_x = img.shape[1]
    # center_y = (shape_y // 2)
    # center_x = (shape_x // 2)
    # angle = (2 * np.pi) / n_nodes
    # radius = min(shape_x, shape_y) // 2 - 2
    # nodes_x = []
    # nodes_y = []
    # circle_x = []
    # circle_y = []

    # # creating nodes
    # for i in range(n_nodes):
    #     curr_angle = angle * i
    #     line_ = line(center_y, center_x, center_y + int(radius *
    #                  math.sin(curr_angle)), center_x + int(radius * math.cos(curr_angle)))
    #     nodes_y.append(line_[0][-1])
    #     nodes_x.append(line_[1][-1])

    # count = 0
    # while count <= len(nodes_x) - 2:
    #     line_circle = line(nodes_y[count], nodes_x[count],
    #                        nodes_y[count+1], nodes_x[count+1])
    #     # np.concatenate(circle_y, line_circle[0])
    #     # np.concatenate(circle_x, line_circle[1])
    #     circle_y += list(line_circle[0])[:-1]
    #     circle_x += list(line_circle[1])[:-1]
    #     # print(circle_x)
    #     # print(circle_y)
    #     # print(line_circle[-1])
    #     # if count == 1:
    #     #     break
    #     count += 1
    # circle_x.append(circle_x[0])
    # circle_y.append(circle_y[0])
        
    # circle_x = np.array(circle_x)
    # circle_y = np.array(circle_y)
    # print(len(circle_x))
    # # for idx_row, row in enumerate(img):
    # #     for idx_col, col in enumerate(row):
    # #         if (sum(idx_col > circle_x) >= 1) and (sum(idx_row > circle_y) >= 1):
    # #             img[idx_row][idx_col] = np.array([255,255,255])
    # #     print(idx_row)
    # for idx_col reversed(range(len(circle_x))):
    #     for row in zip

    # plt.plot(circle_x, circle_y)
    # plt.imshow(img, alpha=1)
    
    img=Image.open(img)
    # display(img)
    
    height,width = img.size
    lum_img = Image.new('L', [height,width] , 0)
    
    draw = ImageDraw.Draw(lum_img)
    draw.pieslice([(0,0), (height,width)], 0, 360, 
                fill = 255, outline = "white")
    img_arr =np.array(img)
    lum_img_arr =np.array(lum_img)
    # display(Image.fromarray(lum_img_arr))
    final_img_arr = np.dstack((img_arr,lum_img_arr))
    fig = plt.imshow(final_img_arr)
    plt.axis('off')
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    # plt.show()
    plt.savefig("test.png",bbox_inches="tight", pad_inches=0)
    # display(Image.fromarray(final_img_arr))
    


# img = image.imread("../images/me1.jpg")
# make_circle(img, 100)
# plt.show()

make_circle("../images/me1.jpg", 100)