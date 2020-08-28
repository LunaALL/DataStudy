from collections import Counter
phe = "김,감,김"
ctnr = Counter(phe.split(","))

dic1= dict(ctnr.most_common())
print(dic1['김'])

print(ctnr.most_common())




def gugu(a):
    for i in range(1, a):
        for j in range(1, 10):
            print("%d * %d = %d" % (i, j, i * j))


gugu(5)