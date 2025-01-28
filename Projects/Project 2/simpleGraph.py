## Adit Gautam
# 1/28/25
# CS003C Project 2
# Matplotlib with Python 
# Simple Bar Graph

from matplotlib import pyplot

#BAR GRAPHS, PARAMS ARE X and Y 
pyplot.bar(1, 1.1)
pyplot.bar(2, 10.0)
pyplot.bar(3, 24.5, color = "red")          #Extra parameter for color
pyplot.bar(4, 44.5)                         #Default bar width 0.8
pyplot.bar(5, 61.0)

#ALTERNATIVE VERSION WITH LISTS
#pyplot.bar([1, 2, 3, 4, 5], [1.1, 10.0, 25.4, 44.5, 61.0]) 

#WIDTH PARAMETER
pyplot.bar(6, 72.7, width = 1.0)

#LABEL AXES
pyplot.xlabel("Month")                      #X axis month
pyplot.ylabel("Temperature")

pyplot.show()