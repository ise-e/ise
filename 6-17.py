import random

a0 = [1,2,3,4]
random.shuffle(a0)
a1 = a0[2:] + a0[:2]
a2 = [a0[1],a0[0],a0[3],a0[2]]
a3 = a2[2:] + a2[:2]

aa = [a0,a1,a2,a3]
random.shuffle([aa[:2]])
random.shuffle([aa[2:]])
bb = [aa[0][:],aa[1][:],aa[2][:],aa[3][:]]

e = 0
while True :
    q = input("원하는 난이도 : ")
    if q == "1" : 
        q = 6
        break
    elif q == "2" :
        q = 8
        break
    elif q == "3" :
        q = 10
        break
    else : continue

while e < q :
    a = random.randint(0,3)
    b = random.randint(0,3)
    if bb[a][b] != 0 :
        bb[a][b] = 0
        e = e + 1
    else :
        continue

while aa != bb :
    print(bb[0],"\n",bb[1],"\n",bb[2],"\n",bb[3], sep = "")

    i = input("원하는 번호 : ")
    r,t = i.split()
    r,t = int(r),int(t)
    if bb[r-1][t-1] == 0 :
        h = input("숫자 : ")
        if aa[r-1][t-1] == int(h) :
            bb[r-1][t-1] = int(h)
            print("맞았다")
            continue
        else :
            print("틀렸다")
            continue

print("끝")