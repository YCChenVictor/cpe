def check(numbers):
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            target = numbers[i] + numbers[j]
            if target in sum:
                return False
            sum.add(numbers[i] + numbers[j])
    return True


case = 0
while True:
    try:
        nums = input()
        numbers = list(map(int, input().split()))
        space = input()
        sum = set()
        case += 1
        if check(numbers):
            print(f"Case #{case}: It is a B2-Sequence.")
        else:
            print(f"Case #{case}: It is not a B2-Sequence.")
        print("")
    except EOFError:
        break
