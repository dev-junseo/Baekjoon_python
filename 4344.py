count = int(input())
per_sum = []

for i in range(count):
    bufer = list(map(int, input().split()))
    avg = (sum(bufer) - bufer[0]) / bufer[0]
    higher = 0
    for j in range(bufer[0]):
        if bufer[j + 1] > avg:
            higher += 1
    per_sum.append((higher / bufer[0]) * 100)
for i in per_sum:
    print("%0.3f%%" %i)
