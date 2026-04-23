import json

p = r'C:\Users\haro\.openclaw\workspace\aws-saa-study\src\data\aws-saa-exam.json'
data = json.load(open(p))

for q in data:
    if q["id"] == 24:
        # Fix: Min size is the correct answer (option 1)
        q["options"][1]["correct"] = True
    elif q["id"] == 90:
        # Fix: S3 bucket policy is the correct answer (option 0)
        q["options"][0]["correct"] = True
    elif q["id"] == 192:
        # Fix: Only Private subnet should be correct (option 1)
        q["options"][3]["correct"] = False

json.dump(data, open(p, 'w'), indent=2, ensure_ascii=False)

# Validate again
errors = 0
for q in data:
    correct = [o for o in q["options"] if o["correct"]]
    if len(correct) != 1:
        errors += 1
        print("ERROR: Q" + str(q["id"]) + " has " + str(len(correct)) + " correct answers")
print("Validation errors:", errors)
