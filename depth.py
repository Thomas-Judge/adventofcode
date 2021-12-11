rawlist = open("input.txt", "r")
list = rawlist.readlines()
rawlist.close()
c=0

f = open("result.txt", "w")

f.writelines(list[0].strip('\n') + " - " + "(N/A - no previous measurement)\n",)
for i in range(1, len(list)):
    if int(list[i-1]) <int(list[i]):
        f.writelines(list[i].strip('\n') + " - " + "(increased)\n")
        c +=1
    elif int(list[i-1]) >int(list[i]):
        f.writelines(list[i].strip('\n') + " - " +  "(decreased)\n")
    
f.writelines(f'In this example, there are {c} measurements that are larger than the previous measurement.')
f.close()

