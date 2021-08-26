from collections import Counter

from konlpy.corpus import kolaw
from konlpy.tag import Okt



doc = kolaw.open('constitution.txt').read()
print(doc)

okt = Okt()

result = okt.nouns(doc);        # 명사형으로 분석
print(result)
cnt = Counter(result);          # count 세기
msrt = cnt.most_common(20);
dsrt = dict(msrt);
print(dsrt)