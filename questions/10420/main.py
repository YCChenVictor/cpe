t = int(input())

collection = {}
for _ in range(t):
    country = input().split()[0]
    if collection.get(country) is None:
        collection[country] = 0

    collection[country] = collection[country] + 1

for country in sorted(collection):
    print(f"{country} {collection[country]}")
