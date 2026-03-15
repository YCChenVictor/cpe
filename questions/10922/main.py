while True:
    number = int(input())
    if number == 0:
        break

    if number % 9 != 0:
        print(f"{number} is not a multiple of 9.")
        continue

    degree = 1 # we already make sure it is 9
    to_divide = number
    while to_divide > 9:
        str_num = str(to_divide)
        sum = 0
        for digit in str_num:
            sum += int(digit)
        to_divide = sum // 3
        degree += 1
    print(f"{number} is a multiple of 9 and has 9-degree {degree}.")
