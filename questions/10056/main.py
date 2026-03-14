# Calculation
# p = winning prob
# q = losing prob = 1 - p
# players = number of players
# 1th win = p + q^players * p + q^(2 * players) * p + ... = x
# 2th win = qp + q^players * q * p + ... = q * x
# 3th win = q^2 * x

# x = p / (1 - q^players) = 0.1666/(1 - 0.8333^2)
# answer = q^(winner - 1) * x

cases = input()

while True:
    try:
        players, win_prob, winner = map(float, input().split())
        if win_prob == 0:
            print("0.0000")
            continue
        lose_prob = 1 - win_prob
        x = win_prob / (1 - lose_prob ** players)
        answer = lose_prob ** (winner - 1) * x
        print(f"{answer:.4f}")
    except EOFError:
        break
