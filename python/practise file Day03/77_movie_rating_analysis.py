# Movie rating analysis
ratings = {
    "Movie A": [4,5,5,3],
    "Movie B": [3,4,2,4],
    "Movie C": [5,5,4,5]
}

for movie, rates in ratings.items():
    total = 0
    for r in rates:
        total += r
    avg = total / len(rates)
    print(movie, "Average Rating:", avg)
