# A Color Extension to a String Art Algorithm

### Author: Yehya Albakri

#

## Abstract

This paper will investigate algorithms that are used to form string art. String art is a technique used to recreate an image by stretching a thread across pins on a canvas. This is usually done with a single thread. The challenge is optimizing the image such that minimal noise and visual artifacts are created while allowing the important features of the image to emerge.
<br>
<br>
![Examples](../images/sample_art.PNG)
above is an example representing images and their conversions to string art. [[1]](#link1)

There are many ways to optimize the placement of the strings, however, the most common one that will likely be used in this paper is an iterative greedy algorithm. This method starts at a random pin and chooses the darkest path in the image to follow and places a string, then moves to the end of the string.

Although such an algorithm is fascinating and the outcome resembles the provided image, allowing the algorithm to process colored images into a set of usable colored strings would have multiple benefits. The first benefit would be novelty and different aesthetic. The second is more retention of detail, at least in theory. Higher retention of detail would come from the fact that we can now overlay strings with different colors and hide their artifacts while simultaneously adding detail in that new color. There would be multiple ways to implement this idea which will be discussed in this paper, however, only one will be implemented and thoroughly examined.

The approach to recreating the original implementation should be fairly straight-forward. However, there are multiple challenges that arise from attempting a color implementation. They can be summarized into selecting the colors for the string(s), deciding how a greedy algorithm can be modified to work in a color image, and how the loss function will work. These modifications increase the complexity of the algorithm; there will be more parameters, and parameter tuning may become a more crucial in attaining desirable results.

The outcome of the extension was successful (qualitatively judging) in transferring more information from the image to the art piece. It appears that the image has more depth and is separated into layers, each containing a different prominent color. At first glance, it is much easier to connect the resulting image to the original than the black and white version. However, the benefits do come with their vices in this case. There are some images where it is difficult for there to be a separation of colors using strings. An example of this is spots or any complex pattern. It seems to work best if the image appears to be divided into colors that are layered on top of each other.

## Annotated Bibliography

### **String art: towards computational fabrication of string images**

Birsak, Michael; Rist, Florian; Wonka, Peter; Musialski, Przemyslaw

This paper examines the concept of recreating an image in the form of string art. The approach they use is similar to an agent-based model, where there are nodes, aligned equidistantly in a circle. The string (the agent) starts at a random node and iteratively makes the decision to go in the direction of the darkest path. After a number of iterations, resemblance to the original image starts to emerge. However, within this one problem they solve, they encounter other problems they need to solve. The first one is defining a frame of nodes that will contain the new image. The nodes need to correspond to pixel positions on the reference image. The second one is sampling pixels from under a line, as mentioned earlier. The third one is eliminating visual artifacts which may emerge patterns of intersecting lines. In conclusion, their approach was successful in forming string art that has a strong resemblance to the reference image. They also found that the method works on some images better than others. For example, if there is a face with high contrast between light areas and dark spots, some visual artifacts emerge.

## Experiment

This experiment intends to recreate a common string art algorithm that uses a greedy algorithm to iteratively decide which direction the string should take next. The extension this paper will pursue is applying that iterative algorithm in color. The experiment will be discussed in the following manner: the "replication" will be explained, then the extension will be explained in the context of the replication. As a note, the replication does not use any code from the papers referenced. The algorithm for the replication was implemented based on an understanding of the descriptions from the sources, so there may be some unaccounted discrepancies.

The replication takes in the following parameters: url, n_nodes, n_strings, and width.

- url refers to the link to the local image to be used for the algorithm.
- n_nodes refers to the number of "nails" that the string would be wrapping around if they were on a canvas.
- n_strings refers to the number of times the single thread of string will wrap around a nail (total sum for all nails on the canvas).
- width refers to the width of the string that is used. The value is unitless as it sets the width of a line plotted using the Matplotlib Python Library, however, the width is very relevant in translating the computer generated sequence of attachments to a real canvas. The conversion between this value and the actual width of a string to be used is unknown.

It starts by organizing n_nodes number of nodes uniformly in a circle. It provides each node with a set of coordinates that correspond to its location on the input image.

<!-- "images/popeye.jpg", n_nodes=350, n_strings=2500, width=0.035
there are multiple extensions that can be explored in the process. The extension will be chosen depending on the difficulty of replication of the original algorithm. An idea for an extension on the easier end would be to see if changing the color of the thread would have an effect on feature retention on the image. An extension on the more difficult end would be to attempt to implement a similar algorithm, but allow it to run with multiple colors simultaneously. There are multiple ways of approaching the latter. The first is dividing the image into its three RGB channels, and running an independent string for all three colors and either run all three colors simultaneously or stack the three RGB thread images on top of each other. Another method is selecting the prominent colors in the image and layering them by prominence, with each color running on a channel filtered by the color. -->

## Results

The results will mainly look like input images and output images, attempted with multiple parameters of node and iteration lengths. Other results can include modifications to improve potential visual artifacts that may emerge.

## Causes for Concern

My main concern is that since replication will be the most difficult step, I may have to aim for the easier end of the extension. My worry about this is that I may not get insightful results. However, I believe that my theory about changing the color of the string (and the color extracted from the image) may have an interesting effect on the features extracted by the algorithm. My other concern is that I may have a difficult time converting a continuous line between two points into discrete pixels. I have an idea for the direction to take this, but no solid plan on what I will be doing.

## Next Steps

The next step is figuring out a way to quantitatively measure the distance between two images. The goal here is to see what the distance between a black and white string art image and the original is versus the distance between a colored string art image and the original.

<!-- What I can start working on is creating the object that contains the ring of equidistant nodes. Afterwards, I will overlay it on the image, and assign coordinates to each node. This will form the framework on which the rest of the algorithm will run. My challenge after this is converting the pixels along the line between any two nodes into coordinates. Then I will have access to these pixels and will be able to form my own selection method for which path the string will take at each node. Achieving these steps will be my goal for the first week. -->

## References

<a name="link1">[[1] Birsak, Michael; Rist, Florian; Wonka, Peter; Musialski, Przemyslaw. 22 May 2018. String Art: Towards Computational Fabrication of String Images.](https://repository.kaust.edu.sa/bitstream/10754/656489/1/2018.EG.Birsak.StringArt.pdf)</a>

Notes:
extension randomize or different nail pattern
