temps_at_sites = [ [ 12.12, 13.25, 11.17, 10.4],
                   [ 22.1, 29.3, 25.3, 20.2, 26.4, 24.3 ],
                   [ 18.3, 17.9, 24.3, 27.2, 21.7, 22.2 ],
                   [ 12.4, 12.5, 12.14, 14.4, 15.2 ] ]

averages = []
for site in temps_at_sites:
    avg = sum(site) / len(site)
    averages.append(avg)

max_avg = max(averages)
max_index = averages.index(max_avg)
print("Maximum average of {:.2f} occurs at site {}".format(max_avg, max_index))

                   
