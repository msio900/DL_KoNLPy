import re
from collections import Counter

import matplotlib.pyplot as plt
from konlpy.corpus import kolaw
from konlpy.tag import Okt
from wordcloud import WordCloud

doc = kolaw.open('constitution.txt').read()

def preprocessing(txt, okt, stop_words = [], remove_stopwords=False): #
    result = [];
    sub_txt = re.sub("[^가-힣ㄱ-ㅎㅏ-ㅣ\\s]", "", txt); # 한글 이외의 것은 다 제거해라!
    noun_txt = okt.nouns(sub_txt);
    if remove_stopwords:
        for token in noun_txt:
            if (not token in stop_words) and (len(token) >= 2):
                result.append(token);
    return result;

stop_words = ['은','\n','는','정','수', '그','제조'];
okt = Okt()
rdoc = [];

rdoc = preprocessing(doc, okt, stop_words, remove_stopwords=True)

print(len(rdoc))
print(rdoc)
cnt = Counter(rdoc);
cdoc = cnt.most_common(10);
print(cdoc)
ddoc = dict(cdoc) # 딕셔너리로 담음.
print(ddoc)

wc = WordCloud(background_color='white',
               font_path='NanumGothic.ttf',
               width=500, height=300).generate_from_frequencies(ddoc);
plt.Figure(figsize=(5,5));
plt.imshow(wc);
plt.axis('off');
plt.show();