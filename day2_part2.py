with open("input2.txt", "r") as rawlist:
    list = [x for x in rawlist.read().split("\n")]
a = 0
b = 0
aim = 0

for i in list:
    i = i.split()
    if i[0] == "up":
        aim -= int(i[1])
    elif i[0] == "down":
        aim += int(i[1])
    elif i[0] == "forward":
        b += aim* int(i[1])
        a += int(i[1])
    else:
        print("N/A")

print(f'Solutions: forward: <{a}>  depth: <{b}> aim: <{aim}> final horizontal position by my final depth<{a*b}>')
