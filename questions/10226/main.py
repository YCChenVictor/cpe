import sys

lines = sys.stdin.read().splitlines()
lines.append('')

answer = {}
for i in range(2, len(lines)):
    if lines[i] == '':
        keys = list(answer.keys())
        keys.sort()
        values = list(answer.values())
        for key in keys:
            print(f"{key} {answer[key]/sum(values) * 100:.4f}")
        print('')
        answer = {}
        continue

    if answer.get(lines[i]) == None:
        answer[lines[i]] = 1
    else:
        answer[lines[i]] += 1
