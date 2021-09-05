
fileName = input()

file = open(fileName, "r")
content = file.read()
words = content.split()
print(words)
print(len(words))