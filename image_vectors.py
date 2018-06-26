## Import block
import pandas as pd
import os

## Directories, locations, etc
imgDir = r"D:\Art\jpg"

## grab the image locations
images = os.listdir(imgDir)

print(images[0])