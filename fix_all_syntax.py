import pathlib, re

p = pathlib.Path(r'C:\Users\haro\.openclaw\workspace\aws-saa-study\generate_questions.py')
c = p.read_text()

# Fix pattern: missing [ before first option in add_q call
# Pattern: add_q(N, "cat",\n     "question",\n     ( without [
# We need to find lines that start with '     (' after a question string

lines = c.split('\n')
fixed = 0
i = 0
while i < len(lines):
    # Look for pattern: add_q call followed by "question", then (option instead of [(option
    if lines[i].strip().startswith('add_q('):
        # Find the question line (should have closing ",)
        j = i + 1
        while j < len(lines) and not lines[j].strip().endswith('",'):
            j += 1
        # Next line should start options with [
        if j + 1 < len(lines):
            opt_line = lines[j + 1]
            # Check if it's an option tuple without opening bracket
            stripped = opt_line.strip()
            if stripped.startswith('("') or stripped.startswith("('") or stripped.startswith('("'):
                # Check if this is indeed an option (has True or False)
                if 'True),' in opt_line or 'False),' in opt_line:
                    lines[j + 1] = opt_line.replace('     (', '     [(', 1)
                    fixed += 1
    i += 1

result = '\n'.join(lines)
p.write_text(result)
print(f"Fixed {fixed} instances")
