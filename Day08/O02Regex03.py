
"""
Backtracking
recall the regex that is already present
recalling depends in grouping (grouping number)
not only matches the regex but also the data

"""
import re

st = "good blood bad blood"

res = re.search(r'(\w+)\s(\w+)\s(\w+)\s(\2)', st)

if res:
    print("Match found...")
    print(res.group(0))             # prints the entire string that matched the regex
    print(res.group(1))
    print(res.group(2))
    print(res.group(3))
    print(res.group(4))
else:
    print("Match not found....")