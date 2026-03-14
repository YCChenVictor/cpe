def sum_digit(strNum):
    # 89455446
    copy = strNum
    while len(copy) > 1:
        total = 0
        for num in copy:
            total += int(num)
        copy = str(total)
    return copy
    

while True:
    current = input()
    if current == '0':
        break
    answer = sum_digit(current)
    print(answer)
