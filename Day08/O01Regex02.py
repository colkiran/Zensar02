
import re

# st = "The quick brown fox jumps over the lazy dog"

# res = re.search(r'\w+', st)   -   alpha numeric data
# res = re.search(r'\W+', st)   -   special characters
# res = re.search(r'\s+', st)   -   spaces
# res = re.search(r'\S+', st)   -   everything other than spaces
# res = re.search(r'\d+', st)   -   Numeric data
# res = re.search(r'\D+', st)   -   non numeric data
# res = re.search(r'(\ba\w+)', st, re.I)    -   word boundary
# res = re.search(r'(\Ba\w+)', st, re.I)
# res = re.search(r'(\Athis)', st, re.I)

st = "this is a sAmple amPle string"

res = re.search(r'(string\Z)', st, re.I)

if res:
    print(res.group(0))
    print("Match found....")
else:
    print('Match not found......')