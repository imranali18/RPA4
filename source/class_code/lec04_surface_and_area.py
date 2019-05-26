'''
This is a modification of the cylindrical volume and
surface area code from lecture 2 to use input 
instead of hardcoding the radius and height.

A sample run is:

What is your name? Sir Lancelot
Sir Lancelot enter the radius: 2
Sir Lancelot enter the height: 10
volume is 125.664 surface area is 150.796
'''
name = input("What is your name? ")
radius = float(input("{:s} enter the radius: ".format(name)))
height = float(input("{} enter the height: ".format(name)))
pi = 3.14159
base_area = pi * radius ** 2
volume = base_area * height
surface_area = 2 * base_area + 2 * pi * radius * height
print("volume is {:.3f} surface area is {:.3f}".format(volume,surface_area))