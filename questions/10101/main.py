def bangla(n):
    answer = []

    def helper(n):
        if n >= 10000000:
            helper(n // 10000000)
            answer.append('kuti')
            n %= 10000000
        if n >= 100000:
            helper(n // 100000)
            answer.append('lakh')
            n %= 100000
        if n >= 1000:
            helper(n // 1000)
            answer.append('hajar')
            n %= 1000
        if n >= 100:
            helper(n // 100)
            answer.append('shata')
            n %= 100
        if n > 0:
            answer.append(str(n))

    if n == 0:
        return "0"

    helper(n)
    return " ".join(answer)

i = 1
while True:
    try:
        number = int(input())
        print(f"{i:>4}. {bangla(number)}")
        i += 1
    except EOFError:
        break
