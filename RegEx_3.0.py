import re

corpus = []

output = open("output.txt","w+")

with open("text.txt", "r") as corpus:
    text = corpus.read().split()
    #print (text)


for i in text:
  match = re.compile(r"(Text|Glas|Buch|Tisch|Geschenk|Hallo)+(ler|lar|de|da|nin|nın|nün|nun)\b")
  result = match.search(i)

  if result is not None:
      output.write(i + "\n")
      print(result.group())


