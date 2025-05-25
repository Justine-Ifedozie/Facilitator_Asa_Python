import math
number = 13.56449
tenth_roundup = 10 ** 1
tenth_result = math.ceil(number * tenth_roundup)
tenth_total =  tenth_result / tenth_roundup

hundredth_roundup = 10 ** 2
hundredth_result = math.floor(number * hundredth_roundup)
hundredth_total = hundredth_result / hundredth_roundup

thousandth_roundup = 10 ** 3
thousandth_result = math.floor(number * thousandth_roundup)
thousandth_total = thousandth_result / thousandth_roundup


print(f"Round off: {number} to the nearest integer: {math.ceil(number)}")
print(f"Round off: {number} to the nearest tenths: {tenth_total}")
print(f"Round off: {number} to the nearest hundredths: {hundredth_total}")
print(f"Round off: {number} to the nearest thousandths: {thousandth_total}")

