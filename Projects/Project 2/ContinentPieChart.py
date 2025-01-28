## Adit Gautam
# 1/28/25
# CS003C Project 2
# Matplotlib with Python 
# Area of Continent pie chart

from matplotlib import pyplot

class Continent :           #Gonna do the same thing for practice.
    def __init__(self, name, area) :
        self.name = name
        self.area = area

#Initialize the objects with data
continentData = [
    Continent("Africa",  30.37),
    Continent("Antarctica", 14.00),
    Continent("Asia", 44.58),
    Continent("Europe", 10.18),
    Continent("North America", 24.71),
    Continent("Australia", 7.69),
    Continent("South America", 17.84)
]

#Separate the data so it is usable
continent_names = [data.name for data in continentData]
continent_area = [data.area for data in continentData]

#Data to plot is area,  labeled with respective names.. Autopct just rounds  to 1 point decimal
pyplot.pie(continent_area, labels = continent_names,startangle = 140, autopct='%1.1f%%')

#Formatting
pyplot.title("Pie Chart of the Areas of Continents - Adit Gautam")
pyplot.axis('equal')

pyplot.show()