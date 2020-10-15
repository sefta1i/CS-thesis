import sys
from io import open
from conllu import parse_incr

with open(sys.argv[1], 'r') as file:
    for sentence in parse_incr(file):
        print(sentence)
        # first_token = sentence[0]
        # print(first_token)
        # print(first_token["upos"])
