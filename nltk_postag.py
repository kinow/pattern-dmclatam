import nltk

pos_tagged = nltk.pos_tag(nltk.word_tokenize("DMC Latam 2013 was awesome dude! Bruno said."))
print 'Sentence with Part Of Speech tags\n'

for t in pos_tagged:
    print t
    
