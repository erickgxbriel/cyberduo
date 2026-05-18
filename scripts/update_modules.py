import json
import re
import os
import glob

P='/home/gabriel/Documentos/dev/cyberduo/scripts/lesson_definitions.json'
with open(P,'r') as f: L=json.load(f)

CUSTOM_DESCRIPTIONS = {
    # Módulo 1
    "1.0-introducao.html": "Visão geral do módulo e objetivos principais sobre segurança ofensiva.",
    "1.1-hacking-etico.html": "Conceitos fundamentais, ética profissional, legalidade e conduta em testes.",
    "1.2-metodologias.html": "Estudo das principais metodologias de pentest: OSSTMM, OWASP e PTES.",
    "1.3-laboratorio-proprio.html": "Guia prático para montar seu próprio laboratório de testes em ambiente seguro.",
    # Módulo 2
    "2.0-introducao.html": "Entendimento dos objetivos, escopo e requisitos legais do planejamento.",
    "2.1-governanca-grc.html": "Fundamentos de Governança, Risco e Conformidade (GRC) aplicados.",
    "2.2-escopo-necessidades.html": "Definição de escopo, regras de engajamento e limitações de teste.",
    "2.3-mentalidade-etica.html": "Desenvolvimento da postura profissional e ética durante o engajamento.",
    # Módulo 3
    "3.0-introducao.html": "Conceitos básicos de coleta de informações e inteligência de ameaças.",
    "3.1-osint.html": "Técnicas e ferramentas para automação de coleta de dados públicos expostos.",
    "3.2-reconhecimento.html": "Varredura ativa, enumeração de serviços, portas e descoberta de hosts na rede.",
    "3.3-varredura-vulnerabilidade.html": "Uso de ferramentas automatizadas para mapeamento de falhas de segurança.",
    "3.4-analise-resultados.html": "Triagem de falso-positivos e classificação de riscos encontrados.",
    # Módulo 4
    "4.0-introducao.html": "Conceitos básicos do elo mais fraco e vetores de ataque humano.",
    "4.1-pretexting.html": "Criação de cenários convincentes e pretextos para manipulação.",
    "4.2-ataques-sociais.html": "Execução de campanhas de Phishing, Spear Phishing e Vishing.",
    "4.3-ataques-fisicos.html": "Técnicas de intrusão física, tailgating, dumpster diving e badges.",
    "4.4-ferramentas-sociais.html": "Exploração do Social-Engineer Toolkit (SET) e clonagem de páginas.",
    "4.5-metodos-influencia.html": "Gatilhos mentais, autoridade, escassez e psicologia de influência.",
    # Módulo 5
    "5.0-introducao.html": "Visão geral de ataques a redes internas, servidores e links wireless.",
    "5.1-vulnerabilidades-rede.html": "Ataques MITM, ARP Spoofing, LLMNR Poisoning e exploração de Kerberos.",
    "5.2-wireless.html": "Quebra de redes sem fio WPA/WPA2, ataques a WPS e criação de Rogue APs.",
    # Módulo 6
    "6.0-introducao.html": "Fundamentos do protocolo HTTP, arquitetura web e a superfície de ataque.",
    "6.1-owasp-top10.html": "Estudo detalhado das falhas críticas listadas no OWASP Top 10.",
    "6.2-lab-setup.html": "Configuração do proxy Burp Suite e ambiente de testes para aplicações web.",
    "6.3-logica-negocio.html": "Identificação de falhas de lógica, manipulação de fluxos e parâmetros.",
    "6.4-injecao-web.html": "Vetores de injeção como SQL Injection (SQLi) e Command Injection.",
    "6.5-autenticacao.html": "Quebra de autenticação, força bruta, e sequestro de sessão (Hijacking).",
    "6.6-autorizacao.html": "Falhas de controle de acesso (BAC) e Insecure Direct Object Reference (IDOR).",
    "6.7-xss.html": "Cross-Site Scripting (XSS) Refletido, Armazenado e baseado em DOM.",
    "6.8-csrf-ssrf.html": "Falsificação de requisições client-side (CSRF) e server-side (SSRF).",
    "6.9-clickjacking.html": "Manipulação de iframes, sobreposição visual e desativação de proteções.",
    "6.10-configuracao.html": "Diretórios expostos, cabeçalhos inseguros e configurações padrão de fábrica.",
    "6.11-file-inclusion.html": "Local (LFI) e Remote (RFI) File Inclusion e Path Traversal.",
    "6.12-codigo-inseguro.html": "Buffer overflows em C/C++, desserialização e lógica insegura web.",
    # Módulo 7
    "7.0-introducao.html": "Fundamentos da arquitetura cloud, IoT e sistemas industriais.",
    "7.1-cloud.html": "Enumeração, falhas de IAM, buckets vazados e exploração de metadados em nuvem.",
    "7.2-sistemas-especiais.html": "Análise mobile (MobSF/Frida), falhas em IoT e redes SCADA/embarcados.",
    # Módulo 8
    "8.0-introducao.html": "Conceitos de escalação de privilégios locais e técnicas pós-comprometimento.",
    "8.1-persistencia.html": "Instalação de web shells, backdoors persistentes e modificação de serviços.",
    "8.2-lateral-exfiltracao.html": "Técnicas de movimentação lateral, pivoting de rede e exfiltração segura.",
    # Módulo 9
    "9.0-introducao.html": "A importância da documentação e da tradução técnica para executivos.",
    "9.1-componentes-relatorio.html": "Sumário executivo, descrição técnica e classificação CVSS/critério.",
    "9.2-analise-recomendacoes.html": "Elaboração de planos de mitigação e contramedidas recomendadas.",
    "9.3-comunicacao-escalonamento.html": "Apresentação de resultados, diplomacia e reporte de falhas críticas.",
    "9.4-atividades-pos-entrega.html": "Testes de revalidação (re-testing), retenção de dados e encerramento.",
    # Módulo 10
    "10.0-introducao.html": "Fundamentos de automação de testes e customização de ferramentas.",
    "10.1-scripts.html": "Lógica de programação com Bash e Python para automação de tarefas em pentest.",
    "10.2-ferramentas.html": "Exploração aprofundada de ferramentas de Recon, Quebra de Hashes, C2 e Forense."
}

# Group lessons by module
modules = {}
for lesson in L:
    mod_num = int(lesson['module'])
    if mod_num not in modules:
        modules[mod_num] = []
    
    # extract number from filename (e.g. 10.2a)
    m = re.match(r'^(\d+\.\d+[a-z]?)-', lesson['filename'])
    number = m.group(1) if m else lesson['module']
    
    # extract description
    filename = lesson['filename']
    if filename in CUSTOM_DESCRIPTIONS:
        desc = CUSTOM_DESCRIPTIONS[filename]
    else:
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
        'title': lesson['title'],
        'icon': lesson['steps'][0].get('icon', 'fa-book'),
        'desc': desc
    })

# Clean and sort lessons inside each module
def sort_key(item):
    match = re.match(r'^(\d+)\.(\d+)([a-z]*)', item['number'])
    if match:
        major = int(match.group(1))
        minor = int(match.group(2))
        suffix = match.group(3)
        return (major, minor, suffix)
    return (0, 0, '')

for mod_num, items in modules.items():
    for item in items:
        title = item['title']
        item['title'] = re.sub(r'\s*\d+\.\d+[a-z]?$', '', title).strip()
    # Sort items based on logical lesson order (e.g., 3.0 -> 3.1a -> 3.2a -> 3.3)
    items.sort(key=sort_key)

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
