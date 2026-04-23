import pathlib

p = pathlib.Path(r'C:\Users\haro\.openclaw\workspace\aws-saa-study\generate_questions.py')
c = p.read_text()

old = '     ("Static anycast IP addresses", True),'
new = '     [(\n     "Static anycast IP addresses", True),'

if old in c:
    c = c.replace(old, new)
    p.write_text(c)
    print("Fixed!")
else:
    print("Not found")
