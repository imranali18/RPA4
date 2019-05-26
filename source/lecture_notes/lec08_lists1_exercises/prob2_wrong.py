values = [ 14, 10, 8, 19, 7, 13 ]

x = int(input("Enter a value: "))
print(x)
values.append(x)
x = int(input("Enter another value: "))
print(x)
values.insert(2,x)

print(values[2], values[-1])

print( 'Difference:', max(values) - min(values) )
avg = sum(values) / 8
print( 'Average: {:.1f}'.format(avg))
values.sort()
mid = 3
print( 'Median:', (values[mid]+values[mid+1])/2 )

