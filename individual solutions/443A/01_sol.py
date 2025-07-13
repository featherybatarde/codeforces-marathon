"""
tags:
easy, wft
"""
a = input()[1:-1]
print([len(set(a)) - 2, [1,0][a ==""]][len(a)<=1])