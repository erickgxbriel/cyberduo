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
        'title': lesson['title'].split(' ')[0] + ' ' + ' '.join(lesson['title'].split(' ')[1:-1]) if len(lesson['title'].split(' ')) > 1 else lesson['title'], # remove the ' 10.2a' from title if exists
        'icon': lesson['steps'][0].get('icon', 'fa-book'),
        'desc': desc
    })

# Clean titles (some have the number at the end, e.g. "Protocolos e Ataques de Rede 5.1a")
for mod_num, items in modules.items():
    for item in items:
        title = item['title']
        item['title'] = re.sub(r'\s*\d+\.\d+[a-z]?$', '', title).strip()

modules_dir = '/home/gabriel/Downloads/64Gram Desktop/CyberDuo/modules'
for mod_file in glob.glob(os.path.join(modules_dir, 'modulo-*.html')):
    # Extract module number from filename
    m = re.search(r'modulo-(\d+)\.html', mod_file)
    if not m: continue
    mod_num = int(m.group(1))
    
    if mod_num not in modules: continue
    
    with open(mod_file, 'r') as f:
        html = f.read()
        
    # Generate new list
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
    new_list_html += '        </div>'
    
    # Replace content between <div class="submodule-list"> and </div>
    # Using regex to find the block
    new_html = re.sub(r'<div class="submodule-list">.*?</div>', new_list_html, html, flags=re.DOTALL)
    
    with open(mod_file, 'w') as f:
        f.write(new_html)
    
    print(f"Updated modulo-{mod_num:02d}.html with {len(modules[mod_num])} lessons")
