cases = int(input())

for _ in range(cases):
    num = input()

    num1 = int(num)
    num1 = bin(num1)
    num1 = num1.count("1")

    num2 = int(num, 16)
    num2 = bin(num2)
    num2 = num2.count("1")

    print(num1, num2)

# for _ in range(cases):
#     num = input()
#     print(num)
#     num = int(num)
#     num = bin(num)
#     print(num)