import sys

data = sys.stdin.read().splitlines()

i = 0
tests = data[0]
i += 1
while i < len(data):
    strikes = set()
    days = int(data[i])
    i += 1
    parties = int(data[i])
    i += 1
    hartal_parameters = []
    for j in range(0, parties):
        hartal_parameters.append(int(data[i]))
        i += 1
    for k in range(0, len(hartal_parameters)):
        hartal_parameter = hartal_parameters[k]
        mod = days // hartal_parameters[k]
        for m in range(0, mod):
            strikes.add((m + 1) * hartal_parameter)
    strike_elements = list(strikes)
    for element in strike_elements:
        if element % 7 == 0:
            strikes.discard(element)
        if element % 7 == 6:
            strikes.discard(element)

    print(len(strikes))
