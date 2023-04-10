# Contrast Limited Adaptive Histogram Equalization (CLAHE)

CLAHE is a contrast enhancment algorithm. It is a preprocessing technique to make tasks like image thresholding, segmentation, object detection easier. Most of the contrast enhancement techniques rely on histogram modifications that can be applied both locally or globally. CLAHE overcomes the limitations of global approaches by enhancing local contrast. 

CLAHE works on small areas of an image called tiles rather than complete image. The surrounding tiles are blended using bilinear interpolation to remove false boundaries. 

Let's see an example.

![](img/test.jpeg?raw=true)