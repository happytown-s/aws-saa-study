import json

data = json.load(open(r'C:\Users\haro\.openclaw\workspace\aws-saa-study\src\data\aws-saa-exam.json'))

for q in data:
    if q["id"] in [24, 90, 192]:
        print("Q" + str(q["id"]) + ": " + q["category"])
        print("  Question: " + q["question"][:80])
        for i, o in enumerate(q["options"]):
            print("  Option " + str(i) + ": " + o["text"] + " -> correct=" + str(o["correct"]))
        print()
