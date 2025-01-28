## Adit Gautam
# 1/28/25
# CS003C Project 2
# Matplotlib with Python 
# Temperature Bar Graph

from matplotlib import pyplot

#CREATE THE BARS USING LISTS
monthsList = list(range(1,13))                                                          #Creates and initializes a list within this range
temperatureList = [1.1, 10.0, 25.4, 44.5, 61.0, 71.6, 72.7, 65.9, 54.6, 31.9, 10.9, 4.8]#Square brackets ensure the list is ordered

pyplot.bar(monthsList, temperatureList)                                                 #Construct bar using list parameters

#FORMATTING
pyplot.xlabel("Months of the Year")
pyplot.ylabel("Temperature (in degrees F)")
pyplot.xticks(monthsList)                                                               #X ticks match months

#LINE FOR 32 DEGREES
pyplot.plot([0, 14], [32, 32], "--")    #PARAMETERS: [x range], [y range], whatever we are drawing (dashed  line)

pyplot.show()






