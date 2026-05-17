import json
import re
import os
import glob

P='/home/gabriel/Downloads/64Gram Desktop/CyberDuo/scripts/lesson_definitions.json'
with open(P,'r') as f: L=json.load(f)

# Group lessons by module
modules = {}
for lesson in L:
    mod_num = int(lesson['module'])
    if mod_num not in modules:
        modules[mod_num] = []
    
    # extract number from filename (e.g. 10.2a)
    m = re.match(r'^(\d+\.\d+[a-z]?)-', lesson['filename'])
    number = m.group(1) if m else lesson['module']
    
    # extract first teach step content as desc
    desc = "Clique para acessar a lição."
    for step in lesson['steps']:
        if step['type'] == 'teach' or step['type'] == 'example':
            # Remove HTML tags and get first sentence
            clean_text = re.sub(r'<[^>]+>', '', step.get('content', step.get('scenario', '')))
            sentences = clean_text.split('.')
            if sentences[0]:
                desc = sentences[0].strip() + "."
                # Truncate if too long
                if len(desc) > 80:
                    desc = desc[:77] + "..."
            break
            
    modules[mod_num].append({
        'filename': lesson['filename'],
        'number': number,
        'title': lesson['title'].split(' ')[0] + ' ' + ' '.join(lesson['title'].split(' ')[1:-1]) if len(lesson['title'].split(' ')) > 1 else lesson['title'],
        'icon': lesson['steps'][0].get('icon', 'fa-book'),
        'desc': desc
    })

for mod_num, items in modules.items():
    for item in items:
        title = item['title']
        item['title'] = re.sub(r'\s*\d+\.\d+[a-z]?$', '', title).strip()

modules_dir = '/home/gabriel/Downloads/64Gram Desktop/CyberDuo/modules'
for mod_file in glob.glob(os.path.join(modules_dir, 'modulo-*.html')):
    m = re.search(r'modulo-(\d+)\.html', mod_file)
    if not m: continue
    mod_num = int(m.group(1))
    
    if mod_num not in modules: continue
    
    with open(mod_file, 'r') as f:
        html = f.read()
        
    new_list_html = '<div class="submodule-list">\n'
    for item in modules[mod_num]:
        new_list_html += f'''            
            <a href="../lessons/{item['filename']}" class="submodule-item">
                <div class="submodule-icon-box">
                    <i class="fas {item['icon']}"></i>
                </div>
                <div class="submodule-info">
                    <span class="submodule-number">{item['number']}</span>
                    <span class="submodule-title">{item['title']}</span>
                    <span class="submodule-desc">{item['desc']}</span>
                </div>
                <i class="fas fa-chevron-right submodule-arrow"></i>
            </a>
'''
    new_list_html += '        </div>\n\n    </main>'
    
    # Find everything before <div class="submodule-list">
    part1 = html.split('<div class="submodule-list">')[0]
    # Find everything after </main>
    part2 = html.split('</main>')[-1]
    
    new_html = part1 + new_list_html + part2
    
    with open(mod_file, 'w') as f:
        f.write(new_html)
    
    print(f"Fixed modulo-{mod_num:02d}.html with {len(modules[mod_num])} lessons")
