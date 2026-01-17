from pathlib import Path

folder = Path("data")
file = folder / "info.txt"

folder.mkdir(exist_ok=True)

file.write_text("Pathlib is awesome!", encoding="utf-8")
print(file.read_text(encoding="utf-8"))
