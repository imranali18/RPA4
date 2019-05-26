"""
Lecture 13 Practice Problem: Parse the yelp.txt data file to create a
list of lists of names and averages. This demonstrates parsing an
irregularly formatted file. We have to know that the 0th entry on
each line and the 6th are the scores.

Prof. Stewart
"""


def yelp_averages(yelp_name):
    averages = []
    for line in open(yelp_name):
        line = line.split('|')
        name = line[0]
        scores = line[6:]    # From entry 6 on are the scores

        if len(scores) == 0:
            # Handle the special case of an empty scores list
            averages.append([name, -1])
        else:
            # Compute the average when there is at least one score
            sum_score = 0
            for s in scores:
                sum_score += int(s)
            avg = sum_score / len(scores)
            averages.append([name, avg])

    return averages

avgs = yelp_averages('yelp.txt')
print(avgs[0:3])
