pi = 3.14159
radius = input("Radius: ")
radius =  float(radius)
height = input("Height: ")
height = float(height)
base_area = pi * radius ** 2
number = 7
volume = base_area * height * number
surface_area = 2 * base_area + 2 * pi * radius * height
print("volume is", volume, ", surface area is", surface_area)
