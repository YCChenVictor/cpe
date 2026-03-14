# you can use `python3 main.py < input.in > output.txt` to write the file
# Directly copy from the terminal will remove the space in the end of string

while True:
    try:
        answer = ""
        line = input()
        is_first = True
        for letter in line:
            if letter == '"':
                if is_first:
                    answer += '``'
                else:
                    answer += "''"
                is_first = not is_first
            else:
                answer += letter

        print(answer)
    except EOFError:
        break
