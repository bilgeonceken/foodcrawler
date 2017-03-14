import re
import subprocess

args = ["curl", "http://kafeterya.metu.edu.tr/" ">" "kaf.html"]

names_file = open("kaf.html", encoding="utf-8")

# puts all the contents of names into data
data = names_file.read()
# wipes the file out of memory
names_file.close()

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

print(midmenu)
print(noonmenu)
