import os
import re

bp_path = '/home/gabriel/Documentos/dev/cyberduo/lessons/0.0-boas-vindas.html'

with open(bp_path, 'r') as f:
    content = f.read()

# 1. Update CSS
old_container_css = '.match-container { display: flex; gap: 1rem; width: 100%; margin-top: 1rem; }'
new_container_css = '.match-container { display: grid; grid-template-columns: 1fr 1fr; gap: 0.6rem 1rem; width: 100%; margin-top: 1rem; }'

if old_container_css in content:
    content = content.replace(old_container_css, new_container_css)

old_column_css = '.match-column { flex: 1; display: flex; flex-direction: column; gap: 0.6rem; }'
new_column_css = '/* .match-column removed */'
if old_column_css in content:
    content = content.replace(old_column_css, new_column_css)

# Also ensure match-item handles height correctly in grid
old_item_css = '.match-item { background: #161b22; border: 2px solid #30363d; border-bottom-width: 4px; padding: 0.8rem; border-radius: 0.8rem; cursor: pointer; text-align: center; font-weight: 600; font-size: clamp(0.85rem, 3.5vw, 0.95rem); transition: all 0.1s; user-select: none; display: flex; align-items: center; justify-content: center; min-height: 60px; }'
new_item_css = '.match-item { background: #161b22; border: 2px solid #30363d; border-bottom-width: 4px; padding: 0.8rem; border-radius: 0.8rem; cursor: pointer; text-align: center; font-weight: 600; font-size: clamp(0.85rem, 3.5vw, 0.95rem); transition: all 0.1s; user-select: none; display: flex; align-items: center; justify-content: center; min-height: 60px; height: 100%; }'
if old_item_css in content:
    content = content.replace(old_item_css, new_item_css)

# 2. Update JS rendering logic
old_js = '''                        <div class="match-container">
                            <div class="match-column">
                                ${matchLeft.map((item, i) => `
                                    <div class="match-item" id="left-${i}" onclick="selectMatch('left', ${i}, ${item.id})">${item.text}</div>
                                `).join('')}
                            </div>
                            <div class="match-column">
                                ${matchRight.map((item, i) => `
                                    <div class="match-item" id="right-${i}" onclick="selectMatch('right', ${i}, ${item.id})">${item.text}</div>
                                `).join('')}
                            </div>
                        </div>'''

new_js = '''                        <div class="match-container">
                                ${matchLeft.map((item, i) => `
                                    <div class="match-item" id="left-${i}" onclick="selectMatch('left', ${i}, ${item.id})">${item.text}</div>
                                    <div class="match-item" id="right-${i}" onclick="selectMatch('right', ${i}, ${matchRight[i].id})">${matchRight[i].text}</div>
                                `).join('')}
                        </div>'''

if old_js in content:
    content = content.replace(old_js, new_js)
    print("Replaced JS grid logic.")
else:
    print("JS logic not found, might have different indentation.")
    # Fallback regex if indentation differs
    js_pattern = re.compile(r'<div class="match-container">.*?</div>\s*</div>\s*</div>', re.DOTALL)
    if js_pattern.search(content):
        content = js_pattern.sub(new_js, content)
        print("Replaced JS grid logic using regex.")

# The JS selectMatch has a querySelector that relies on match-column:
old_select = "document.querySelectorAll(`.match-column:nth-child(${side==='left'?1:2}) .match-item`).forEach"
new_select = "document.querySelectorAll(`.match-item[id^='${side}-']`).forEach"

if old_select in content:
    content = content.replace(old_select, new_select)
    print("Replaced selectMatch querySelector.")

with open(bp_path, 'w') as f:
    f.write(content)

os.system('cd "/home/gabriel/Documentos/dev/cyberduo/scripts" && python3 generate_lessons.py')
