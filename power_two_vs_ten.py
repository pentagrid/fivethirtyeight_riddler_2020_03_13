import math
from decimal import Decimal
found = 0
threshold = pow(Decimal(2), 10) / pow(Decimal(10), 3) - Decimal(1.0)
current_exp_2 = 10

while found < 10:
    current_val_2 = pow(Decimal(2), current_exp_2)
    current_log_2 = math.log10(current_val_2)
    current_exp_10 = math.floor(current_log_2)
    val_10_low = pow(Decimal(10), int(current_exp_10))
    val_10_high = pow(Decimal(10), int(current_exp_10) + 1)
    if (current_val_2 - val_10_low) < (val_10_high - current_val_2):
        current_val_10 = val_10_low
    else:
        current_val_10 = val_10_high

    error = Decimal(current_val_2)/Decimal(current_val_10) - Decimal(1.0)
    current_exp_2 = current_exp_2 + 1
    if abs(error) <= threshold:
        print str(found)+","+str(current_val_2)+","+str(current_val_10)+","+str(error)
        found = found + 1


