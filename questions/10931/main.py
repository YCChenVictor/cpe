while True:
    try:
        num = int(input())
        if num == 0:
            break
        binary = bin(num).replace("0b", "")
        digits = binary.count("1")
        print(f"The parity of {binary} is {digits} (mod 2).")
    except EOFError:
        break
