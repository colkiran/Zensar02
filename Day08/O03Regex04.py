
"""
st = "The quick brown fox jumps over the lazy dog"

re.search(r'fox', st)

three parts in our that we match with regex
1. string that did'nt match the regex.      -   "The quick brown "
2. string that matched the regex.           -   "fox"
3. string that was not checked by regex.    -   " jumps over the lazy dog"
"""
import re

st = "The quick brown fox jumps over the lazy dog"

res = re.search(r'(f\w+)', st)

if res:
    print("Match found....")
    print(f"string that did'nt match :{st[:res.start()]}")
    print(f"string that matched :{res.group(0)} \t {st[res.start():res.end()]}")
    print(f"string that is not checked :{st[res.end():]}")
else:
    print("Match not found....")


