import sys

data = sys.stdin.read().split()

i = 0
while i + 1 < len(data):
    a = data[i]
    b = data[i + 1]
    i += 2

    if a == '0' and b == '0':
        break

    p = len(a) - 1
    q = len(b) - 1
    carry = 0
    count = 0
    while p >= 0 or q >= 0:
        da = ord(a[p]) - 48 if p >= 0 else 0
        db = ord(b[q]) - 48 if q >= 0 else 0

        if da + db + carry >= 10:
            count += 1
            carry = 1
        else:
            carry = 0

        p -= 1
        q -= 1
  
    if count == 1:
        print(f"{count} carry operation.")
    elif count == 0:
        print("No carry operation.")
    else:
        print(f"{count} carry operations.")
