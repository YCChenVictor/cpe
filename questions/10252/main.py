import sys

lines = sys.stdin.read().splitlines()

for i in range(0, len(lines), 2):
    first = list(lines[i])
    second = list(lines[i+1])

    first_dict = {}
    for letter in first:
        if first_dict.get(letter) == None:
            first_dict[letter] = 0
        first_dict[letter] += 1

    second_dict = {}
    for letter in second:
        if second_dict.get(letter) == None:
            second_dict[letter] = 0
        second_dict[letter] += 1

    both_keys = first_dict.keys() & second_dict.keys()

    answer = ""
    for key in both_keys:
        first_amount = first_dict[key]
        second_amount = second_dict[key]
        min_amount = min(first_amount, second_amount)

        answer += key * min_amount


    print("".join(sorted(answer)))
