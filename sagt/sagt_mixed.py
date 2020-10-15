import sys
from io import open
from conllu import parse_incr

with open(sys.argv[1], 'r') as file:
    for sentence in parse_incr(file):
        for tokens in sentence:
            lang = tokens["misc"]
            upos = tokens["upos"]
            element = tokens["form"]

            if (lang["LangID"] == "MIXED"):
                index = element.index("§")
                print(element)
                #print(element[0:index-1])






