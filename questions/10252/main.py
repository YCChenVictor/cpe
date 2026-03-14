while True:
    try:
        first = input()
        second = input()
        
        count1 = [0] * 26
        count2 = [0] * 26

        for letter in first:
            count1[ord(letter) - ord('a')] += 1
        for letter in second:
            count2[ord(letter) - ord('a')] += 1

        ans = ""
        for i in range(26):
            common = min(count1[i], count2[i])
            ans += chr(i + ord('a')) * common

        print(ans)
    except EOFError:
        break
