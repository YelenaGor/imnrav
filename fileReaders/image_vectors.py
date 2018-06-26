## Import block
import os

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import pandas as pd

## Directories, locations, etc
imgDir = r"D:\Art\jpg"

## grab the image locations
images = [os.path.abspath(os.path.join(imgDir, x)) for x in os.listdir(imgDir)]

print(images[0])

img = mpimg.imread(images[0])
imgplot = plt.imshow(img)
plt.show()
