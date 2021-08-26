from sklearn.feature_extraction.text import TfidfVectorizer

doc1 = 'She likes python';

doc2 = 'She hates python';

tfv = TfidfVectorizer();
result = tfv.fit_transform([doc1, doc2]).toarray(); # 단어를 벡터형태로

print(tfv.vocabulary_)
print(result)