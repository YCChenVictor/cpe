cases = int(input())

for _ in range(cases):
    n = int(input())
    nums = list(map(int, input().split()))

    swap = 0
    for i in range(n):
        for j in range(n - 1 - i):
            if nums[j] > nums[j+1]:
                nums[j+1], nums[j] = nums[j], nums[j+1]
                swap += 1
    print(f"Optimal train swapping takes {swap} swaps.")
