

rawlist = open("input.txt", "r")
list = rawlist.readlines()
rawlist.close()
c=0

f = open("result2.txt", "w")
f.writelines(f' {int(list[0]) + int(list[1]) + int(list[2])} (N/A - no previous measurement)\n')
for i in range(3, len(list)):
    if int(list[i-3]) + int(list[i-2]) + int(list[i-1]) < int(list[i-2]) + int(list[i-1]) + int(list[i]):
        f.writelines(f' {int(list[i-2]) + int(list[i-1]) + int(list[i])} (increased)\n')
        c +=1
    elif int(list[i-3]) + int(list[i-2]) + int(list[i-1]) > int(list[i-2]) + int(list[i-1]) + int(list[i]):
        f.writelines(f' {int(list[i-2]) + int(list[i-1]) + int(list[i])} (decreased)\n')
    else:
        f.writelines(f' {int(list[i-2]) + int(list[i-1]) + int(list[i])} (no change)\n')
    
f.writelines(f' In this example, there are {c} sums that are larger than the previous sum.\n')
f.close()