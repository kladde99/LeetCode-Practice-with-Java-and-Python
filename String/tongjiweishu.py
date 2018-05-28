import math

s  = raw_input("Int array")
mylist = map(int, s.split())

for x in range(2, len(s)):

    digits = int(math.log10(s[-1])) + 1

    # for x in range(1, 4)

