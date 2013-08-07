import nltk

stemmer = nltk.stem.RSLPStemmer()
s = stemmer.stem("copiar")
print 'Copiar stem...: ', s
s = stemmer.stem("Copiou")
print 'Copiou stem...: ', s