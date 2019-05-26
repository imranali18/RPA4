census = [ 340, 589, 959, 1372, 1918, 2428, 3097, 3880, 4382, 5082, \
            5997, 7268, 9113, 10385, 12588, 13479, 14830, 16782, \
            8236, 17558, 17990, 18976, 19378 ]

index = 1
percent = []
values = []
value = int(input("Enter a value (0 to end): "))
print(value)
while value != 0:
    values.append(value)
    value = int(input("Enter a value (0 to end): "))
    print(value)
print("Min: {}".format(min(values)))
print("Max: {}".format(max(values)))
print("Avg: {:.1f}".format(sum(values)/len(values)))
