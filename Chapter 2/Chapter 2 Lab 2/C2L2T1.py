## Adit Gautam
# 1/27/25
# Chapter 2 Lab 2 Task 1
# A program to calculate the area of a right circular cone

from math import pi, pow, sqrt

height = float(input("Enter the height:"))
radius = float(input("Enter the radius:"))

surface_area = (pi) * (radius) *( radius + sqrt((height ** 2) + (radius **2 )))

print("The area of the cone is", surface_area)