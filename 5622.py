dial = input()
dial_num = []
for i in range(len(dial)):
    if  ord(dial[i]) >= 65 and ord(dial[i]) <= 67:
        dial_num.append(2)
    elif  ord(dial[i]) >= 68 and ord(dial[i]) <= 70:
        dial_num.append(3)
    elif  ord(dial[i]) >= 71 and ord(dial[i]) <= 73:
        dial_num.append(4)
    elif  ord(dial[i]) >= 74 and ord(dial[i]) <= 76:
        dial_num.append(5)
    elif  ord(dial[i]) >= 77 and ord(dial[i]) <= 79:
        dial_num.append(6)
    elif  ord(dial[i]) >= 80 and ord(dial[i]) <= 83:
        dial_num.append(7)
    elif  ord(dial[i]) >= 84 and ord(dial[i]) <= 86:
        dial_num.append(8)
    elif  ord(dial[i]) >= 87 and ord(dial[i]) <= 90:
        dial_num.append(9)
time = 0
for i in range(len(dial_num)):
    if dial_num[i] == 1:
        time += 2
    elif dial_num[i] == 2:
        time += 3
    elif dial_num[i] == 3:
        time += 4
    elif dial_num[i] == 4:
        time += 5
    elif dial_num[i] == 5:
        time += 6
    elif dial_num[i] == 6:
        time += 7
    elif dial_num[i] == 7:
        time += 8
    elif dial_num[i] == 8:
        time += 9
    elif dial_num[i] == 9:
        time += 10
print(time)
