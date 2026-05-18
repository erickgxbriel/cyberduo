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
    "3.1a-osint-busca.html": "Técnicas de OSINT para buscas eficientes de dados públicos expostos.",
    "3.1b-osint-ferramentas.html": "Exploração de ferramentas para automação de coleta OSINT.",
    "3.2a-recon-ativo-rede.html": "Técnicas de varredura ativa e descoberta de hosts em redes.",
    "3.2b-enumeracao-servicos.html": "Identificação de portas abertas, serviços e versões ativas.",
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
    "5.1a-protocolos-ataques.html": "Ataques a protocols de rede como ARP spoofing, DHCP starvation e DNS.",
    "5.1b-senhas-kerberos.html": "Exploração do protocolo Kerberos, Kerberoasting e quebra de senhas.",
    "5.2a-wireless-fundamentals.html": "Estrutura física de redes sem fio, espectro de rádio e criptografias.",
    "5.2b-wireless-attacks.html": "Quebra de chaves WPA/WPA2, ataques a WPS e criação de Rogue APs.",
    # Módulo 6
    "6.0-introducao.html": "Fundamentos do protocolo HTTP, arquitetura web e a superfície de ataque.",
    "6.1a-owasp-top10-1.html": "Estudo detalhado das primeiras falhas críticas listadas no OWASP Top 10.",
    "6.1b-owasp-top10-2.html": "Análise das falhas restantes e vetores de risco emergentes da OWASP.",
    "6.2-lab-setup.html": "Configuração do proxy Burp Suite e ambiente de testes para aplicações web.",
    "6.3-logica-negocio.html": "Identificação de falhas de lógica, manipulação de fluxos e parâmetros.",
    "6.4-injecao-web.html": "Vetores de injeção como SQL Injection (SQLi) e Command Injection.",
    "6.5-autenticacao.html": "Bypass de login, força bruta, session fixation e falhas de JWT.",
    "6.6-autorizacao.html": "Falhas de IDOR (Broken Object Level Authorization) e controle de acesso.",
    "6.7-xss.html": "Cross-Site Scripting Refletido, Armazenado e baseado em DOM.",
    "6.8-csrf-ssrf.html": "Ataques de falsificação de requisições do lado do cliente (CSRF) e servidor (SSRF).",
    "6.9-clickjacking.html": "Manipulação de iframes, sobreposição visual e desativação de proteções.",
    "6.10-configuracao.html": "Diretórios expostos, cabeçalhos inseguros e configurações padrão de fábrica.",
    "6.11-inclusao-arquivos.html": "Exploração de vulnerabilidades de Local/Remote File Inclusion (LFI/RFI).",
    "6.12a-codigo-inseguro-memoria.html": "Falhas clássicas de corrupção de memória e buffer overflows em C/C++.",
    "6.12b-codigo-inseguro-web.html": "Desserialização insegura, race conditions e erros de lógica em código web.",
    # Módulo 7
    "7.0-introducao.html": "Fundamentos da arquitetura cloud, IoT e sistemas industriais.",
    "7.1a-vetores-nuvem.html": "Erros de permissão em buckets, falhas de IAM e vazamento de chaves.",
    "7.1b-cloud-exploits.html": "Enumeração de metadados, escalação de privilégios e exploits na nuvem.",
    "7.2a-mobile-iot.html": "Análise estática de APKs, vetores de ataque mobile e firmware de IoT.",
    "7.2b-ics-scada-embedded.html": "ICS/SCADA, sistemas embarcados, redes industriais e Modbus.",
    # Módulo 8
    "8.0-introducao.html": "Conceitos de escalação de privilégios locais e técnicas pós-comprometimento.",
    "8.1a-persistencia-avancada.html": "Instalação de web shells, backdoors persistentes e modificação de serviços.",
    "8.2a-lateral-exfiltracao.html": "Técnicas de movimentação lateral, pivoting de rede e exfiltração segura.",
    # Módulo 9
    "9.0-introducao.html": "A importância da documentação e da tradução técnica para executivos.",
    "9.1-componentes-relatorio.html": "Sumário executivo, descrição técnica e classificação CVSS/critério.",
    "9.2-analise-recomendacoes.html": "Elaboração de planos de mitigação e contramedidas recomendadas.",
    "9.3-comunicacao-escalonamento.html": "Apresentação de resultados, diplomacia e reporte de falhas críticas.",
    "9.4-atividades-pos-entrega.html": "Testes de revalidação (re-testing), retenção de dados e encerramento.",
    # Módulo 10
    "10.0-introducao.html": "Fundamentos de automação de testes e customização de ferramentas.",
    "10.1a-fundamentos-script.html": "Lógica de programação com scripts rápidos e tratamento de dados brutos.",
    "10.1b-linguagens-pratica.html": "Uso de Python e Bash para automação de tarefas repetitivas em testes.",
    "10.2a-recon-enum-tools.html": "Exploração aprofundada de Nmap, GoBuster, Sublist3r e Amass.",
    "10.2b-vuln-cred-tools.html": "Domínio de Hydra, John the Ripper, Hashcat, Nessus e Sqlmap.",
    "10.2c-persist-evasion-tools.html": "Uso de Metasploit, Netcat, Empire e técnicas para evadir antivírus.",
    "10.2d-forense-special-tools.html": "Ferramentas como Wireshark, Autopsy, Volatility e análise de memória."
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
        'title': lesson['title'].split(' ')[0] + ' ' + ' '.join(lesson['title'].split(' ')[1:-1]) if len(lesson['title'].split(' ')) > 1 else lesson['title'], # remove the ' 10.2a' from title if exists
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
