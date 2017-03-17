import re
import requests

data = requests.get("http://kafeterya.metu.edu.tr/").text

foods = re.compile(r'''
    Öğle[ ]Yemeği</h3>\s+
    <div[ ]class="yemek">\s+
        <span>.+</span>\s+
        <p>(?P<midfirst>.+)</p>\s+
    </div><!.+>\s+
    <div[ ]class="yemek">\s+
        <span>.+</span>\s+
        <p>(?P<midsecond>.+)</p>\s+
    </div><!.+>\s+
    <div[ ]class="yemek">\s+
        <span>.+</span>\s+
        <p>(?P<midthird>.+)</p>\s+
    </div><!.+>\s+
    <div[ ]class="yemek">\s+
        <span>.+</span>\s+
        <p>(?P<midfourth>.+)</p>\s+
    </div><!.+>\s+
    </div><!.+>\s+
    <div[ ]style="clear:both"></div>\s+
    <div[ ]class="yemek-listesi">\s+
    <h3>Akşam[ ]Yemeği</h3>\s+
    <div[ ]class="yemek">\s+
        <span>.+</span>\s+
        <p>(?P<noonfirst>.+)</p>\s+
    </div><!.+>\s+
    <div[ ]class="yemek">\s+
        <span>.+</span>\s+
        <p>(?P<noonsecond>.+)</p>\s+
    </div><!.+>\s+
    <div[ ]class="yemek">\s+
        <span>.+</span>\s+
        <p>(?P<noonthird>.+)</p>\s+
    </div><!.+>\s+
    <div[ ]class="yemek">\s+
        <span>.+</span>\s+
        <p>(?P<noonfourth>.+)</p>\s+
    </div><!.+>\s+
    ''', re.VERBOSE | re.MULTILINE)

foodlist = re.search(foods, data).groups()
midmenu = []
noonmenu = []

for i in range(8):
    if i < 4:
        midmenu.append(foodlist[i])
    else:
        noonmenu.append(foodlist[i])

print("Öğlen: " + " .".join(midmenu))
print("Akşam: " + " ".join(noonmenu))
