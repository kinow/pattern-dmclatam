from pattern.en import parse, pprint
s = 'The DMC Latam 2013 was awesome! I loved it!'
s = parse(s, relations=True, lemmata=True)
pprint(s)