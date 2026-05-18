import os
import re
import json

bp_path = '/home/gabriel/Documentos/dev/cyberduo/lessons/0.0-boas-vindas.html'
gen_path = '/home/gabriel/Documentos/dev/cyberduo/scripts/generate_lessons.py'

# 1. Update boilerplate HTML
with open(bp_path, 'r') as f:
    bp = f.read()

# Update Match Derangement logic
old_match = '''                matchLeft = shuffle(step.pairs.map((p, i) => ({text: p.term, id: i})));
                matchRight = shuffle(step.pairs.map((p, i) => ({text: p.definition, id: i})));'''

new_match = '''                matchLeft = shuffle(step.pairs.map((p, i) => ({text: p.term, id: i})));
                
                let isDeranged = false;
                while (!isDeranged) {
                    matchRight = shuffle(step.pairs.map((p, i) => ({text: p.definition, id: i})));
                    isDeranged = true;
                    for (let j = 0; j < matchLeft.length; j++) {
                        if (matchLeft[j].id === matchRight[j].id) {
                            if (matchLeft.length > 1) {
                                isDeranged = false;
                                break;
                            }
                        }
                    }
                }'''

if old_match in bp:
    bp = bp.replace(old_match, new_match)
    print("Replaced Match derangement logic.")

# Update Victory Screen Buttons
old_victory = '''                    <button class="check-btn active w-full" onclick="window.location.href='../modules/modulo-00.html'" style="background: var(--cyber-blue); color: black;">FINALIZAR LIÇÃO</button>'''

new_victory = '''                    <div style="display: flex; flex-direction: column; gap: 0.8rem; width: 100%;">
                        <button class="check-btn active w-full" onclick="location.reload()" style="background: transparent; border: 2px solid var(--cyber-blue); color: var(--cyber-blue);">REINICIAR LIÇÃO</button>
                        ##NEXT_LESSON_BTN##
                        <button class="check-btn active w-full" onclick="window.location.href='../modules/modulo-00.html'" style="background: var(--cyber-blue); color: black;">VOLTAR AO MÓDULO</button>
                    </div>'''

if old_victory in bp:
    bp = bp.replace(old_victory, new_victory)
    print("Replaced Victory Screen buttons.")

with open(bp_path, 'w') as f:
    f.write(bp)

# 2. Update generate_lessons.py
with open(gen_path, 'r') as f:
    gen = f.read()

# I need to add 'next_lesson' logic.
# The definition is generate_lesson(filename, module_num, title, victory_msg, steps_json)
# I will change it to generate_lesson(filename, module_num, title, victory_msg, steps_json, next_lesson_filename)

old_def = 'def generate_lesson(filename, module_num, title, victory_msg, steps_json):'
new_def = 'def generate_lesson(filename, module_num, title, victory_msg, steps_json, next_lesson_filename=None):'
if old_def in gen:
    gen = gen.replace(old_def, new_def)

# Add replacement logic for ##NEXT_LESSON_BTN## inside generate_lesson
old_replace_back = '''    bp = bp.replace("'../modules/modulo-00.html'", f"'../modules/{mod_str}.html'")
    # Fix the second occurrence of back link in victory
    bp = bp.replace("FINALIZAR LIÇÃO", "VOLTAR AO MÓDULO")'''

new_replace_back = '''    bp = bp.replace("'../modules/modulo-00.html'", f"'../modules/{mod_str}.html'")
    
    if next_lesson_filename:
        next_btn = f\'\'\'<button class="check-btn active w-full" onclick="window.location.href=\\'../lessons/{next_lesson_filename}\\'" style="background: #00ff41; color: black; border-color: #00ff41;">PRÓXIMA LIÇÃO <i class="fas fa-arrow-right ml-2"></i></button>\'\'\'
        bp = bp.replace("##NEXT_LESSON_BTN##", next_btn)
    else:
        bp = bp.replace("##NEXT_LESSON_BTN##", "")
'''
if old_replace_back in gen:
    gen = gen.replace(old_replace_back, new_replace_back)
else:
    # Maybe already replaced? Or slightly different?
    # Actually, in generate_lessons.py the second replace was:
    pass

# Try to find exactly where to inject ##NEXT_LESSON_BTN##
if "##NEXT_LESSON_BTN##" not in gen:
    inject_point = "    outpath = os.path.join(LESSONS_DIR, filename)"
    injection = '''
    if next_lesson_filename:
        next_btn = f'<button class="check-btn active w-full" onclick="window.location.href=\\'../lessons/{next_lesson_filename}\\'" style="background: #00ff41; color: black; border-color: #00ff41;">PRÓXIMA LIÇÃO <i class="fas fa-arrow-right ml-2"></i></button>'
        bp = bp.replace("##NEXT_LESSON_BTN##", next_btn)
    else:
        bp = bp.replace("##NEXT_LESSON_BTN##", "")
'''
    gen = gen.replace(inject_point, injection + inject_point)

# Now update the main loop calling generate_lesson
old_call = '''        generate_lesson(
            lesson['filename'],
            lesson['module'],
            lesson['title'],
            lesson['victory_msg'],
            json.dumps(lesson['steps'], ensure_ascii=False, indent=12)
        )'''

new_call = '''        next_filename = definitions[i+1]['filename'] if i+1 < len(definitions) else None
        
        generate_lesson(
            lesson['filename'],
            lesson['module'],
            lesson['title'],
            lesson['victory_msg'],
            json.dumps(lesson['steps'], ensure_ascii=False, indent=12),
            next_filename
        )'''

# Need to change `for lesson in definitions:` to `for i, lesson in enumerate(definitions):`
if 'for lesson in definitions:' in gen:
    gen = gen.replace('for lesson in definitions:', 'for i, lesson in enumerate(definitions):')
    gen = gen.replace(old_call, new_call)
    print("Replaced main loop calling generator.")

with open(gen_path, 'w') as f:
    f.write(gen)

# 3. Run the generator
os.system('cd "/home/gabriel/Documentos/dev/cyberduo/scripts" && python3 generate_lessons.py')
