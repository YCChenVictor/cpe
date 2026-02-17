import sys

data = sys.stdin.read().split()

num_of_nums = data[0]

threshold = 100000000
fib_numbers = []

fib_0 = 0
fib_1 = 1
current_value = fib_0 + fib_1
fib_numbers = []
while True:
    current_value = fib_0 + fib_1

    if current_value > threshold:
        break
    fib_numbers.append(current_value)
    fib_0 = fib_1
    fib_1 = current_value

fib_numbers.reverse()

for i in range(1, len(data)):
    left = int(data[i])
    answer = ''
    for j in range(0, len(fib_numbers)):
        if fib_numbers[j] <= left:
            left -= fib_numbers[j]
            answer += '1'
        else:
            answer += '0'

    print(f"{int(data[i])} = {answer.lstrip('0')} (fib)")
