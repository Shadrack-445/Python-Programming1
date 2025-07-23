import requests
from bs4 import BeautifulSoup

url = "https://www.jumia.co.ke/huahua-huahua-new-type-of-travel-bag-large-capacity-multi-purpose-luggage-lightweight-311514425.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

title = soup.find("h1", class_="-fs20 -pts -pbxs")
price = soup.find("span", class_="-b -ubpt -tal -fs24 -prxs")
rating = soup.find("div", class_="stars _m _al")

brand = "" 
for div in soup.find_all("div", class_="-pvxs"):
    label = div.find("span", class_="-b -mrm")
    if label and label.text.strip() == "Brand: ":
        anchor = div.find("a",class_="_more")
        if anchor:
            brand = anchor.text.strip()
        break

print(title.text.strip())
print("Brand:", brand)
print("Price:", price.text.strip())
print("Rating:", rating.text.strip())






