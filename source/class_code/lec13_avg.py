file_name = input("Enter the name of the scores file: ")
file_name = file_name.strip()   # Eliminate extra white space that the user may have typed
print(file_name)

num_scores = 0
sum_scores = 0
for s in open(file_name):
    sum_scores += int(s)
    num_scores += 1
    print(int(s))

print("Average score is {:.1f}".format(sum_scores / num_scores))
