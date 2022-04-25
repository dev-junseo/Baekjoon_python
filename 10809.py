s = input()
alphabet = ['a', 'b', 'c', 'd', 'e' ,'f', 'g', 
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 
            'o', 'p', 'q', 'r', 's', 't', 'u', 
            'v', 'w', 'x', 'y', 'z']
count = [-1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1]
for a in range(len(s)):
    for b in range(len(alphabet)):
        if (s[a] == alphabet[b]):
            if count[b] == -1:
                count[b] = a
print(*count)
