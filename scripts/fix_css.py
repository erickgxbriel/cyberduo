import os
import re

bp_path = '/home/gabriel/Documentos/dev/cyberduo/lessons/0.0-boas-vindas.html'

with open(bp_path, 'r') as f:
    content = f.read()

# Replace .teach-highlight to include display: flex; gap: 0.6rem; align-items: center;
old_css = '.teach-highlight { background: rgba(0, 255, 65, 0.1); border-left: 3px solid var(--cyber-green); padding: 0.8rem; margin-top: 1rem; font-weight: 600; color: var(--cyber-green); border-radius: 0 0.5rem 0.5rem 0; }'
new_css = '.teach-highlight { display: flex; align-items: center; gap: 0.6rem; background: rgba(0, 255, 65, 0.1); border-left: 3px solid var(--cyber-green); padding: 0.8rem; margin-top: 1rem; font-weight: 600; color: var(--cyber-green); border-radius: 0 0.5rem 0.5rem 0; }'

if old_css in content:
    content = content.replace(old_css, new_css)
    print("Replaced .teach-highlight")
else:
    print("Old CSS not found, maybe already replaced?")

# Check for other mr-1, mr-2 usages that might need a global class
if '.mr-1' not in content:
    utility_classes = "\n        /* Utility Classes */\n        .mr-1 { margin-right: 0.25rem; }\n        .mr-2 { margin-right: 0.5rem; }\n        .mb-1 { margin-bottom: 0.25rem; }\n        .mb-2 { margin-bottom: 0.5rem; }"
    # Insert before .highlight-cyan
    content = content.replace('.highlight-cyan', utility_classes + '\n        .highlight-cyan')
    print("Added utility classes mr-1, mr-2")

with open(bp_path, 'w') as f:
    f.write(content)

os.system('cd "/home/gabriel/Documentos/dev/cyberduo/scripts" && python3 generate_lessons.py')
