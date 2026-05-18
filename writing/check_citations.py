import re

with open('/Users/baltaymarci/Documents/Feel Good AI/Analysis/writing/article_current.md', 'r') as f:
    text = f.read()

bib_start = text.find('Bibliography')
body = text[:bib_start]
bib = text[bib_start:]

# Find all citations in brackets like [Author et al., 2020] or [Author, 2020]
in_text_citations = re.findall(r'\[(.*?)\]', body)
# also look for "Author et al. (2020)"
in_text_citations2 = re.findall(r'([A-Z][a-z]+(?: et al\.)? \(\d{4}\))', body)

cites = set()
for c in in_text_citations:
    # Handle multiple citations in one bracket separated by ';'
    parts = [p.strip() for p in c.split(';')]
    for p in parts:
        if re.search(r'\d{4}', p):
            cites.add(p)

for c in in_text_citations2:
    cites.add(c)

missing = []
for c in cites:
    # Just check if the first word or two is in the bibliography
    author = c.split()[0].replace(',', '')
    if author not in bib:
        missing.append(c)

print("Potential missing citations:")
for m in sorted(missing):
    print(m)

