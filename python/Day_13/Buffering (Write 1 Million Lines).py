with open("bigfile.txt", "w") as f:
    for i in range(1_000_000):
        f.write(f"Line {i}\n")

print("Done writing efficiently")
