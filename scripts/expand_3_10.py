import json
P='/home/gabriel/Downloads/64Gram Desktop/CyberDuo/scripts/lesson_definitions.json'
with open(P,'r') as f: L=json.load(f)

# Expand 3.1 (10→20 steps via split)
L = [l for l in L if l['filename'] != '3.1-reconhecimento-passivo.html']
L.extend([
{"filename":"3.1a-osint-busca.html","module":"3","title":"OSINT e Buscas 3.1a","victory_msg":"OSINT DOMINADO!","steps":[
{"type":"teach","icon":"fa-globe","title":"OSINT Overview","content":"<b>OSINT</b> coleta informações de fontes públicas: <b>motores de busca</b>, <b>redes sociais</b>, <b>registros DNS</b>, <b>WHOIS</b>, <b>certificados TLS</b>, <b>documentos vazados</b> e <b>metadados de arquivos</b>.","highlight":"Fontes públicas = mina de ouro"},
{"type":"teach","icon":"fa-search","title":"Google Dorking Avançado","content":"Operadores: <b>site:</b> (domínio), <b>filetype:</b> (formato), <b>inurl:</b> (URL), <b>intitle:</b> (título), <b>intext:</b> (conteúdo), <b>cache:</b> (versão em cache). Combinações potencializam resultados.","highlight":"Google Dorks revelam dados que não deveriam ser públicos"},
{"type":"example","icon":"fa-terminal","title":"Dorks para Pentest","scenario":"Buscando arquivos sensíveis expostos em um domínio alvo.","code":"site:alvo.com filetype:sql\nsite:alvo.com filetype:env\nsite:alvo.com inurl:admin\nsite:alvo.com intitle:\"index of\"","takeaway":"Combine operadores para buscas cirúrgicas."},
{"type":"teach","icon":"fa-address-card","title":"WHOIS e DNS Enumeration","content":"<b>WHOIS</b>: proprietário, e-mails, nameservers. <b>dig/nslookup</b>: registros A, MX, NS, TXT. <b>Zone Transfer</b> (AXFR): se permitido, revela TODOS os registros DNS de uma zona.","highlight":"Zone Transfer = mapa completo do DNS"},
{"type":"example","icon":"fa-terminal","title":"DNS Zone Transfer","scenario":"Tentando um zone transfer contra o nameserver do alvo para obter todos os registros DNS.","code":"dig axfr alvo.com @ns1.alvo.com","takeaway":"Zone transfers mal configurados expõem toda a infraestrutura DNS."},
{"type":"quiz","task":"Qual consulta DNS revela TODOS os registros de uma zona se estiver mal configurada?","options":["Zone Transfer (AXFR)","Reverse DNS","DNS over HTTPS"],"correctText":"Zone Transfer (AXFR)","explanation":"AXFR transfere todos os registros DNS de uma zona — deve ser restrito apenas a servidores secundários."},
{"type":"teach","icon":"fa-certificate","title":"Certificate Transparency","content":"<b>CT Logs</b> registram todos os certificados TLS emitidos. Ferramentas como <b>crt.sh</b> permitem descobrir subdomínios a partir dos certificados registrados.","highlight":"Certificados TLS revelam subdomínios ocultos"},
{"type":"fill","sentence":"A plataforma ___ permite descobrir subdomínios a partir de logs de Certificate Transparency.","options":["crt.sh","Google","Facebook"],"correctText":"crt.sh","explanation":"crt.sh indexa certificados TLS públicos e lista todos os domínios/subdomínios associados."}
]},
{"filename":"3.1b-osint-ferramentas.html","module":"3","title":"Ferramentas OSINT 3.1b","victory_msg":"TOOLKIT OSINT DOMINADO!","steps":[
{"type":"teach","icon":"fa-toolbox","title":"Recon-ng","content":"<b>Recon-ng</b> é um framework OSINT modular (similar ao Metasploit). Possui módulos para <b>WHOIS</b>, <b>DNS</b>, <b>harvesting de e-mails</b>, <b>busca de subdomínios</b> e <b>geolocalização</b>.","highlight":"Recon-ng = Metasploit do OSINT"},
{"type":"teach","icon":"fa-envelope","title":"theHarvester","content":"<b>theHarvester</b> coleta <b>e-mails</b>, <b>nomes</b>, <b>subdomínios</b>, <b>IPs</b> e <b>URLs</b> de fontes públicas (Google, Bing, LinkedIn, Shodan, Hunter.io).","highlight":"theHarvester = coleta massiva de intel"},
{"type":"example","icon":"fa-terminal","title":"theHarvester em Ação","scenario":"Coletando e-mails e subdomínios do domínio alvo usando múltiplas fontes.","code":"theHarvester -d alvo.com -b google,bing,linkedin -l 500","takeaway":"Combine múltiplas fontes para máxima cobertura."},
{"type":"teach","icon":"fa-file-lines","title":"Metadata Analysis","content":"Documentos (PDF, DOCX, XLSX) contêm <b>metadados</b>: autor, software, datas, caminhos de rede internos. <b>Exiftool</b> e <b>FOCA</b> extraem essas informações.","highlight":"Metadados revelam infraestrutura interna"},
{"type":"example","icon":"fa-terminal","title":"Exiftool para Metadados","scenario":"Extraindo metadados de um PDF público encontrado no site do alvo.","code":"exiftool documento.pdf\n# Revela: Author, Creator (software), Create Date, internal paths","takeaway":"Metadados podem revelar usernames, software e caminhos internos."},
{"type":"teach","icon":"fa-database","title":"Shodan e Censys","content":"<b>Shodan</b>: indexa servidores, câmeras, IoT. <b>Censys</b>: foca em certificados e serviços TLS. Ambos permitem buscar dispositivos do alvo sem enviar pacotes.","highlight":"Buscar dispositivos sem tocar no alvo"},
{"type":"teach","icon":"fa-users","title":"LinkedIn e Redes Sociais","content":"<b>LinkedIn</b>: vagas revelam tecnologias, perfis revelam hierarquia. <b>Hunter.io</b>: encontra padrões de e-mail. <b>Maltego</b>: visualiza relações entre entidades.","highlight":"Pessoas revelam mais do que imaginam"},
{"type":"match","title":"Ferramenta OSINT → Função","pairs":[{"term":"Recon-ng","definition":"Framework modular de OSINT"},{"term":"theHarvester","definition":"E-mails e subdomínios"},{"term":"Exiftool","definition":"Metadados de documentos"},{"term":"FOCA","definition":"Metadados + fingerprinting"},{"term":"Maltego","definition":"Visualização de relações"}]},
{"type":"quiz","task":"Qual ferramenta extrai metadados (autor, software, paths) de documentos como PDF e DOCX?","options":["Exiftool","Nmap","SQLMap"],"correctText":"Exiftool","explanation":"Exiftool lê/escreve metadados em 300+ formatos de arquivo."},
{"type":"fill","sentence":"O framework OSINT modular que funciona de forma similar ao Metasploit é o ___.","options":["Recon-ng","Shodan","theHarvester"],"correctText":"Recon-ng","explanation":"Recon-ng tem módulos carregáveis, workspaces e banco de dados, similar ao Metasploit."}
]}
])

