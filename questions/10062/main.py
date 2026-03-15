while True:
    try:
        line = input()
        collection = {}
        for ch in line:
            encode = ord(ch)
            if collection.get(encode) is None:
                collection[encode] = 0
            collection[encode] = collection[encode] + 1
        for code, freq in sorted(collection.items(), key=lambda item: (item[1], -item[0])):  # sort with frequency first, then the key
            print(code, freq)
        print("")
    except EOFError:
        break