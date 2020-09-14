tuplearr=(1,23,56,2,1,42)
print( tuplearr[1])

#tuplearr[1]=10
#튜플은 수정이 불가.

#del(tuplearr)
#튜플 삭제
#print( tuplearr[1])

dic1= {}
dic1['이름']='아이오아이'
dic1['하이']='아이고허리야'
dic1['수박']='과일'
dic1['죽음']='death'

for k in dic1.keys():
    print("%s ----> %s" % (k,dic1[k]))