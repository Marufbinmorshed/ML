text = "Hello

with open("unicode.txt", "w", encoding="utf-8") as f:
    f.write(text)

with open("unicode.txt", "r", encoding="utf-8") as f:
    print(f.read())
