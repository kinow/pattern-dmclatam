from pattern.search import search
from pattern.en import parsetree

strings = [
    'DMCLatam 2013 was awesome!', 
    'Bruno is not so smarty'
]

for s in strings: 
    t = parsetree(s)
    named_entities = search('NNP', t)
    adjectives = search('RB?+ JJ', t) 
    for named_entity in named_entities:
        print named_entity.string, '=>', adjectives[0].string
