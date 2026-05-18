import json
import re
import os
import glob

P='/home/gabriel/Documentos/dev/cyberduo/scripts/lesson_definitions.json'
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

# Clean titles
for mod_num, items in modules.items():
    for item in items:
        title = item['title']
        item['title'] = re.sub(r'\s*\d+\.\d+[a-z]?$', '', title).strip()

modules_dir = '/home/gabriel/Documentos/dev/cyberduo/modules'

# Função auxiliar para substituir o conteúdo da submodule-list de forma robusta
def replace_submodule_list(html, new_list_html):
    # Procurar o início da tag <div class="submodule-list">
    start_idx = html.find('<div class="submodule-list">')
    if start_idx == -1:
        return html
    
    # Encontrar a div de fechamento correspondente
    # Vamos contar os abridores e fechadores de <div> para achar o correto
    open_divs = 0
    end_idx = -1
    
    # Analisamos a string a partir do start_idx
    i = start_idx
    while i < len(html):
        if html[i:i+4] == '<div':
            open_divs += 1
            i += 4
        elif html[i:i+5] == '</div':
            open_divs -= 1
            if open_divs == 0:
                end_idx = i + 6 # inclui a tag </div>
                break
            i += 5
        else:
            i += 1
            
    if end_idx != -1:
        # Substitui a região inteira (do início da div list até seu fechamento exato)
        return html[:start_idx] + new_list_html + html[end_idx:]
    return html

for mod_file in glob.glob(os.path.join(modules_dir, 'modulo-*.html')):
    # Extract module number from filename
    m = re.search(r'modulo-(\d+)\.html', mod_file)
    if not m: continue
    mod_num = int(m.group(1))
    
    if mod_num not in modules: continue
    
    with open(mod_file, 'r') as f:
        html = f.read()
        
    # Generate new list HTML
    new_list_html = '<div class="submodule-list">\n'
    for item in modules[mod_num]:
        new_list_html += f'''            <a href="../lessons/{item['filename']}" class="submodule-item">
                <div class="submodule-icon-box">
                    <i class="fas {item['icon']}"></i>
                </div>
                <div class="submodule-info">
                    <span class="submodule-number">{item['number']}</span>
                    <span class="submodule-title">{item['title']}</span>
                    <span class="submodule-desc">{item['desc']}</span>
                </div>
                <i class="fas fa-chevron-right submodule-arrow"></i>
            </a>\n'''
    new_list_html += '        </div>'
    
    # Executa a substituição segura
    new_html = replace_submodule_list(html, new_list_html)
    
    with open(mod_file, 'w') as f:
        f.write(new_html)
    
    print(f"Updated modulo-{mod_num:02d}.html with {len(modules[mod_num])} lessons")
