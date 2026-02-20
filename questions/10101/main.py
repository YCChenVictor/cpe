import sys

lines = sys.stdin.read().splitlines()

for k in range (0, len(lines)):
    line = lines[k]
    index = str(k+1).rjust(4)
    if line == '0':
        print(f"{index}. {0}")
        continue
    answer = ""
    group = []
    while line:
        group.append(line[-7:])
        line = line[:-7]
    group.reverse()
   
    sub_answers = [] 
    for i in range(0, len(group)):
        chunk = group[i]
        chunk = chunk.zfill(7)
        lakh = int(chunk[0:2])
        hajar = int(chunk[2:4])
        shata = int(chunk[4:5])
        rest = int(chunk[5:7])
        
        out = []
        if lakh: out.append(f"{lakh} lakh")
        if hajar: out.append(f"{hajar} hajar")
        if shata: out.append(f"{shata} shata")
        if rest: out.append(str(rest))
        sub_answers.append(" ".join(out))
    
    print(f"{index}. {' kuti '.join(sub_answers).replace('  ', ' ')}")
