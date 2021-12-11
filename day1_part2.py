rawlist = open("input.txt", "r")
list = rawlist.readlines()
rawlist.close()
c=0


print(int(list[0]) + int(list[1]) + int(list[2]), "(N/A - no previous measurement)\n",)
for i in range(3, len(list)):
    if int(list[i-3]) + int(list[i-2]) + int(list[i-1]) < int(list[i-2]) + int(list[i-1]) + int(list[i]):
        print(int(list[i-2]) + int(list[i-1]) + int(list[i]) ,"(increased)\n")
        c +=1
    elif int(list[i-3]) + int(list[i-2]) + int(list[i-1]) > int(list[i-2]) + int(list[i-1]) + int(list[i]):
        print(int(list[i-2]) + int(list[i-1]) + int(list[i]), "(decreased)\n")
    else:
        print(int(list[i-2]) + int(list[i-1]) + int(list[i]), "(no change)")
    
print(f'In this example, there are {c} sums that are larger than the previous sum.')