with open("input2.txt", "r") as rawlist:
   for x in rawlist:
       list = rawlist.read().split("\n")

print(list)

a = 0
b = 0
for i in list:
    i = i.split()
    if i[0] == "forward":
        a += int(i[1])
    elif i[0] == "up":
        b -= int(i[1])
    elif i[0] == "down":
        b += int(i[1])
    else:
        print("N/A")

print(f'Solutions: forward: <{a}> depth: <{b}> vector (multiple): <{a*b}>')