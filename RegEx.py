import re

corpus = []
words = []

output = open("output.txt","w+")

with open("text.txt", "r") as corpus:
    text = corpus.read().split()
    #print (text)

with open("ger_lex.txt", "r") as ger_words:
  words = ger_words.read().split()
  #print(words)


for i in text:
  #match = re.search(r"(Buch|Glas|Tisch)+(lar|ler)\b", i)
  match = re.search(r"\w+(ler|lar|de|da|nin|nın|nün|nun)\b", i)

  if match:
    #print(match.group())
    for x in words:
      if(match.group().startswith(x)):
        output.write(i+"\n")
        print (i)
      else:
        continue
  else:
    continue


#r = re.compile(".*(lar|ler)")
#newlist = list(filter(r.match, sentence)) # Read Note
#print(newlist)

#for i in newlist:
 #new = list(filter(r.match(),nouns))
 #print(new)

#match = re.search(r"(Buch|Glas|Tisch)+(lar|ler)\b",s)
#match = re.search(r"\w+(lar|ler)\b",s)

#print(match.group())

#________________________#
#regex = re.compile(r"\w+(lar|ler)\b")


