import sys

lines = sys.stdin.read().splitlines()

for line in lines:
    collect = {}
    for ch in line:
        asc = ord(ch)
        if collect.get(asc) == None:
            collect[asc] = 1
        else:
            collect[asc] += 1

    swap_collect = {}
    for k in collect:
        if swap_collect.get(collect[k]) == None:
            swap_collect[collect[k]] = []
        swap_collect[collect[k]].append(k)

    for k in sorted(swap_collect):
        asc_codes = swap_collect[k]
        asc_codes.sort(reverse=True)
        for asc_code in asc_codes:
            print(asc_code, k)
    print(" ")        
