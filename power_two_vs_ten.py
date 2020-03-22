# Solution to the 538 Riddler Express for March 18th 2020
# original author is David R. Perek
# Provided under the MIT license. Have fun

import math
from decimal import Decimal
from decimal import getcontext

found_max = 10  # maximum number of values to find
getcontext().prec = found_max # make sure we have "enough" precision, maybe
found = 0 # number of values found so far
# threshold sets the maximum amount of error between the power of two and the nearest
# power of ten for the pair to be considered a found value
threshold = pow(Decimal(2), 10) / pow(Decimal(10), 3) - Decimal(1.0)
# sets the initial power of two to consider in the search
current_exp_2 = 10

# while we still have values to find
# note this solution is fundamentally inefficient as it searches by the smaller base
# and we'd find it faster to search by power of ten. For example, with the known solution to the
# puzzle of power(10,28) and power(2,93), we would need to search 83 powers of two
# here versus only 25 powers of ten in this technique.
# I wonder if this method could be faster in practice, since computing the powers of two is cheap,
# and we could screen the first two digits in base ten to weed out most impossible values, or apply a
# heuristic to the first bits to see if it can be a possible consideration. In any case, I didn't do this.
while found < found_max:
    current_val_2 = Decimal(1 << current_exp_2)  # compute the current power of two
    current_log_2 = Decimal.log10(current_val_2)  # compute the base ten log of the current value of two
    current_exp_10 = divmod(current_log_2,1)[0]  # consider only the integer part of the log
    val_10_low = pow(Decimal(10), current_exp_10)  # compute this power of ten
    val_10_high = val_10_low * 10  # compute the next power of ten

    # find out which of the two above powers of ten are actually closer to the power of two considered
    # note I could see if the fractional part is >= log[10](5) as well, but this seems easier to grok
    if (current_val_2 - val_10_low) < (val_10_high - current_val_2):
        current_val_10 = val_10_low
    else:
        current_val_10 = val_10_high

    # find the ratio metric error between the power of two and the closest power of ten
    error = Decimal(current_val_2) / Decimal(current_val_10) - Decimal(1.0)
    if abs(error) <= threshold: # if the error is less than or equal to the threshold
        # print the values out
        print str(found) + "," + str(current_val_2) + "," + str(current_val_10) + "," + str(error)
        # put a notch in the belt
        found = found + 1
    # prepare for the next search iteration
    current_exp_2 = current_exp_2 + 1