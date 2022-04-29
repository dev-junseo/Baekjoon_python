a, b = input().split()
li = []
def reverse(i):
    re = ''
    for j in i:
        re += j
    return re
li.append(int(reverse(a)))
li.append(int(reverse(b)))
print(max(li))
