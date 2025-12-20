# Movie collection dictionary
movies = {
    "Action": ["Movie1", "Movie2"],
    "Comedy": ["Movie3"],
    "Drama": ["Movie4", "Movie5", "Movie6"]
}

for genre, names in movies.items():
    print(genre)
    for n in names:
        print(" -", n)
