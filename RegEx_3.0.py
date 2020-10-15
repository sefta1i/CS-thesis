import re

output = open("output.txt","w+")

with open('sagt_dict.txt') as infile:
    lexicon = infile.read()
    lexicon = lexicon.replace('\n', '|')
    #print(lexicon)

corpus = open("sagt_corpus.txt", "r")
text = corpus.read()
corpus.close()


nouns = r'('+lexicon+')'
#print(nouns)
#suffixes = r'(?P<suffix>(ler|lar)?(de|da)?(nin|nın|nün|nun)?)'
#print(suffixes)
#print(nouns+suffixes)

mixed = re.compile(nouns+r'(\')?(?P<suffix>(ler|lar)?((i|ı|u|ü|)?m|(i|ı|u|ü)?n|si|sı|su|sü|i|ı|u|ü|imiz|ımız|umuz|ümüz|miz|mız|mus|müz|iniz|ınız|unuz|ünüz|niz|nız|nuz|nüz|leri|ları)?(yi|yı|yu|yü|i|ı|u|ü)?(ye|ya|a|e)?(den|dan|ten|tan)?(de|da|te|ta)?(nin|nın|nün|nun)?(in|ın|un|ün)?)')
#mixed =(nouns+suffixes)
#print(mixed)
#match = re.findall(mixed,text)
#print (match)

count = 0

for match in re.finditer(mixed, text):
    if(match.group('suffix')):
        count +=1
        output.write(match.group()+"\n")
        print(match.group())

#expected amount of tokens
corpus = open("sagt_corpus.txt", "r")
line_count = 0.
for line in corpus:
    if line != "\n":
        line_count += 1.
corpus.close()

print("")
print("EXPECTED AMOUNT OF WORDS: ")
print(line_count)
print("AMOUNT OF FOUND MIXED WORDS: ")
print(count)
print("PRECISION :")
print(count/line_count)




