from wordseg import WordSegment, sequence

corpus = open(
    "doc/dictionary.txt", encoding="utf-8"
    ).read().splitlines()

# corpus = [line.replace('\n', '') for line in corpus]

news = open(
    "doc/news_0.txt", encoding="utf-8"
    ).read()

# existing words count 85581

new_words = []

ws = WordSegment(news, max_word_len=8, min_freq=0.00005, min_aggregation=50, min_entropy=1)
# sg = ws.segSentence(news)
rs = ws.words

labels = sequence.dedup(rs)
        
print("All gened words", len(labels))

for i in labels:
    if i not in corpus:
        corpus.append(i)
        new_words.append(i)

print("new ones", len(new_words))

# with open('new_dict.txt', 'w') as f:
#     for item in corpus:
#         f.write(str(item) + '\n')

with open('new_words.txt', 'w') as ff:
    for item in new_words:
        ff.write(str(item) + '\n')

# with open('new_sg.txt', 'w') as ffy:
#     for item in sg:
#         ffy.write(str(item) + '\n')

# 85581

#corpus 102554
#labels 16974
#newwords16973
