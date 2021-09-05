import re

file = open("/Users/a5131082/PycharmProjects/DailyPython/resources/ben.txt", "r")
content = file.read()
words = content.split()
print(words)
print(len(words))