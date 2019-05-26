values = []
done = False
while not done:
    n = int(input("Enter a value (0 to end): "))
    print(n)
    if n == 0:
        done = True
    else:
        values.append(n)

print('Min:', min(values))
print('Max:', max(values))
print('Avg: {:.1f}'.format(sum(values)/len(values)))
