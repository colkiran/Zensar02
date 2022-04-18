
import re
st = "the quick brown fox jumps over the lazy dog"

print(f"st :{st}")

res= re.sub('the', 'The', st, 1)

print(f"res :{res}")

print("-" * 40)

st = """
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog. 
"""

for line in st.splitlines():
    res = re.sub("the", "The", line,1)
    print(res)