# Expand 10.1 (7→18 steps)
L = [l for l in L if l['filename'] != '10.1-scripts-desenvolvimento.html']
L.extend([
{"filename":"10.1a-fundamentos-script.html","module":"10","title":"Fundamentos de Script 10.1a","victory_msg":"FUNDAMENTOS DE SCRIPT DOMINADOS!","steps":[
{"type":"teach","icon":"fa-code","title":"10.1.2 Construções Lógicas","content":"Construções essenciais para scripts: <b>if/else</b> (condicionais), <b>for/while</b> (loops), <b>try/except</b> (tratamento de erros). Todo script de pentest usa essas construções.","highlight":"Lógica = fundamento de todo script"},
{"type":"teach","icon":"fa-database","title":"10.1.4 Estruturas de Dados","content":"<b>Listas</b>: coleção ordenada (IPs, portas). <b>Dicionários</b>: pares chave-valor (host→vulnerabilidades). <b>Sets</b>: valores únicos (eliminar duplicatas).","highlight":"Estrutura certa = código eficiente"},
{"type":"teach","icon":"fa-puzzle-piece","title":"10.1.6 Bibliotecas","content":"Bibliotecas estendem a funcionalidade: <b>import requests</b> (HTTP), <b>import socket</b> (rede), <b>import os</b> (sistema). Sem bibliotecas, tudo seria reinventado do zero.","highlight":"Bibliotecas = atalhos para funcionalidades complexas"},
{"type":"teach","icon":"fa-gears","title":"10.1.7-9 Funções e Classes","content":"<b>Procedimentos</b>: blocos de código reutilizáveis. <b>Funções</b>: procedimentos que retornam valor. <b>Classes</b>: agrupam dados + comportamento (OOP).","highlight":"Funções = modularidade. Classes = organização."},
{"type":"quiz","task":"Qual estrutura de dados Python é ideal para armazenar pares IP→vulnerabilidade?","options":["Dicionário","Lista","String"],"correctText":"Dicionário","explanation":"Dicionários permitem acessar dados por chave (IP) ao invés de índice numérico."},
{"type":"fill","sentence":"Para importar funcionalidade HTTP em Python, usamos ___.","options":["import requests","import nmap","import metasploit"],"correctText":"import requests","explanation":"A biblioteca requests é o padrão para requisições HTTP em Python."}
]},
{"filename":"10.1b-linguagens-pratica.html","module":"10","title":"Linguagens e Prática 10.1b","victory_msg":"LINGUAGENS DE PENTEST DOMINADAS!","steps":[
{"type":"teach","icon":"fa-terminal","title":"10.1.12 Bash Scripting","content":"<b>Bash</b> é a cola entre ferramentas Linux. Automatiza: varreduras em massa, parsing de saída, enumeração de hosts. Essencial para qualquer pentester em Linux.","highlight":"Bash = automação nativa do Linux"},
{"type":"example","icon":"fa-code","title":"Scan em Massa com Bash","scenario":"Script que varre uma subnet inteira e salva hosts com portas abertas.","code":"#!/bin/bash\nfor ip in $(seq 1 254); do\n  (ping -c1 -W1 192.168.1.$ip > /dev/null 2>&1 && echo \"192.168.1.$ip UP\") &\ndone\nwait","takeaway":"Bash com & (background) paraleliza tarefas."},
{"type":"teach","icon":"fa-snake","title":"10.1.13 Python para Pentest","content":"<b>Python</b> é a linguagem nº1: <b>requests</b> (web), <b>scapy</b> (pacotes), <b>pwntools</b> (exploits), <b>impacket</b> (Windows/AD), <b>paramiko</b> (SSH), <b>beautifulsoup</b> (parsing HTML).","highlight":"Python = canivete suíço do pentester"},
{"type":"teach","icon":"fa-windows","title":"10.1.15 PowerShell para AD","content":"<b>PowerShell</b> domina ambientes Windows/AD: <b>Get-ADUser</b>, <b>Invoke-Command</b>, <b>Download cradle</b>. Também é usado ofensivamente: <b>PowerView</b>, <b>PowerUp</b>, <b>Invoke-Mimikatz</b>.","highlight":"PowerShell = ferramenta #1 para atacar AD"},
{"type":"teach","icon":"fa-gem","title":"10.1.14 Ruby","content":"<b>Ruby</b> é a linguagem do <b>Metasploit Framework</b>. Escrever módulos Metasploit requer Ruby. Também usado em ferramentas como <b>WPScan</b> e <b>BeEF</b>.","highlight":"Ruby = linguagem do Metasploit"},
{"type":"teach","icon":"fa-js","title":"10.1.17 JavaScript","content":"<b>JavaScript</b> é essencial para ataques web: <b>XSS payloads</b>, <b>DOM manipulation</b>, <b>WebSocket hijacking</b>. Node.js expande para server-side.","highlight":"JS = linguagem dos ataques web client-side"},
{"type":"teach","icon":"fa-file-code","title":"10.1.10 Análise de Código","content":"Saber <b>ler e entender</b> código de exploits é tão importante quanto saber escrever. Identifique: <b>CVE alvo</b>, <b>vetor de ataque</b>, <b>payload</b>, <b>condições de sucesso</b>.","highlight":"Leia o exploit ANTES de executar"},
{"type":"match","title":"Linguagem → Uso Principal","pairs":[{"term":"Python","definition":"Scripts, exploits, automação geral"},{"term":"Bash","definition":"Automação Linux, cola de ferramentas"},{"term":"PowerShell","definition":"Ataques AD e automação Windows"},{"term":"Ruby","definition":"Módulos Metasploit"},{"term":"JavaScript","definition":"XSS e ataques client-side"}]},
{"type":"quiz","task":"Qual linguagem é usada para escrever módulos do Metasploit Framework?","options":["Ruby","Python","C++"],"correctText":"Ruby","explanation":"Metasploit é escrito em Ruby e seus módulos de exploit também são em Ruby."},
{"type":"fill","sentence":"A ferramenta PowerShell usada para enumerar Active Directory é o ___.","options":["PowerView","PowerPoint","PowerBI"],"correctText":"PowerView","explanation":"PowerView (parte do PowerSploit) enumera usuários, grupos, trusts e shares do AD."}
]}
])

with open(P,'w') as f: json.dump(L,f,ensure_ascii=False,indent=2)
print(f"✅ {len(L)} lessons (expanded 3.1→a/b, 10.1→a/b)")
