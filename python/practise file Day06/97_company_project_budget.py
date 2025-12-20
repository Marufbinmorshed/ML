# Company project budget
projects = {
    "ProjA": [20000, 25000],
    "ProjB": [30000, 35000]
}

for proj, costs in projects.items():
    print(proj, "Total Budget:", sum(costs))
