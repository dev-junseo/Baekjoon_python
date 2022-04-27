count = int(input())
result = []
for a in range(count):
    r, s = input().split()
    p = ''
    for b in s:
        p += b * int(r)
    result.append(p)
for i in range(count):
    print(result[i])
