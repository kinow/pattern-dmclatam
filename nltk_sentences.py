import nltk

sent_tokenizer=nltk.data.load('tokenizers/punkt/portuguese.pickle')
raw_text='O DMC Latam 2013 foi incrivel! Bom demais da conta!'
sentences=sent_tokenizer.tokenize(raw_text)
print "First sentence....: ", sentences[0]
print "Second sentence...: ", sentences[1]
