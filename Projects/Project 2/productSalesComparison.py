## Adit Gautam
# 1/28/25
# CS003C Project 2
# Matplotlib with Python 
# Sales Line Graphs

from matplotlib import pyplot
#This may cost my grade but I want to do this with classes. It seems more intuitive

class ProductSales:
    #CONSTRUCTOR
    def __init__(self, month, a_sales, b_sales) :
        self.month = month                          #Basically using an initianlization list
        self.a_sales = a_sales                      #"My A SALES DATA will be assigned to the A SALES given in constructor"
        self.b_sales = b_sales

#Initialize the Objects for out Data
product_sales_list = [
    ProductSales("January", 200, 250),
    ProductSales("February", 300, 350),
    ProductSales("March", 400, 300),
    ProductSales("April", 500, 450),
    ProductSales("May", 600, 550),
    ProductSales("June", 700, 650)
]
#Now all of our data is consolidated and encapsulated together. This avoids indexing issues

#extract into new lists - this is made much easier with our class

months_list = [data.month for data in product_sales_list]           #For each piece of data in the list, append to the new list.
a_sales_list = [data.a_sales for data in product_sales_list]
b_sales_list = [data.b_sales for data in product_sales_list]

#Create the graph

pyplot.plot(months_list, a_sales_list, color = "red", label ="Product A Sales", marker = 'o')       #Label method lets us label our lines
pyplot.plot(months_list, b_sales_list, color = "blue", label = "Product B Sales", marker = 'o')     #Marker adds the little dots 

#Formatting
pyplot.title("Sales Comparison of Product A and Product  B")
pyplot.xlabel("Months")
pyplot.ylabel("Sales")
pyplot.ylim(0,800)                                              #Ensure Y values stay in range

pyplot.legend()
pyplot.grid(True)

pyplot.show()