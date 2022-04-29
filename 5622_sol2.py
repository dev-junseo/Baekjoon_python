alp = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
dial = input()
time = 0
for a in alp:
    for b in a:
        for i in dial:
            if i == b:
                time += alp.index(a) + 3
print(time)
