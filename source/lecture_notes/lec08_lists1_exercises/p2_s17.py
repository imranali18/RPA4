values = [ 14, 10, 8, 19, 7, 13 ]
val1 = int(input("Enter a value: "))
print(val1)
values.append(val1)
val2 = int(input("Enter another value: "))
print(val2)
values.insert(2, val2)
print(values[3], values[-1])
values.sort()
median = (values[len(values)//2-1] + values[len(values)//2]) / 2
print("Difference: {}".format(max(values) - min(values)))
print("Average: {:.1f}".format(sum(values)/len(values)))
print("Median: {:.1f}".format(median))
