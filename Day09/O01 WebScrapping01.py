
from bs4 import BeautifulSoup

with open("mypage.html", "r") as HTMLFILE:
    content = HTMLFILE.read()

    soup = BeautifulSoup(content, 'lxml')

    tag = soup.find("h5")
    print(f"tag :{tag}")

    print("-" * 40)

    tag_text = soup.find("h5").text
    print(tag_text)

    print("-" * 40)

    crdTitle = soup.findAll("h5")
    print(crdTitle)

    print("-" * 40)

    for ct in crdTitle:
        print(ct.text)