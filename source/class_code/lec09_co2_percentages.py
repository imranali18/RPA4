"""
Demonstrate walking through a list calculating values between pairs of
values. In this instance we are calculating the percent change year-to-year
for CO2 concentration.
"""

co2_levels = [(2001, 320.03), (2003, 322.16), (2004, 328.07),\
              (2006, 323.91), (2008, 341.47), (2009, 348.92),\
              (2010, 357.29), (2011, 363.77), (2012, 361.51),\
              (2013, 382.47)]

i = 1
percent_change = []
while i < len(co2_levels):
    percent_change.append((co2_levels[i][1] - co2_levels[i - 1][1]) / co2_levels[i - 1][1])
    i += 1

print(percent_change)