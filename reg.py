import re
import requests
from bs4 import BeautifulSoup as BS

soup = BS(requests.get("http://kafeterya.metu.edu.tr/").text, "lxml")

lunch = []
dinner = []
for index, food in list(enumerate(soup.select(".yemek-listesi p"))):
    if index < 4:
        lunch.append(food)
    else:
        dinner.append(food)

lunch = [str(l.contents).strip("[]'") for l in lunch]
dinner = [str(l.contents).strip("[]'") for l in dinner]
print("Lunch:  " + " ".join(lunch))
print("Dinner: " + " ".join(dinner))
