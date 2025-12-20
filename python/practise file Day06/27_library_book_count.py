# Library book count by category
library = {
    "Science": ["Phy", "Chem", "Bio"],
    "Arts": ["History", "Civics"],
    "IT": ["Python", "Java", "ML"]
}

for category, books in library.items():
    print(category, "Books Count:", len(books))
