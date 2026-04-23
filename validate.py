import json

data = json.load(open(r'C:\Users\haro\.openclaw\workspace\aws-saa-study\src\data\aws-saa-exam.json'))
print("Total questions:", len(data))
cats = {}
for q in data:
    c = q["category"]
    cats[c] = cats.get(c, 0) + 1
for c, n in sorted(cats.items()):
    print(f"  {c}: {n}")

errors = 0
for q in data:
    correct = [o for o in q["options"] if o["correct"]]
    if len(correct) != 1:
        errors += 1
        print("ERROR: Q" + str(q["id"]) + " has " + str(len(correct)) + " correct answers")
    if not q["explanation"]:
        errors += 1
    if not q["hint"]:
        errors += 1
print("Validation errors:", errors)
