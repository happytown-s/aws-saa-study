import pathlib

p = pathlib.Path(r'C:\Users\haro\.openclaw\workspace\aws-saa-study\generate_questions.py')
c = p.read_text()

old = '     (\n     "Static anycast IP addresses", True),'
new = '     [\n     ("Static anycast IP addresses", True),'

if old in c:
    c = c.replace(old, new)
    p.write_text(c)
    print("Fixed!")
else:
    print("Pattern not found, checking...")
    idx = c.find('"Static anycast IP addresses"')
    if idx >= 0:
        print(f"Found at position {idx}")
        print(repr(c[idx-10:idx+60]))
    else:
        print("Not found at all")
