import os
import glob
from bs4 import BeautifulSoup
import json

content_dir = '/home/gabriel/Documentos/dev/cyberduo/content'
lesson_file = '/home/gabriel/Documentos/dev/cyberduo/scripts/lesson_definitions.json'

with open(lesson_file, 'r') as f:
    lessons = json.load(f)

# Build a simple index of covered concepts from lesson definitions
covered_concepts = []
for l in lessons:
    if int(l['module']) <= 4:
        for step in l['steps']:
            if 'title' in step:
                covered_concepts.append(step['title'].lower())

files = glob.glob(os.path.join(content_dir, '[0-4].*.html'))
files.sort()

print("--- AUDIT: Modulos 0 a 4 ---")
for file in files:
    filename = os.path.basename(file)
    print(f"\nAnalyzing {filename}...")
    
    # These files are huge, we will parse them using string finding to avoid high memory or use a simple HTML parser
    # Let's read in chunks and just extract <h2> and <h3>
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        html_content = f.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    headers = soup.find_all(['h1', 'h2', 'h3'])
    
    missing = []
    found = []
    for h in headers:
        text = h.get_text(strip=True)
        if not text: continue
        
        # Check if any word from the header is in our covered concepts
        # This is a very rough heuristic
        is_covered = False
        words = set(text.lower().split())
        for c in covered_concepts:
            # If the concept title has overlap with the header
            if len(set(c.split()) & words) > 1:
                is_covered = True
                break
                
        if is_covered:
            found.append(text)
        else:
            missing.append(text)
            
    print(f"  Found {len(found)} headers matching concepts.")
    print(f"  Found {len(missing)} headers POTENTIALLY MISSING.")
    if missing:
        # print up to 5 missing to give us an idea
        for m in missing[:5]:
            print(f"    - {m}")
