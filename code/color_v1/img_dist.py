import matplotlib.pyplot as plt
import matplotlib.image as image
from skimage.draw import line
import numpy as np
import math
from PIL import Image, ImageDraw
from IPython.display import display
import colour


def make_circle(img, str_img):
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
    # fig.axes.get_xaxis().set_visible(False)
    # fig.axes.get_yaxis().set_visible(False)
    # plt.show()
    plt.savefig("temp.png",bbox_inches="tight", pad_inches=0)
    # display(Image.fromarray(final_img_arr))
    
    
    str_img = (image.imread(str_img)*255)[:,:,:-1].astype(int)
    img = (image.imread("temp.png")*255)[:,:,:-1].astype(int)
    print(np.mean(colour.delta_E(img, str_img)))
    
    # a = image.imread("../images/aysha_cropped.jpg")
    # # print(np.mean(colour.delta_E(a, a)))
    # print(a)
    # print(np.mean(img))
    


# img = image.imread("../images/me1.jpg")
# make_circle(img, 100)
# plt.show()

make_circle("../images/aysha_cropped.jpg", "../../reports/images/aysha_color.png")
make_circle("../images/aysha_cropped.jpg", "../../reports/images/aysha_gf1.1.png")