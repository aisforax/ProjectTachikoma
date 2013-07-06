import nltk
from nltk.text import Text
from nltk.corpus import PlaintextCorpusReader
from nltk.probability import FreqDist

def extract_entity_names(t):
    entity_names = []
            
    if hasattr(t, 'node') and t.node:
        if t.node == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))
                    
    return entity_names

#corpus_root = "samples"
corpus_root = "abstracts"
text = PlaintextCorpusReader(corpus_root, '.*')

fd = FreqDist()

for fid in text.fileids():
    try:
        tagged_words = nltk.pos_tag(text.words(fid))
        chunked_words = nltk.ne_chunk(tagged_words, binary=True)

        for name in extract_entity_names(chunked_words):
            fd.inc(name)
    except Exception as e:
        print e

print fd.keys()[:50]
