def mod_c_style(x, m):
    return x % m if x >= 0 else -((-x) % m)


def sort_key(x, m):
    r = mod_c_style(x, m)
    if x % 2 != 0:   # odd
        return (r, 0, -x)   # the smaller, the prior
    else:            # even
        return (r, 1, x)


while True:
    n, m = map(int, input().split())
    print(n, m)

    if n == 0 and m == 0:
        break

    nums = [int(input()) for _ in range(n)]
    nums.sort(key=lambda x: sort_key(x, m))

    for x in nums:
        print(x)
