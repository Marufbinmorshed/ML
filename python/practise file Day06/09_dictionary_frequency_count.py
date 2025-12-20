# Frequency count using dictionary
text = "python programming"
freq = {}

for ch in text:
    if ch == " ":
        continue
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for k, v in freq.items():
    print(k, "=>", v)
