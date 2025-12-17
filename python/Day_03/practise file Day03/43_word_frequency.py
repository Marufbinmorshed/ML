# Word frequency counter
text = "python is easy and python is powerful"
words = text.split()
freq = {}

for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

for k, v in freq.items():
    print(k, ":", v)
