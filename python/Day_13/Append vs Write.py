# Write mode (overwrites file)
with open("log.txt", "w") as f:
    f.write("First line\n")

# Append mode (adds to file)
with open("log.txt", "a") as f:
    f.write("Second line\n")
