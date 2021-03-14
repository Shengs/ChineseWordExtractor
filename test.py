from wordseg import WordSegment, sequence

corpus = open(
    r"doc/dictionary.txt", encoding="utf-8"
    ).readlines()

news = open(
    r"doc/news_0.txt", encoding="utf-8"
    ).read()

# existing words count
print(len(corpus))

new_words = []

ws = WordSegment(news, max_word_len=3, min_aggregation=1, min_entropy=0.5)
rs = ws.genWords(news)

labels = [i.text for i in rs]
print(labels)
labels = sequence.dedup(labels)

for i in labels:
    if i not in corpus:
        corpus.append(i+ "\n")
        new_words.append(i)

with open('new_dict.txt', 'w') as f:
    for item in corpus:
        f.write(str(item) + '\n')

with open('new_words.txt', 'w') as ff:
    for item in new_words:
        ff.write(str(item) + '\n')



# 85581

#corpus 102554
#labels 16974
#newwords16973
