import sys

lines = sys.stdin.read().splitlines()
lines = lines[2:]
lines.append("")
collection = {}
total = 0
for line in lines:
    if line == "":
        for key in sorted(collection):
            print(f"{key} {collection[key]/total * 100:.4f}")
        print("")
        collection = {}
        total = 0
    else:
        if collection.get(line) is None:
            collection[line] = 0
        total += 1
        collection[line] = collection[line] + 1
