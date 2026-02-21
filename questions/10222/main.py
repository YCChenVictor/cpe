import sys

lines = sys.stdin.read().splitlines()

keyboard = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
mapping = {" ": " "}
for i in range(2, len(keyboard)):
    mapping[keyboard[i]] = keyboard[i-2]

for line in lines:
    answer = ''
    for letter in line:
        answer += mapping[letter]
    print(answer)
