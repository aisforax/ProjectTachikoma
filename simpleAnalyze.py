from nltk.text import Text
from nltk.probability import FreqDist
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords

import string

corpus_root = "abstracts"
wordlists = PlaintextCorpusReader(corpus_root, '.*')

all_words_list = []
for fid in wordlists.fileids():
    try:
        all_words_list += list(wordlists.words(fid))
    except Exception as e:
        print e

fd = FreqDist(Text([w.lower() for w in all_words_list]))

vocabulary = fd.keys()
clean_vocabulary = [ v for v in vocabulary if v not in stopwords.words("english") and v not in string.punctuation]

print clean_vocabulary[:50]

# TODOs:
# 1. Take care of non-meaningful words, like "1", ").", etc.
# 2. In the whole vocabulary, there are some words like "\x00", why?
