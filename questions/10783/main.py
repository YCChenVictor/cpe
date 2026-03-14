cases = int(input())

for j in range(cases):
    start = int(input())
    end = int(input())
    answer = 0
    for i in range(start, end+1):
        if i % 2 == 1:
            answer += i
    print(f"Case {j + 1}: {answer}")
