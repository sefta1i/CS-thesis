import re

output = open("output.txt","w+")

with open('ger_lex.txt') as infile:
    lexicon = infile.read()
    lexicon = lexicon.replace('\n', '|')
    #print(lexicon)

corpus = open("text.txt", "r")
text = corpus.read()
corpus.close()

nouns = r'('+lexicon+')'
#print(nouns)
#suffixes = r'(?P<suffix>(ler|lar)?(de|da)?(nin|nın|nün|nun)?)'
#print(suffixes)
#print(nouns+suffixes)

mixed = re.compile(nouns+r'(?P<suffix>(ler|lar)?(de|da)?(nin|nın|nün|nun)?)')
#mixed =(nouns+suffixes)
#print(mixed)
#match = re.findall(mixed,text)
#print (match)

for match in re.finditer(mixed, text):
    if(match.group('suffix')):
        output.write(match.group()+"\n")
        print(match.group())






