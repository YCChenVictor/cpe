import math

while True:
    number = int(input())
    if number == 0:
        break

    G = 0
    for i in range(1, number):
        for j in range(i+1, number + 1):
            G += math.gcd(i, j)
    print(G)
