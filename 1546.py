sub = int(input())
score = list(map(int, input().split()))
new_sc = []
for i in range(sub):
    new_sc.append((score[i] / max(score) * 100))
print(sum(new_sc) / sub)
