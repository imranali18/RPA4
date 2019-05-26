census = [ 340, 589, 959, 1372, 1918, 2428, 3097, 3880, 4382, 5082, \
            5997, 7268, 9113, 10385, 12588, 13479, 14830, 16782, \
            8236, 17558, 17990, 18976, 19378 ]

index = 1
percent = []

while index < len(census):
    percent.append((census[index]-census[index-1])/census[index-1] * 100)
    index += 1
    
average = sum(percent)/len(percent)
print("Average = {:.1f}%".format(average))