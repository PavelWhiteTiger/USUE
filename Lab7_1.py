import codecs
import re

words = dict();

with codecs.open("./resources/lab7_1.txt", "r", "utf_8_sig") as myFile:
    lines = list(filter(lambda x: x != "", [line.strip() for line in myFile.readlines()]))
    for line in lines:
        line = re.sub("\\.*'*-*:*,*«*»*\"*\\?*!*", "", line).split(" ")
        for word in line:
            words[word.lower()] = words.get(word.lower(), 0) + 1

words = dict(reversed(sorted(words.items(), key=lambda item: item[1]), ))

for key in words:
    print(f"{key} - {words[key]}")
