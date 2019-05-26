values = [ 14, 10, 8, 19, 7, 13 ]

x = int(input("Enter a value: "))
print(x)
values.append(x)
x = int(input("Enter another value: "))
print(x)
values.insert(3,x)

print(values[2], values[-1])

print( 'Difference:', max(values) - min(values) )
avg = sum(values) / len(values)
print( 'Average: {:.1f}'.format(avg))
values.sort()
mid = len(values)//2 - 1
print( 'Median:', (values[mid]+values[mid+1])/2 )

