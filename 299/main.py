import sys

data = sys.stdin.read().split()

num_of_trains = data[0]

i = 1
while i < len(data):
    cars = int(data[i])

    order = []
    for j in range(i + 1, i + cars + 1):
        order.append(int(data[j]))
        i += 1
    i += 1

    requireSwap = True
    numOfSwap = 0
    while requireSwap:
        noSwapOccurred = True
        for k in range(0, len(order) - 1):
            if (order[k] > order[k+1]):
                order[k+1], order[k] = order[k], order[k+1]
                numOfSwap += 1
                noSwapOccurred = False
        if noSwapOccurred:
            requireSwap = False
        
    print(f"Optimal train swapping takes {numOfSwap} swaps.")
