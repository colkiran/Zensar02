
# mastering regular expression
import re

lcno = "LCNO-APN-70-2022-2320"
res = re.search(r'LCNO-(KAR|KER|TND|TEL|APN|MAH|GOA)-([0-6][1-9]|[1-7][0-3])-([2-9][0-9]{3})'
                r'-((?!0000)[0-9]{4})', lcno)

if res:
    print("Match found....")
    print(res.group(0))
else:
    print('Match not found......')