while True:
    try:
        coordinates = input().split()
        dots = set()
        for i in range(0, len(coordinates), 2):
            current = coordinates[i] + " " + coordinates[i+1]
            if current in dots:
                dup = current
            dots.add(current)
        dots.remove(dup)

        dots = list(dots)
        dot1 = list(map(float, dots[0].split()))
        dot2 = list(map(float, dots[1].split()))
        dup = list(map(float, dup.split()))

        answer = [dot2[0] + dot1[0] - dup[0], dot2[1] + dot1[1] - dup[1]]

        print(' '.join([f"{x:.3f}" for x in answer]))
        
    except EOFError:
        break
