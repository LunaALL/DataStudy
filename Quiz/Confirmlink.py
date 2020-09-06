import urllib.request

url =str(input("링크를 입력해주쇼 "))
try:
    with urllib.request.urlopen(url) as doc:
     html=doc.read()

except:
    print("링크가 절단되어 있는 링크입니다. -> %s " % url)



