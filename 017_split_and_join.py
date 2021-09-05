def split_and_join(str_line):
    listStr = str_line.split(" ")
    return "-".join(listStr)

strInput = "This is a test"
print(split_and_join(strInput))
