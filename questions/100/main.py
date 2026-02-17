import sys

data = sys.stdin.buffer.read().split()
out = []
it = iter(data)

def calculation(n):
    if n == 1:
        return 1

    if n % 2:
        return 1 + calculation(3*n+1)
    else:
        return 1 + calculation(n//2)

for a in it:
    b = next(it, None)
    if b is None:
        break
    i = int(a); j = int(b)
    l, h = (i, j) if i < j else (j, i)
    
    best = 0
    for x in range(l, h+1):
        best = max(best, calculation(x))

    out.append(f"{i} {j} {best}")
    

sys.stdout.write("\n".join(out))
