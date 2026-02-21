import sys

lines = sys.stdin.read().splitlines()

is_primes = [True] * (1000000 + 1) # from 0 to 1000000
for i in range(2, int(1000000**0.5) + 1):
    if is_primes[i]:
        for j in range(i * i, 1000000 + 1, i):
            is_primes[j] = False    

for line in lines:
    number = int(line)
    rebmun = int(line[::-1])
    if not is_primes[number]:
        print(f'{number} is not prime.')
    else:
        if number != rebmun and is_primes[rebmun]:
            print(f'{number} is emirp.')
        else:
            print(f'{number} is prime.')
        
