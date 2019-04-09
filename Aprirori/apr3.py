#name = input()
#min_s=int(input())
import copy
name ="ex1.csv"
min_s=3


f = open(name)
c1=dict()
for i in f:
    for j in i.strip().split(","):
        if (j,) not in c1:
            c1[(j,)]=1
        else:
            c1[(j,)]+=1

f.close()

print("C1 = ",c1)

def prune(c,min):
    cc = dict()
    for i in c:
        if c[i]>=min:
            cc[i]=c[i]
    return cc


def gen(l):
    c=dict()
    lis=sorted(l.keys())
    #print(lis)
    for i in range(len(lis)):
        for j in range(i+1,len(lis)):
            #print(lis[i][:-1])
            if lis[i][:-1]==lis[j][:-1]:
                t = lis[i]+(lis[j][-1],)
                c[t]=0
    return c


def cand_freq(c,name):
    f = open(name)
    for i in f:
        for k in c:
            num=0
            for l in k:
                if l in i.strip().split(","):
                    num+=1
            if num==len(k):
                c[k]+=1
    return c


l = prune(c1,min_s)
print("L1= ",l)
count = 2

while l!={}:
    c=gen(l)
    c=cand_freq(copy.deepcopy(c),name)
    print("C",count," = ",c)
    l=prune(c,min_s)
    print("L", count, " = ", l)

    count+=1





