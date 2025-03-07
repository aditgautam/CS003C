## Adit Gautam
# 1/28/25
# CS003C Project 3
# Graphics with ezgraphics
# Task 2

##
#  This program creates a new flipped version of a GIF image.
#
import os
from ezgraphics import GraphicsImage

filename = input("Enter the name of the image file: ")
if not os.path.exists(filename):
    print(f"❌ ERROR: File '{filename}' not found in {os.getcwd()}!")
    exit()

# Load the original image.
origImage = GraphicsImage(filename)

# Create an empty image that will contain the new flipped image.
width = origImage.width()
height = origImage.height()
newImage = GraphicsImage(width, height)

# Iterate over the image and copy the pixels to the new image to 
# produce the flipped image.
newRow = height - 1
for row in range(height) :
   for col in range(width) :
      newCol = col
      pixel = origImage.getPixel(row, col)
      newImage.setPixel(newRow, newCol, pixel)
   newRow = newRow - 1
    
# Save the new image with a new name.
newImage.save("flipped-" + filename)