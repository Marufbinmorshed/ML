# Online course rating
ratings = {
    "Python": [5, 4, 5, 5],
    "ML": [4, 4, 5],
    "DS": [5, 5, 4]
}

for course, rts in ratings.items():
    print(course, "Avg Rating:", sum(rts)/len(rts))
