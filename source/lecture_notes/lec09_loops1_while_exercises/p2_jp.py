census = [340, 589, 959, 1372, 1918, 2428, 3097, 3880, 4382, 5082, 5997, 7268, 9113,
          10385, 12588, 13479, 14830, 16782, 8236, 17558, 17990, 18976, 19378]

percentage_list = []
index = 0
while index < len(census) - 1:
    previous = census[index]
    current = census[index + 1]
    delta = current - previous
    percentage = 100.0 * (delta / previous)
    percentage_list.append(percentage)
    index += 1

print('Average = {:0.1f}%'.format(sum(percentage_list) / len(percentage_list)))
