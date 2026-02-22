import sys

lines = sys.stdin.read().splitlines()

for line in lines:
    collection = set()
    numbers = line.split()
    shared = []
    for i in range(0, len(numbers) - 1, 2):
        if (numbers[i], numbers[i + 1]) in collection:
            shared = (numbers[i], numbers[i + 1])
        else:
            collection.add((numbers[i], numbers[i + 1]))

    x, y = 0, 0
    for element in collection:
        (x_d, y_d) = element
        x += float(x_d)
        y += float(y_d)

    (x_s, y_s) = shared
    
    x -= 2 * float(x_s)
    y -= 2 * float(y_s)

    print(f"{x:.3f}", f"{y:.3f}")
