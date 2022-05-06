rate = list(map(int, input().split()))
fixed_cost = rate[0]
variable_cost = rate[1]
notebook_cost = rate[2]
impossible = -1

if variable_cost >= notebook_cost:
    print(impossible)
else:
    count = int(fixed_cost / (notebook_cost - variable_cost)) + 1
    print(count)
