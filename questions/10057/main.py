while True:
    try:
        cases = int(input())
        nums = list(map(int, input().split()))
        nums.sort()

        length = len(nums)
        low = nums[(length - 1) // 2]
        high = nums[length // 2]

        count = 0
        for num in nums:
            if low <= num <= high:
                count += 1

        print(low, count, high - low + 1)
    except EOFError:
        break
