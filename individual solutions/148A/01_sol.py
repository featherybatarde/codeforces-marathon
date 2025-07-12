"""
tags:
800,difficult,clunky
"""

a = []
for i in [0]*4:
    a.append(int(input()))


d = int(input())
c =0 # counter for distinct multiples
# find the number of distinct multiples of inputs in the span of 1-(greatest inputted number)
for x in range(1, d + 1):
    if not(x%a[3] and x%a[2] and x%a[1] and x%a[0]):
        c+=1

print(c)
