import re

corpus = []

output = open("output.txt","w+")

with open("text.txt", "r") as corpus:
    text = corpus.read().split()
    #print (text)


for i in text:
  match = re.search(r"(Text|Glas|Buch|Tisch|Geschenk|Hallo)+(ler|lar|de|da|nin|nın|nün|nun)\b", i)

  if match:
      output.write(i + "\n")
      print(match.group())
  else:
    continue


