def fake_large_file():
    for i in range(1_000_000):
        yield f"Line {i}"

for line in fake_large_file():
    if int(line.split()[1]) == 5:
        print(line)
        break

