from bs4 import BeautifulSoup
from collections import Counter
from nltk.corpus import stopwords
from nltk import LancasterStemmer
from urllib.request import urlopen
import nltk

nltk.download('punkt')

# 형태소 분류기 만들기
ls = nltk.LancasterStemmer()
soup = BeautifulSoup(urlopen("https://en.wikipedia.org/wiki/Data_science"), "html.parser")

# 텍스트를 추출하고 토큰화한다.
words = nltk.word_tokenize(soup.text)
print(words)

# 단어를 소문자 변환
words = [w.lower() for w in words]
print(words)

#불용어(the 같은것) 을 제거하고 단어의 형태소 추출 패스 nltk 패키지 문제

freqs= Counter(words)
print(freqs.most_common(10))
