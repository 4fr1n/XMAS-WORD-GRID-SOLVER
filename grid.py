def neighbour(co_ordinate,n,m):
    x=co_ordinate[0]
    y=co_ordinate[1]
    if co_ordinate==(0,0):
        return [(1,0),(0,1),(1,1)]
    elif co_ordinate==(0,m):
        return [(0,m-1),(1,m),(1,m-1)]
    elif co_ordinate==(n,0):
        return [(n,1),(n-1,0),(n-1,1)]
    elif co_ordinate==(n,m):
        return [(n-1,m),(n,m-1),(n-1,m-1)]
    elif x==n:
        return [(x-1,y),(x-1,y+1),(x-1,y-1),
                (x,y+1),(x,y-1)]
    elif y==m:
        return [(x+1,y),(x-1,y),
                (x,y-1),(x-1,y-1),(x+1,y-1)]
    elif y==0:
        return [(x+1,y),(x-1,y),
                (x+1,y+1),(x,y+1),(x-1,y+1)]
    elif x==0:
        return [(x+1,y),(x+1,y+1),(x+1,y-1),
                (x,y+1),(x,y-1)]
    else:
        return [(x+1,y),(x-1,y),
                (x,y+1),(x,y-1),
                (x+1,y+1),(x+1,y-1),
                (x-1,y+1),(x-1,y-1)]

count=0
file=open("grid.txt","r")
contents=file.readlines()
file.close()
m=len(contents)-1
n=len(contents[0].strip())-1
co_ordinateList=[]
for i in range(m+1):
    for j in range(n+1):
        co_ordinate=(j,i)
        co_ordinateList.append(co_ordinate)
totalstring=""
for line in contents:
    totalstring+=line.strip()
#now we have a list with co_ordinates and a long string such that the co-rodinate of the ith character of the string = list[i]
#co-ordinate is a tuple (x,y)
for i in range(0,len(totalstring)):
    if totalstring[i]=="X":
        co_ordinate=co_ordinateList[i]
        neighbourhood=neighbour(co_ordinate,n,m)
        for neighbours in neighbourhood:
            index=co_ordinateList.index(neighbours)
            if totalstring[index]=="M":
                direction=(neighbours[0]-co_ordinate[0],neighbours[1]-co_ordinate[1])
                posA=(neighbours[0]+direction[0],neighbours[1]+direction[1])
                posS=(neighbours[0]+2*direction[0],neighbours[1]+2*direction[1])
                if posA in neighbour(neighbours,n,m):
                    Aindex=co_ordinateList.index(posA)
                    if totalstring[Aindex]=="A":
                        if posS in neighbour(posA,n,m):
                            Sindex=co_ordinateList.index(posS)
                            if totalstring[Sindex]=="S":
                                count+=1

print("Total XMAS count=",count)
                    




  




