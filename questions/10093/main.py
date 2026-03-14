base_mapping = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

while True:
    try:
        num = input()
        base = 2
        if num == "0":
            print(base)
            continue
        # first guess, must > any digits
        sum = 0
        for digit in num:
            if digit in ["+", "-", " "]:
                continue
            if base_mapping.index(digit) >= base:
                base = base_mapping.index(digit) + 1
            sum += base_mapping.index(digit)

        answer = -1  # this is really important
        for i in range(base, 62 + 1):  # check the division
            if sum % (i - 1) == 0:
                answer = i
                break  # smallest

        if answer == -1:
            print("such number is impossible!")
        else:
            print(answer)
        
    except EOFError:
        break
