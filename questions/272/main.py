import sys

data = sys.stdin.read()

answer = ""
firstQuoteExist = False
for letter in data:
    print(letter)
    if letter == '"':
        firstQuoteExist = not firstQuoteExist
        if firstQuoteExist:
            answer += '``'
        else:
            answer += "''"
    else:
        answer += letter

sys.stdout.write(answer)
