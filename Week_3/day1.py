import requests

# url = "https://quotes.toscrape.com/"

# response = requests.get(url)

# if response.status_code == 200:
#     print("Successful fetch")
# else:
#     print(f"Failed:{response.status_code}")


from bs4 import BeautifulSoup

# soup = BeautifulSoup(response.text,"html.parser")

# print(soup)

# title = soup.find("div",class_="col-md-8")
# print(title.text.strip())

# quotes = soup.find_all("span",class_="text")
# print(quotes)

# for quote in quotes:
#     print(quote.text)

# quote = soup.find("div",class_="quote")
# print(quote)

# authors = soup.find_all("small",class_="author")
# for author in authors:
#     print(author.text)

# links = soup.find_all("a",class_="tag")
# for link in links:
#     print(link.h.strip())

# quote = soup.find("div",class_="quote")

# links = quote.find_all("a",class_="tag")
# for link in links:
#     print(link.text)
#     print(link["href"])

# quotes = soup.find_all("div",class_="quote")

# for quote in quotes:
#     tags = []
#     tags_title = []
#     links = quote.find_all("a",class_="tag")
#     for link in links:
#         tags_title.append(link.text)
#         tags.append(link["href"])

page = 1

while page <= 3:

    url = f"https://quotes.toscrape.com/page/{page}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    quotes = soup.find_all("div",class_="quote")
    for quote in quotes:
        print(quote.text)
    page += 1