# Event participant tracker
events = {
    "Hackathon": ["A", "B", "C"],
    "Workshop": ["A", "D"]
}

for event, people in events.items():
    print(event, "Participants:", len(people))
