from pattern.en import parsetree
from pattern.search import search
s = 'The DMC Latam 2013 was awesome! I loved it!'
t = parsetree(s, relations=True, lemmata=True)
for match in search('NP (CD)? be JJ', t):
    print match.constituents()[-1], "=>", match.constituents()[0]