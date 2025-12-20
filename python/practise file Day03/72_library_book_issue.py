# Library book issue tracking
books = {
    "Python": [1, 0, 1],
    "ML": [0, 1, 1],
    "DS": [1, 1, 1]
}

for book, issues in books.items():
    count = 0
    for i in issues:
        if i == 1:
            count += 1
    print(book, "Issued:", count, "times")
