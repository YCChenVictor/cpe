import math

cases = int(input())

for case in range(cases):
    target = int(input(), 2)
    base = int(input(), 2)

    gcd = math.gcd(target, base)
    
    if gcd > 1:
        print("All you need is love!")
    else:
        print("Love is not all you need!")
