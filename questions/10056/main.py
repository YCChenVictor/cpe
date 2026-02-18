# winning prob = p
# losing prob = q
# 1th player win = p + q^N * p + q^2N * p + ... = p (1 + q^N + q^2N + ...) = p/(1-q^N)
# 2th player win = qp/(1-q^N)
# 3th player win = q^2 * p/(1-q^N)
# ...

import sys

data = sys.stdin.read().splitlines()
for i in range(1, len(data)):
    line = data[i]
    numbers = line.split()
    prob = float(numbers[1])
    player = int(numbers[2])
    players = int(numbers[0])
    if prob == 0.0:
        answer = 0
    else:
        answer = (1-prob)**(player-1) * prob / (1-(1-prob)**players)
    print(f"{answer:.4f}")
