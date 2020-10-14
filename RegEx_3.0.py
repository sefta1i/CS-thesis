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

mixed = re.compile(nouns+r'(?P<suffix>(ler|lar)?((i|ı|u|ü|)?m|(i|ı|u|ü)?n|si|sı|su|sü|i|ı|u|ü|imiz|ımız|umuz|ümüz|miz|mız|mus|müz|iniz|ınız|unuz|ünüz|niz|nız|nuz|nüz|leri|ları)?(yi|yı|yu|yü)?(ye|ya)?(den|dan|ten|tan)?(de|da|te|ta)?(nin|nın|nün|nun)?(in|ın|un|ün)?)')
#mixed =(nouns+suffixes)
#print(mixed)
#match = re.findall(mixed,text)
#print (match)

for match in re.finditer(mixed, text):
    if(match.group('suffix')):
        output.write(match.group()+"\n")
        print(match.group())






