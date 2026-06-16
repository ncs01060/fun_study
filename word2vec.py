import re
from lxml import etree
from nltk.tokenize import word_tokenize, sent_tokenize

path = "./data"
targetText = etree.parse(open(path+"data.xml","r",encoding="UTF-8"))
parseText = "\n".join(targetText.xpath("//content/text()"))

# 데이터 전처리
contentText = re.sub('\([^)]*\)', '', parseText)
# 문장 단위 토큰화 
sentText = sent_tokenize(contentText)


# 대문자 => 소문자, 구두점 제거 (영문, 숫자 제외)
normalizedText = [] 
for sent in sentText: 
    tokens = re.sub("[^a-z0-9]+"," ",sent.lower())
    normalizedText.append(tokens)
result = [ word_tokenize(s) for s in normalizedText ]
