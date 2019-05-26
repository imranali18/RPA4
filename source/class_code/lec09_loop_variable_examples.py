"""
Two examples of manipulating loop variables. The first prints out every 
other element of the list starting from the first element. The second uses the
loop variable to print out an evergreen tree.
"""


months=['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

i = 0
while i < len(months):
    print(months[i])
    i += 2

# Now print out the evergreen.
print()
i = 1
length = 9
while i < 10:
    print((4 - i // 2 ) * " " + i * '*')
    i += 2

print(3 * " " + 3 * '*')
print(3 * " " + 3 * '*')

"""
Finally, let's let the user pick
an odd value > 3.
"""
print()
field = int(input("Enter an odd number greater than 3: "))
if field % 2 == 1 and field > 3:
    j = 1
    while j <= field:
        print((field - j) // 2 * ' ', j * "*")
        j += 2
    j = 3
    print((field - j) // 2 * ' ', j * "*")
    print((field - j) // 2 * ' ', j * "*")
else:
    print("{} is not an odd integer greater than 3.".format(field))