## Adit Gautam
# 1/28/25
# CS003C Project 3
# Graphics with ezgraphics
# Task 2

##
#  This program processes a digital image by creating a negative of 
#  the original.
#

from ezgraphics import GraphicsImage, GraphicsWindow
import os
print("Current working directory:", os.getcwd())

filename = input("Enter the name of the image file: ")

# Load the image from the file.
image = GraphicsImage(filename)

# Process the image.
width = image.width()
height = image.height()
for row in range(height) :
   for col in range(width) :
      # Get the current pixel color.
      red = image.getRed(row, col)
      green = image.getGreen(row, col)
      blue = image.getBlue(row, col)
    
      # Filter the pixel.
      newRed = 255 - red
      newGreen = 255 - green
      newBlue = 255 - blue

      # Set the pixel to the new color.
      image.setPixel(row, col, newRed, newGreen, newBlue)

# Display the image on screen.
win = GraphicsWindow()
canvas = win.canvas()
canvas.drawImage(image)
win.wait()
   
save_path = os.path.join(os.getcwd(), "negative-" + filename)
print("Saving image to:", save_path)

# Save the new image with a new name.
image.save("negative-" + filename)