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
    "3.1a-osint-dns.html": "Google Dorking, WHOIS, DNSRecon e enumeração passiva inicial de domínios e subdomínios.",
    "3.1b-recon-ng-shodan.html": "Recon-ng, theHarvester, Certificate Transparency e busca de ativos expostos com Shodan/Censys.",
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
    "5.1a-fundamentos-mitm.html": "Protocolos de rede, ARP Spoofing e posicionamento do atacante em Man-in-the-Middle.",
    "5.1b-resolucao-smb.html": "LLMNR/NBT-NS poisoning, captura de hashes com Responder e enumeração/exploração SMB.",
    "5.1c-credenciais-controles.html": "Pass-the-Hash, Kerberoasting, AS-REP Roasting, NAC e segmentação por VLAN.",
    "5.2-wireless.html": "Quebra de redes sem fio WPA/WPA2, ataques a WPS e criação de Rogue APs.",
    # Módulo 6
    "6.0-introducao.html": "Fundamentos do protocolo HTTP, arquitetura web e a superfície de ataque.",
    "6.1a-owasp-fundamentos.html": "Fundamentos do OWASP Top 10 e falhas de Broken Access Control.",
    "6.1b-owasp-riscos-modernos.html": "Design inseguro, configuração incorreta, componentes vulneráveis e autenticação quebrada.",
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
    "6.12a-memoria-concorrencia.html": "Buffer overflow, use-after-free e race conditions em aplicações inseguras.",
    "6.12b-desserializacao-reversa.html": "Desserialização insegura e análise de comportamento perigoso em código.",
    # Módulo 7
    "7.0-introducao.html": "Visão geral do Módulo 7, motivação profissional da Cisco e o que você dominará nesta jornada.",
    "7.1a-cloud.html": "Tipos de serviços em nuvem, colheita de credenciais com o SET (Kali), escalada de privilégios e aquisição de contas.",
    "7.1b-configuracoes-nuvem.html": "Ataques IMDSv1/v2 por SSRF, buckets mal configurados, DoS na nuvem, injeção de malware e CPU Side-Channels.",
    "7.2a-mobile.html": "Engenharia reversa, análise local SQLite/Keychain, bypass biométrico e Certificate Pinning com Frida e Objection.",
    "7.2b-iot-virtualizacao.html": "Protocolos IoT, Shodan, BLE MITM, BMC/IPMI, VM Escape e auditorias cloud-native (kube-hunter, Grype, Falco).",
    # Módulo 8
    "8.0-introducao.html": "Visão geral do módulo e objetivos principais sobre segurança ofensiva.",
    "8.1a-shells-c2.html": "Diferenças entre Shell Reverso e Bind, e uso avançado de utilitários C2 e Netcat.",
    "8.1b-persistencia-avancada.html": "Persistência em Windows e Linux via tarefas agendadas, cron jobs e novos usuários.",
    "8.2a-movimento-lateral.html": "Técnicas de pivotagem, exfiltração de dados e o conceito de Living off the Land (LOLBins).",
    "8.2b-powershell-sysinternals.html": "Uso avançado de cmdlets PowerShell e ferramentas Sysinternals no Windows.",
    "8.2c-escalada-limpeza.html": "BloodHound para Active Directory, escalada de privilégios, esteganografia e sanitização NIST 800-88.",
    # Módulo 9
    "9.0-introducao.html": "A importância da documentação e da tradução técnica para executivos.",
    "9.1a-componentes-distribuicao.html": "Público executivo e técnico, estrutura do relatório, CVE/CVSS e distribuição segura.",
    "9.1b-notas-causa-raiz.html": "Gestão de notas, Dradis, validação manual e análise de causa raiz.",
    "9.2a-controles-remediacao.html": "Recomendações práticas, controles de segurança e remediação orientada ao risco.",
    "9.2b-comunicacao-pos-entrega.html": "Comunicação durante o teste, debriefing, limpeza e encerramento seguro.",
    # Módulo 10
    "10.0-introducao.html": "Fundamentos de automação de testes e customização de ferramentas.",
    "10.1a-logica-estruturas.html": "Construções lógicas, JSON, listas, dicionários e bases de automação para pentest.",
    "10.1b-scripts-bibliotecas.html": "Bibliotecas, funções, classes e o uso de Bash, Python e PowerShell no arsenal ofensivo.",
    "10.2a-ferramentas-caso-uso.html": "Classificação de ferramentas por caso de uso: rede, credenciais, exploração e C2.",
    "10.2b-analise-codigo-reversa.html": "Leitura de exploits, Ghidra, engenharia reversa e análise segura de código ofensivo."
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
