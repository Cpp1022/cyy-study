from gensim.models import Word2Vec
import jieba.posseg as pseg

sentences=[]
path=r"./label-RemoveTime-cut.txt"
output=r"./label-RemoveTime-word2vec.txt"

def skip_some_char(sentences):
    flag=0
    skip_list = [' ', '\n', '=*', '.......','','，','。','/']
    for skip_char in skip_list:
        if sentences == skip_char:
            sentences = ''
            flag=1
    
    return sentences,flag

# sentences = sentences.replace(skip_char, "")  

def saveTxt(txt_name,content):
    f=open(txt_name,'a',encoding="utf-8")
    f.write(content)
    f.close()
wordlist=[]
for line in open(path, 'r', encoding='UTF-8'):
    line=line[:-2]
    # print(line)
    content=line.split( )
    con_char=[]
    for i in range (len(content)):
        content[i],flag=skip_some_char(content[i])
        wordlist.append(content[i])
        if flag==0:
           con_char.append(content[i])
        # print(con_char)
    # print(con_char)
    sentences.append(con_char)
    # print(sentences)    
model = Word2Vec(sentences,vector_size=10,sg=0, min_count=1)
# Word2Vec(sentences=None, corpus_file=None, vector_size=100, alpha=0.025, window=5, min_count=5, max_vocab_size=None, sample=0.001, seed=1, workers=3, min_alpha=0.0001, sg=0, hs=0, negative=5, ns_exponent=0.75, cbow_mean=1, hashfxn=hash, epochs=5, null_word=0, trim_rule=None, sorted_vocab=1, batch_words=MAX_WORDS_IN_BATCH, compute_loss=False, callbacks=(), comment=None, max_final_vocab=None, shrink_windows=True)
model.train(sentences, total_examples=len(sentences), epochs=1)

for word in wordlist:
    vector = model.wv[word]
    print(word,vector)
sims = model.wv.most_similar('检查单', topn=10)  # get other similar words
print(sims)