#!/usr/bin/env python3
"""
CyberDuo Lesson Generator - Phase 1+2 merged
Generates interactive Duolingo-style lessons from the 0.0 boilerplate.
"""
import os, json, re

LESSONS_DIR = os.path.join(os.path.dirname(__file__), '..', 'lessons')
BOILERPLATE = os.path.join(LESSONS_DIR, '0.0-boas-vindas.html')

# Module color map from CYBER_DUO_SKILL.md
COLORS = {
    '0': '#00ff41', '1': '#2d5af5', '2': '#ffb800', '3': '#00facd',
    '4': '#ff00ff', '5': '#ff8c00', '6': '#00f2ff', '7': '#e6edf3',
    '8': '#ff003c', '9': '#00ffa3', '10': '#8a2be2'
}

# Shadow colors for buttons (darker version of module color)
SHADOWS = {
    '0': '#008f20', '1': '#1a3fb3', '2': '#b38200', '3': '#009e80',
    '4': '#990099', '5': '#b36200', '6': '#00a8b3', '7': '#a0a8b0',
    '8': '#b3002a', '9': '#00b372', '10': '#5e1d80'
}

def get_boilerplate():
    with open(BOILERPLATE, 'r') as f:
        return f.read()

def generate_lesson(filename, module_num, title, victory_msg, steps_json, next_lesson_filename=None):
    """Generate a lesson HTML file from the boilerplate."""
    bp = get_boilerplate()
    color = COLORS.get(module_num, '#00f2ff')
    shadow = SHADOWS.get(module_num, '#008f20')
    mod_str = f'modulo-{module_num.zfill(2)}'
    
    # Replace color
    bp = bp.replace('--cyber-blue: #00ff41', f'--cyber-blue: {color}')
    # Replace shadow in button
    bp = bp.replace('#008f20', shadow)
    # Replace back link
    bp = bp.replace("'../modules/modulo-00.html'", f"'../modules/{mod_str}.html'")
    # Replace title
    bp = bp.replace('<title>CyberDuo - Bem-vindo ao Curso 0.0</title>', f'<title>CyberDuo - {title}</title>')
    # Replace steps array
    old_steps_match = re.search(r'const steps = \[.*?\];', bp, re.DOTALL)
    if old_steps_match:
        bp = bp[:old_steps_match.start()] + f'const steps = {steps_json};' + bp[old_steps_match.end():]
    # Replace victory
    bp = bp.replace('BEM-VINDO AO TIME!', victory_msg)
    bp = bp.replace('Você completou o treinamento inicial e dominou as bases da Segurança Ofensiva.', f'Você completou esta lição com sucesso!')
    bp = bp.replace("'../modules/modulo-00.html'", f"'../modules/{mod_str}.html'")
    
    if next_lesson_filename:
        next_btn = f'''<button class="check-btn active w-full" onclick="window.location.href=\'../lessons/{next_lesson_filename}\'" style="background: var(--cyber-green); color: black; border-color: var(--cyber-green); box-shadow: 0 4px 0 #008f20; font-size: 1.1rem; padding: 1.2rem; letter-spacing: 2px;">PRÓXIMA LIÇÃO <i class="fas fa-arrow-right ml-2"></i></button>'''
        bp = bp.replace("##NEXT_LESSON_BTN##", next_btn)
    else:
        bp = bp.replace("##NEXT_LESSON_BTN##", "")

    
    outpath = os.path.join(LESSONS_DIR, filename)
    with open(outpath, 'w') as f:
        f.write(bp)
    print(f"  ✅ {filename}")

def main():
    print("🚀 CyberDuo Lesson Generator")
    print("=" * 50)
    
    # Load lesson definitions from JSON
    defs_path = os.path.join(os.path.dirname(__file__), 'lesson_definitions.json')
    with open(defs_path, 'r') as f:
        definitions = json.load(f)
    
    for i, lesson in enumerate(definitions):
        next_filename = definitions[i+1]['filename'] if i+1 < len(definitions) else None
        
        generate_lesson(
            lesson['filename'],
            lesson['module'],
            lesson['title'],
            lesson['victory_msg'],
            json.dumps(lesson['steps'], ensure_ascii=False, indent=12),
            next_filename
        )
    
    print(f"\n✅ Generated {len(definitions)} lessons!")

if __name__ == '__main__':
    main()
