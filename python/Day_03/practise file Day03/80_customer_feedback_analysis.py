# Customer feedback analysis
feedback = ["good", "bad", "excellent", "good", "bad", "good"]
summary = {}

for f in feedback:
    if f in summary:
        summary[f] += 1
    else:
        summary[f] = 1

for k, v in summary.items():
    print(k, ":", v)
