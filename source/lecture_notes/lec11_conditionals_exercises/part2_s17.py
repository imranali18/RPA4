hd = int(input("Enter Dale's height: "))
he = int(input("Enter Erin's height: "))
hs = int(input("Enter Sam's height: "))

# Sam tallest
if hs > he and hs > hd:
    print('Sam')
    if hd > he:
        # Dale, Erin
        print('Dale')
        print('Erin')
    else:
        # Erin, Dale
        print('Erin')
        print('Dale')
# Erin tallest
elif he > hs and he > hd:        
    print('Erin')
    if hd > hs:
        # Dale, Sam
        print('Dale')
        print('Sam')
    else:
        # Sam, Dale
        print('Sam')
        print('Dale')
                
# Dale tallest
else:        
    print('Dale')
    if he > hs:
        # Erin, Sam
        print('Erin')
        print('Sam')
    else:
        # Sam, Erin
        print('Sam')
        print('Erin')
