from tkinter import *
import math 

root = Tk()

width = 300
height = 300

def triangleArea(side1, side2, side3):
    # Area of Triangle 
    print("Area of Triangle")

def drawTriangle(height, width):
    # Draw Triangle
    print("Draw Triangle")
    canvas = Canvas(root, width=width, height=height)
    canvas.create_rectangle(0, 0, 100, 100, fill="blue", outline="blue")
    canvas.create_rectangle(50, 50, 100, 100, fill="red", outline="blue")
    canvas.
    canvas.pack()

def generateBill(area):
    # Generate Bill
    print("Generate Bill")

side1 = 30
side2 = 40
side3 = 60
drawTriangle(height, width)

# area = triangleArea(side1, side2, side3)
# print(generateBill(area))

root.mainloop()
