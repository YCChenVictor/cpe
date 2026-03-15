is_primes = [True] * 1000000  # 0 ~ 999999
is_primes[0] = False
is_primes[1] = False

for i in range(2, int(1000000 ** 0.5) + 1):
    if is_primes[i]:
        for j in range(i * i, 1000000, i):
            is_primes[j] = False

while True:
    try:
        num_input = input().strip()
        num = int(num_input)
        rev = int(num_input[::-1])

        if not is_primes[num]:
            print(f"{num} is not prime.")
        elif rev != num and is_primes[rev]:
            print(f"{num} is emirp.")
        else:
            print(f"{num} is prime.")
    except EOFError:
        break
