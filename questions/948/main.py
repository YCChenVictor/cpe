fib = [1, 2]

i = 1
new = 0
while True:
    new = fib[i - 1] + fib[i]
    if new > 100000000:
        break
    fib.append(new)
    i += 1

fib.reverse()

cases = input()
while True:
    try:
        answer = ""
        num = int(input())
        to_extract = num
        for extract in fib:
            if to_extract >= extract:
                to_extract -= extract
                answer += "1"
            else:
                answer += "0"
        print(f"{num} = {int(answer)} (fib)")
    except EOFError:
        break
