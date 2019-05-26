hd = int(input("Enter Dale's height: "))
print(hd)
he = int(input("Enter Erin's height: "))
print(he)
hs = int(input("Enter Sam's height: "))
print(hs)

'''
if hd > he and hd > hs:
    if he > hs:
        print('Dale\nErin\nSam')
    else:
        print('Dale\nSam\nErin')
elif he > hs:
    if hd > hs:
        print('Erin\nDale\nSam')
    else:
        print('Erin\nSam\nDale')
else:
    if hd > he:
        print('Sam\nDale\nErin')
    else:
        print('Sam\nErin\nDale')
'''

if hd > he > hs:
    print('Dale\nErin\nSam')
elif hd > hs > he:
    print('Dale\nSam\nErin')
elif he > hd > hs:
    print('Erin\nDale\nSam')
elif he > hs > hd:
    print('Erin\nSam\nDale')
elif hs > hd > he:
    print('Sam\nDale\nErin')
else:
    print('Sam\nErin\nDale')
