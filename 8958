leng = int(input())
quiz = []
for i in range(leng):
    q = input()
    quiz.append(q)
score = []
for a in range(leng):
    db = 1
    bufer = []
    for b in range(len(quiz[a])):
        if quiz[a][b] == "O":
            bufer.append(db)
            db += 1
        elif quiz[a][b] == "X":
            bufer.append(0)
            db = 1
    score.append(sum(bufer))
    bufer = []
for i in range(len(score)):
    print(score[i])
