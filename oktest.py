from konlpy.tag import Okt
okt = Okt();

text = '한글 자연어 처리는 제미있오 이제부터 시작해 볼까나';

print('-'*120)
print(okt.morphs(text))
print(okt.morphs(text, stem=True))
print('-'*120)
print(okt.nouns(text));
print(okt.phrases(text));
print('-'*120)
print(okt.pos(text))
print(okt.pos(text, join=True))
print(okt.pos(text, stem=True, join=True))
