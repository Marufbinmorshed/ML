import json

data = {
    "name": "Maruf",
    "age": 25,
    "skills": ["Python", "Data Science"]
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)
