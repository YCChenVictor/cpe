mapping = "1234567890-=qwertyuiop[]asdfghjkl;'zxcvbnm,./"

while True:
    try:
        line = input()
        answer = ""
        for letter in line:
            if letter == " ":
                answer += " "
            else:
                answer += mapping[mapping.index(letter) - 2]
        print(answer)
    except EOFError:
        break