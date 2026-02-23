import sys

lines = sys.stdin.read().splitlines()

i = 0
num_of_case = 1
i += 1
digits = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
while i < len(lines):
    costs = ""
    for j in range(i, i + 4):
        costs += " " + lines[j]
    i += 4
    costs = costs.split()
    cost_mapping = {}
    for c in range(0, len(digits)):
        cost_mapping[digits[c]] = costs[c]
    numbers = int(lines[i])
    i += 1
    print(f"Case {num_of_case}:")
    num_of_case += 1
    for k in range(i, i + numbers):
        answer = ''
        target = int(lines[k])
        transform = ""
        cost_total = []
        for mod in range(2, 37):
            cost = 0
            n = target
            while n > 0:
                n, r = divmod(n, mod)
                cost += int(cost_mapping[digits[r]])
            cost_total.append(cost)
        lowest_cost = min(cost_total)
        for a in range(0, len(cost_total)):
            if cost_total[a] <= lowest_cost:
                answer += " " + str(a+2)
        print(f"Cheapest base(s) for number {target}:{answer}")
    i += numbers
    print("")
