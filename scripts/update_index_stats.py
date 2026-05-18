import json
import re

P = '/home/gabriel/Documentos/dev/cyberduo/scripts/lesson_definitions.json'
with open(P, 'r') as f:
    L = json.load(f)

# Calculate stats per module
stats = {}
for i in range(11):
    stats[str(i)] = {'lessons': 0, 'skills': 0}

for lesson in L:
    mod = str(int(lesson['module'])) # normalize '0', '01' to '0'
    if mod in stats:
        stats[mod]['lessons'] += 1
        stats[mod]['skills'] += len(lesson['steps'])

# Print stats to verify
for mod in range(11):
    m = str(mod)
    print(f"Módulo {m}: {stats[m]['lessons']} lições, {stats[m]['skills']} skills")

# Update index.html
index_file = '/home/gabriel/Documentos/dev/cyberduo/index.html'
with open(index_file, 'r') as f:
    html = f.read()

# We need to replace the module-stats div for each module card
# The modules are likely in order 0, 1, 2, ..., 10
# We can find them by looking for the href to modulo-XX.html

for mod in range(11):
    m_str = str(mod)
    m_pad = f"{mod:02d}"
    
    # Target href pattern: href="modules/modulo-XX.html" or similar
    # In index.html, it's usually inside an <a> tag. Let's find the block.
    # The structure is something like:
    # <a href="modules/modulo-01.html" class="module-card">
    # ...
    # <div class="module-stats"><span><i class="fas fa-book-open mr-1"></i> X Lições</span><span><i class="fas fa-microchip mr-1"></i> Y Skills</span></div>
    
    # We can use regex to find the module card and replace its stats
    # Regex: href="modules/modulo-01\.html".*?<div class="module-stats">.*?</div>
    
    lessons = stats[m_str]['lessons']
    skills = stats[m_str]['skills']
    
    if lessons == 0 and mod == 0:
        # Module 0 is usually static, maybe 1 lesson, 0 skills
        lessons = 1
        skills = 1 # or maybe keep it as 1 lição, 0 skills
        
    new_stats = f'<div class="module-stats"><span><i class="fas fa-book-open mr-1"></i> {lessons} Liç{"ões" if lessons != 1 else "ão"}</span><span><i class="fas fa-microchip mr-1"></i> {skills} Skills</span></div>'
    
    pattern = re.compile(rf'(href="modules/modulo-{m_pad}\.html".*?)<div class="module-stats">.*?</div>', re.DOTALL)
    
    # Replace in html
    html, count = pattern.subn(rf'\1{new_stats}', html)
    if count > 0:
        print(f"Updated HTML for module {mod}")
    else:
        print(f"Could not find block for module {mod}")

with open(index_file, 'w') as f:
    f.write(html)
