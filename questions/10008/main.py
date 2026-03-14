t = int(input())

collection = {}
for _ in range(t):
    line = input()
    for text in line:
        if not (("a" <= text <= "z") or ("A" <= text <= "Z")):
            continue
        cap_letter = text.capitalize()
        if collection.get(cap_letter) is None:
            collection[cap_letter] = 0
        collection[cap_letter] = collection[cap_letter] + 1

items = list(collection.items())
items.sort(key=lambda item: (-item[1], item[0]))
for item in items:
    print(f"{item[0]} {item[1]}")
