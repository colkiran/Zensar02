
from bs4 import BeautifulSoup

with open("mypage.html", "r") as HTMLFILE:
    content = HTMLFILE.read()

    soup = BeautifulSoup(content, "lxml")

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

    print("-" * 40)

    test = soup.find("p")
    print(test)

    print("-" * 40)

    crd_txt = soup.findAll("p")
    for ct in crd_txt:
        print(ct.text)

    print("-" * 40)

    cards = soup.findAll('div', class_="card")
    for card in cards:
        crd_title = card.h5.text
        prc = card.a.text.split()[-1]

        print(f"Training on {crd_title} will cost {prc}")
