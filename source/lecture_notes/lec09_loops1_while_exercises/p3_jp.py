number_list = []
number = int(input('Enter a value (0 to end): '))
print(number)

while number != 0:
    number_list.append(number)
    number = int(input('Enter a value (0 to end): '))
    print(number)

print('Min: {:d}'.format(min(number_list)))
print('Max: {:d}'.format(max(number_list)))
print('Avg: {:0.1f}'.format(sum(number_list) / len(number_list)))
