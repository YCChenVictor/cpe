t = int(input())

bases = [10, 21, 7, 4, 9, 6, 11, 8, 5, 10, 7, 12]
mapping = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for _ in range(t):
    month, day = map(int, input().split())
    difference = day - bases[month - 1] # day more than base

    print(mapping[difference % 7])
