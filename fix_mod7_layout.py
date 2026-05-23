import os
import re

files = [
    "7.0-introducao.html",
    "7.1a-cloud.html",
    "7.1b-configuracoes-nuvem.html",
    "7.2a-mobile.html",
    "7.2b-iot-virtualizacao.html"
]

for f in files:
    path = os.path.join("/home/gabriel/Documentos/dev/cyberduo/lessons", f)
    with open(path, "r") as f_obj:
        content = f_obj.read()
    
    # 1. Fix color: white to color: black in .check-btn.active
    content = content.replace("color: white; box-shadow: 0 4px 0 #1e3eb3;", "color: black; box-shadow: 0 4px 0 #1e3eb3;")
    content = content.replace("color: white; box-shadow: 0 4px 0 #008f20;", "color: black; box-shadow: 0 4px 0 #008f20;")
    
    # 2. Move X button to the right side of the header.
    # From: <div class="cursor-pointer"... onclick="window.location.href='../modules/modulo-07.html'"><i class="fas fa-times"></i></div>
    
    header_pattern = re.compile(
        r'(<div class="game-header">.*?)(<div class="cursor-pointer"[^>]*><i class="fas fa-times"></i></div>)(.*?<div class="hearts" id="heartsContainer"></div>\s*)</div>',
        re.DOTALL
    )
    
    match = header_pattern.search(content)
    if match:
        prefix = match.group(1)
        x_btn = match.group(2)
        middle = match.group(3)
        
        # Adjust margins: remove margin-left: -10px, add margin-left: 10px or margin-right: -10px
        x_btn = x_btn.replace('margin-left: -10px;', 'margin-left: 10px; margin-right: -10px;')
        
        new_header = prefix + middle + x_btn + '\n    </div>'
        content = content[:match.start()] + new_header + content[match.end():]
        
    with open(path, "w") as f_obj:
        f_obj.write(content)

print("Fixed layout defects and button positions.")
