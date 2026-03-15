cases = int(input())

for i in range(cases):
    print(f"Case {i + 1}:")
    costs = []
    for _ in range(4):
        cost_row = input().split()
        for cost in cost_row:
            costs.append(int(cost))
    
    numbers = int(input())
    for _ in range(numbers):
        number = int(input())
        total_cost = {}
        lowest_cost = float('inf')
        for i in range(2, 37):  # 2 ~ 36
            total = 0
            to_divide = number
            while to_divide > 0:
                digit = to_divide % i
                total += costs[digit]
                to_divide //= i
            total_cost[i] = total
            if total < lowest_cost:
                lowest_cost = total
        bases = []
        for key in total_cost:
            if total_cost[key] == lowest_cost:
                bases.append(str(key))
        print(f"Cheapest base(s) for number {str(number)}: {' '.join(bases)}")
    print("")
