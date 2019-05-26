scores_name = input('Enter the scores file: ')
print(scores_name)
sorted_name = input('Enter the output file: ')
print(sorted_name)

scores = []
for line in open(scores_name):
    s = int(line)
    scores.append(s)

scores.sort()
out_f = open(sorted_name,'w')
for i in range(len(scores)):
    out_f.write('{:2d}: {:3d}\n'.format(i,scores[i]))
