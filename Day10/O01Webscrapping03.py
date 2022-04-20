
from bs4 import BeautifulSoup
import requests
from prettytable import PrettyTable

for i in range(1, 5):
    htmlText = requests.get("https://www.flipkart.com/search?q=smart+watches+samsung&otracker=search&otracker1="
                            "search&marketplace=FLIPKART&as-show=on&as=off&page=" + str(i))

    soup = BeautifulSoup(htmlText.text, 'lxml')

    pTbl = PrettyTable(["product", "price"])

    results = soup.findAll("div", class_="_3pLy-c row")
    for result in results:
        prod = result.find("div", class_="_4rR01T")
        price = result.find("div", class_="_30jeq3 _1_WHN1")

        if prod != None:
            pTbl.add_row([prod.text, price.text])


    pTbl.align["product"] = "l"
    pTbl.align["price"] = "r"

    print(pTbl)


    #     print(f"{prod.text} ")
    #
    # if price != None:
    #     print(f"{price.text}")

# for result in results1:
#     price = result.find("div", class_="_30jeq3 _1_WHN1")
#
#     # if price != None:
#     print(f"{price}")