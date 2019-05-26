co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
                   348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]

avg = sum(co2_levels)/len(co2_levels)
print('Average: {:.2f}'.format(avg))
num_above = 0
for level in co2_levels:
    if level > avg:
        num_above += 1
print('Num above average:', num_above)
