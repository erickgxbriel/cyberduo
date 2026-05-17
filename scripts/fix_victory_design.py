import os

bp_path = '/home/gabriel/Downloads/64Gram Desktop/CyberDuo/lessons/0.0-boas-vindas.html'
gen_path = '/home/gabriel/Downloads/64Gram Desktop/CyberDuo/scripts/generate_lessons.py'

# 1. Update boilerplate HTML
with open(bp_path, 'r') as f:
    bp = f.read()

# We need to find the victory screen part.
# Previously we set it to:
old_victory = '''                    <div style="display: flex; flex-direction: column; gap: 0.8rem; width: 100%;">
                        <button class="check-btn active w-full" onclick="location.reload()" style="background: transparent; border: 2px solid var(--cyber-blue); color: var(--cyber-blue);">REINICIAR LIÇÃO</button>
                        ##NEXT_LESSON_BTN##
                        <button class="check-btn active w-full" onclick="window.location.href='../modules/modulo-00.html'" style="background: var(--cyber-blue); color: black;">VOLTAR AO MÓDULO</button>
                    </div>'''

new_victory = '''                    <div style="display: flex; flex-direction: column; gap: 1rem; width: 100%; align-items: center; margin-top: 1rem;">
                        ##NEXT_LESSON_BTN##
                        <div style="display: flex; gap: 1rem; width: 100%; max-width: 400px; margin-top: 0.5rem;">
                            <button class="check-btn" onclick="location.reload()" style="flex: 1; background: #161b22; border: 2px solid #30363d; color: #c9d1d9; box-shadow: 0 4px 0 #0d1117; padding: 0.8rem 0.5rem;">
                                <i class="fas fa-rotate-right mb-1 block text-lg"></i>
                                <span style="font-size: 0.75rem; display: block; margin-top: 4px;">REINICIAR</span>
                            </button>
                            <button class="check-btn" onclick="window.location.href='../modules/modulo-00.html'" style="flex: 1; background: #161b22; border: 2px solid var(--cyber-blue); color: var(--cyber-blue); box-shadow: 0 4px 0 rgba(0,255,255,0.2); padding: 0.8rem 0.5rem;">
                                <i class="fas fa-layer-group mb-1 block text-lg"></i>
                                <span style="font-size: 0.75rem; display: block; margin-top: 4px;">MÓDULOS</span>
                            </button>
                        </div>
                    </div>'''

if old_victory in bp:
    bp = bp.replace(old_victory, new_victory)
    print("Replaced victory container in boilerplate.")

with open(bp_path, 'w') as f:
    f.write(bp)

# 2. Update generate_lessons.py
with open(gen_path, 'r') as f:
    gen = f.read()

old_next = '''        next_btn = f\'\'\'<button class="check-btn active w-full" onclick="window.location.href=\\'../lessons/{next_lesson_filename}\\'" style="background: #00ff41; color: black; border-color: #00ff41;">PRÓXIMA LIÇÃO <i class="fas fa-arrow-right ml-2"></i></button>\'\'\''''
new_next = '''        next_btn = f\'\'\'<button class="check-btn active w-full" onclick="window.location.href=\\'../lessons/{next_lesson_filename}\\'" style="background: var(--cyber-green); color: black; border-color: var(--cyber-green); box-shadow: 0 4px 0 #008f20; font-size: 1.1rem; padding: 1.2rem; letter-spacing: 2px;">PRÓXIMA LIÇÃO <i class="fas fa-arrow-right ml-2"></i></button>\'\'\''''

if old_next in gen:
    gen = gen.replace(old_next, new_next)
    print("Replaced next button in generator.")

with open(gen_path, 'w') as f:
    f.write(gen)

# 3. Run generator
os.system('cd "/home/gabriel/Downloads/64Gram Desktop/CyberDuo/scripts" && python3 generate_lessons.py')
