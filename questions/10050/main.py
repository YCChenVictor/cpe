#  no hartals on on Fridays and Saturdays: 5, 6, 12, 13, ...
#  start from Sunday

cases = int(input())

for _ in range(cases):
    days = int(input())
    parties = int(input())
    strikes = [0] * days  # 0 means no strike
        
    for j in range(parties):
        party = int(input())
        for i in range(len(strikes)):
            if (i + 1) % party == 0:
                strikes[i] = 1

    # no Friday & Saturday
    friday = 5
    while friday < len(strikes):
        strikes[friday] = 0
        friday = friday + 7

    saturday = 6
    while saturday < len(strikes):
        strikes[saturday] = 0
        saturday = saturday + 7

    print(sum(strikes))