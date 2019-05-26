value_list = []

value = int(input("Enter a value (0 to end): "))
print(value)

while value > 0:
    value_list.append(value)
    value = int(input("Enter a value (0 to end): "))
    print(value)    

avg_values = sum(value_list)/len(value_list)

print("Min: {:d}".format(min(value_list)))
print("Max: {:d}".format(max(value_list)))
print("Avg: {:.1f}".format(avg_values))