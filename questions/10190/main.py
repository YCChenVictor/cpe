while True:
    try:
        den, nom = map(int, input().split())
        if (den == 0) or (nom == 0) or (den < nom) or (nom == 1):
            print("Boring!")
            continue
        answer = []
        while den > 0:
            answer.append(str(den))
            if den % nom != 0:
                break
            den //= nom
        if answer[-1] == '1':
            print(" ".join(answer))
        else:
            print("Boring!")
    except EOFError:
        break
