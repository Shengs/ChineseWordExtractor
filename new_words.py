from wordseg import WordSegment, sequence

corpus = open(
    "doc/dictionary.txt", encoding="utf-8"
    ).read().splitlines()

news = open(
    "doc/news_0.txt", encoding="utf-8"
    ).read()


gened_words = []
new_words = []

ws = WordSegment(news, max_word_len=8, min_freq=0.00005, min_aggregation=50, min_entropy=0.8)
rs = ws.words
     
print("All gened words:", len(rs))

for i in rs:
        gened_words.append(i)
        if i not in corpus:
            new_words.append(i)

print("New ones:", len(new_words))

with open('new_words.txt', 'w') as ff:
    for item in new_words:
        ff.write(str(item) + '\n')
