import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
reports = soup.find_all("div",class_="sc-666b6d83-0 jSTfiy")

for report in reports:
    headline = report.find("h2",class_="sc-9d830f2a-3 fWzToZ")
    summary = report.find("p",class_="sc-36e63c4d-0 kVgkhK")
    print(headline.text)
    print(summary.text)