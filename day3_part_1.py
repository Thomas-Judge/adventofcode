with open("input3", "r") as rawlist:
    list = [x for x in rawlist.read().split("\n")]

x=[]
z=0
o=0
iter=0
list_ones=[]
list_zeroes=[]
gamma=[]
epsilon=[]

while z<(len(list[0])):
    for i in list:
        x.append(i[z])
    z+=1

chunked_list = []
chunk_size = len(list)

for j in range(0, len(x)):
    x[j]=(int(x[j]))
    
for m in range(0, len(x), chunk_size):
    chunked_list.append(x[m:m+chunk_size])

o = chunked_list[0].count(1)
z = chunked_list[0].count(0)


for k in range(0, len(chunked_list)):
    list_ones.append(chunked_list[iter].count(1))
    list_zeroes.append(chunked_list[iter].count(0))
    iter+=1



lool = 0
for lol in range(0, len(list_ones)):
    if list_ones[lool] > list_zeroes[lool]:
        gamma.append(1)
        epsilon.append(0)
    else:
        gamma.append(0)
        epsilon.append(1)
    lool+=1

s1=[str(int) for int in gamma]
gammabinary= "".join(s1)

s2=[str(int) for int in epsilon]
epsilonbinary= "".join(s2)

print(gammabinary)
print(epsilonbinary)

epsilonbinaryfinal=(int(gammabinary, 2))
gammabinaryfinal=(int(epsilonbinary, 2))

print(f'The power consumption of the submarine is: {int(epsilonbinaryfinal*gammabinaryfinal)}')