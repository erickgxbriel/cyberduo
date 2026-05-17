import json
P='/home/gabriel/Downloads/64Gram Desktop/CyberDuo/scripts/lesson_definitions.json'
with open(P,'r') as f: L=json.load(f)

# Replace 5.1 with expanded version (8→20 steps)
L = [l for l in L if l['filename'] != '5.1-vulnerabilidades-rede.html']
L.extend([
{"filename":"5.1a-protocolos-ataques.html","module":"5","title":"Protocolos e Ataques de Rede 5.1a","victory_msg":"PROTOCOLOS DE REDE DOMINADOS!","steps":[
{"type":"teach","icon":"fa-route","title":"ARP Spoofing","content":"<b>ARP Spoofing</b> envia respostas ARP falsas para associar o MAC do atacante ao IP do gateway. Todo o tráfego da vítima passa pelo atacante (<b>Man-in-the-Middle</b>).","highlight":"ARP Spoofing = redirecionar tráfego para si"},
{"type":"teach","icon":"fa-shield-halved","title":"Man-in-the-Middle (MITM)","content":"No <b>MITM</b>, o atacante intercepta a comunicação entre duas partes. Pode <b>ler</b>, <b>modificar</b> e <b>injetar</b> dados. Ferramentas: <b>Ettercap</b>, <b>Bettercap</b>, <b>mitmproxy</b>.","highlight":"MITM = interceptação + manipulação em tempo real"},
{"type":"teach","icon":"fa-server","title":"LLMNR/NBT-NS Poisoning","content":"<b>LLMNR</b> e <b>NBT-NS</b> são protocolos Windows de resolução de nomes local. O atacante responde a essas queries para capturar <b>hashes NTLMv2</b> de credenciais. Ferramenta: <b>Responder</b>.","highlight":"Responder captura hashes automaticamente na rede"},
{"type":"example","icon":"fa-terminal","title":"Responder em Ação","scenario":"O pentester roda Responder na rede e captura hashes NTLMv2 quando usuários Windows tentam acessar shares inexistentes.","code":"responder -I eth0 -wrf","takeaway":"LLMNR poisoning é um dos ataques mais eficazes em redes Windows."},
{"type":"quiz","task":"Qual ferramenta captura hashes NTLMv2 respondendo a queries LLMNR/NBT-NS?","options":["Responder","Nmap","Wireshark"],"correctText":"Responder","explanation":"Responder se anuncia como servidor para queries de resolução de nome e captura credenciais."},
{"type":"teach","icon":"fa-arrow-right-arrow-left","title":"NTLM Relay","content":"Após capturar um hash NTLM, o atacante pode <b>retransmiti-lo</b> (relay) para outro serviço, autenticando sem crackar a senha. Ferramenta: <b>ntlmrelayx</b> (Impacket).","highlight":"Relay = usar o hash imediatamente sem crackar"},
{"type":"teach","icon":"fa-network-wired","title":"VLAN Hopping","content":"<b>VLAN Hopping</b> permite ao atacante saltar entre VLANs. Técnicas: <b>Switch Spoofing</b> (fingir ser um switch trunk) e <b>Double Tagging</b> (encapsular 2 tags 802.1Q).","highlight":"VLANs não são barreira de segurança real"},
{"type":"teach","icon":"fa-globe","title":"DNS Poisoning","content":"<b>DNS Poisoning/Spoofing</b> altera respostas DNS para redirecionar vítimas a sites falsos. O atacante injeta registros DNS falsos no cache do resolver.","highlight":"DNS envenenado = site legítimo vira armadilha"},
{"type":"fill","sentence":"O ataque que retransmite hashes NTLM capturados para autenticar em outros serviços é o ___.","options":["NTLM Relay","Brute Force","Phishing"],"correctText":"NTLM Relay","explanation":"NTLM Relay usa o hash capturado imediatamente, sem precisar crackear."},
{"type":"match","title":"Ataque de Rede → Técnica","pairs":[{"term":"ARP Spoofing","definition":"Redireciona tráfego via ARP falso"},{"term":"LLMNR Poisoning","definition":"Captura hashes via resolução local"},{"term":"VLAN Hopping","definition":"Salta entre VLANs isoladas"},{"term":"DNS Poisoning","definition":"Redireciona via DNS falso"}]}
]},
{"filename":"5.1b-senhas-kerberos.html","module":"5","title":"Ataques de Senha e Kerberos 5.1b","victory_msg":"ATAQUES DE SENHA DOMINADOS!","steps":[
{"type":"teach","icon":"fa-key","title":"Brute Force e Dictionary","content":"<b>Brute Force</b>: testa TODAS as combinações. <b>Dictionary</b>: testa palavras de uma lista. <b>Hybrid</b>: combina dicionário + regras (ex: Password1!, Password2!).","highlight":"Dicionário é mais rápido, brute force é mais completo"},
{"type":"teach","icon":"fa-unlock","title":"Pass-the-Hash","content":"No <b>Pass-the-Hash</b>, o atacante usa o hash NTLM capturado para autenticar em serviços Windows <b>sem precisar da senha em texto claro</b>. Funciona com <b>psexec</b> e <b>wmiexec</b>.","highlight":"Hash NTLM = equivalente à senha no Windows"},
{"type":"teach","icon":"fa-ticket","title":"Kerberoasting","content":"<b>Kerberoasting</b>: solicita tickets Kerberos TGS para contas de serviço e tenta crackar offline. Contas de serviço frequentemente têm senhas fracas e privilégios altos.","highlight":"Service accounts = alvo fácil com alto impacto"},
{"type":"example","icon":"fa-terminal","title":"Kerberoasting com Impacket","scenario":"O pentester solicita tickets TGS para todas as contas de serviço do AD e tenta crackar com Hashcat.","code":"GetUserSPNs.py domain/user:pass -dc-ip 10.0.0.1 -outputfile tgs.txt\nhashcat -m 13100 tgs.txt rockyou.txt","takeaway":"Kerberoasting não requer privilégios elevados no AD."},
{"type":"teach","icon":"fa-id-card","title":"AS-REP Roasting","content":"<b>AS-REP Roasting</b>: explora contas com <b>Kerberos pre-auth desabilitado</b>. O atacante solicita o AS-REP e cracka offline sem precisar de credenciais válidas.","highlight":"Pre-auth desabilitado = senha crackável sem login"},
{"type":"teach","icon":"fa-database","title":"Credential Stuffing","content":"<b>Credential Stuffing</b>: usa pares <b>email:senha</b> de vazamentos (breaches) para tentar login em outros serviços. 65% das pessoas reutilizam senhas.","highlight":"Reutilização de senhas = porta aberta"},
{"type":"quiz","task":"Qual ataque solicita tickets Kerberos TGS para crackar senhas de service accounts offline?","options":["Kerberoasting","Phishing","ARP Spoofing"],"correctText":"Kerberoasting","explanation":"Kerberoasting explora contas de serviço com SPNs registrados no Active Directory."},
{"type":"match","title":"Ataque → Requisito","pairs":[{"term":"Pass-the-Hash","definition":"Hash NTLM capturado"},{"term":"Kerberoasting","definition":"Acesso ao AD (qualquer user)"},{"term":"AS-REP Roasting","definition":"Pre-auth desabilitado"},{"term":"Credential Stuffing","definition":"Lista de credenciais vazadas"}]},
{"type":"fill","sentence":"O ataque que explora contas com Kerberos pre-authentication desabilitado é o ___.","options":["AS-REP Roasting","Kerberoasting","Pass-the-Hash"],"correctText":"AS-REP Roasting","explanation":"AS-REP Roasting funciona sem credenciais se a pre-auth estiver desabilitada."}
]}
])

# Replace 5.2 with expanded version
L = [l for l in L if l['filename'] != '5.2-vulnerabilidades-wireless.html']
L.extend([
{"filename":"5.2a-wireless-fundamentals.html","module":"5","title":"Fundamentos Wireless 5.2a","victory_msg":"WIRELESS FUNDAMENTALS DOMINADOS!","steps":[
{"type":"teach","icon":"fa-wifi","title":"Protocolos WiFi","content":"<b>WEP</b>: RC4, quebrado (não usar). <b>WPA</b>: TKIP, vulnerável. <b>WPA2-Personal</b>: PSK + AES/CCMP, padrão atual. <b>WPA2-Enterprise</b>: 802.1X + RADIUS. <b>WPA3</b>: SAE, mais seguro.","highlight":"WEP→WPA→WPA2→WPA3: evolução da segurança"},
{"type":"teach","icon":"fa-shield-halved","title":"WPA2-Enterprise vs Personal","content":"<b>Personal (PSK)</b>: senha compartilhada por todos. <b>Enterprise (802.1X)</b>: cada usuário tem credenciais individuais autenticadas por RADIUS. Enterprise é mais seguro.","highlight":"Enterprise = autenticação individual por usuário"},
{"type":"quiz","task":"Qual modo WPA2 usa autenticação individual via servidor RADIUS?","options":["WPA2-Enterprise","WPA2-Personal","WEP"],"correctText":"WPA2-Enterprise","explanation":"WPA2-Enterprise usa 802.1X com RADIUS para autenticar cada usuário individualmente."},
{"type":"teach","icon":"fa-satellite-dish","title":"Captura de Handshake","content":"O <b>4-way handshake</b> do WPA2 pode ser capturado com <b>airodump-ng</b>. Para forçar a captura, usa-se <b>deautenticação</b> para desconectar clientes e forçar reconexão.","highlight":"Deauth → captura handshake → brute force offline"},
{"type":"teach","icon":"fa-bolt","title":"PMKID Attack","content":"O ataque <b>PMKID</b> captura o hash diretamente do AP, <b>sem precisar de clientes conectados</b>. É mais rápido que esperar o handshake. Ferramenta: <b>hcxdumptool</b>.","highlight":"PMKID = ataque ao AP sem depender de clientes"},
{"type":"fill","sentence":"O ataque ___ captura o hash WiFi direto do AP sem precisar de clientes conectados.","options":["PMKID","Evil Twin","Deauth"],"correctText":"PMKID","explanation":"PMKID extrai o hash do primeiro frame EAPOL, sem necessidade de capturar o handshake completo."}
]},
{"filename":"5.2b-wireless-attacks.html","module":"5","title":"Ataques Wireless Avançados 5.2b","victory_msg":"WIRELESS ATTACKS DOMINADOS!","steps":[
{"type":"teach","icon":"fa-tower-broadcast","title":"Evil Twin","content":"<b>Evil Twin</b>: AP falso com SSID idêntico ao legítimo. Combinado com <b>deauth</b>, força vítimas a conectar no AP falso. Ferramentas: <b>hostapd-wpe</b>, <b>Fluxion</b>.","highlight":"AP falso + deauth = interceptação total"},
{"type":"teach","icon":"fa-ghost","title":"Karma Attack","content":"<b>Karma</b>: o AP falso responde a <b>TODAS</b> as probe requests, fingindo ser qualquer rede que o dispositivo já conhece. O celular da vítima conecta automaticamente.","highlight":"Karma = 'eu sou a rede que você procura'"},
{"type":"teach","icon":"fa-ban","title":"Deauthentication Attack","content":"Frames de <b>deautenticação 802.11</b> não são autenticados. O atacante envia deauth frames para desconectar clientes, forçando reconexão ao Evil Twin ou captura de handshake.","highlight":"Deauth é irrastreável e não requer autenticação"},
{"type":"example","icon":"fa-terminal","title":"Deauth com Aireplay-ng","scenario":"O pentester envia 100 frames de deautenticação para desconectar o cliente alvo do AP legítimo.","code":"aireplay-ng --deauth 100 -a AA:BB:CC:DD:EE:FF -c 11:22:33:44:55:66 wlan0mon","takeaway":"Deauth é o catalisador de vários ataques WiFi."},
{"type":"quiz","task":"Qual ataque faz o AP falso responder a QUALQUER probe request, fingindo ser qualquer rede?","options":["Karma","Evil Twin","WEP Cracking"],"correctText":"Karma","explanation":"Karma responde 'sim, sou eu' para toda probe request que o dispositivo envia."},
{"type":"teach","icon":"fa-shield-halved","title":"Rogue AP Detection","content":"Para detectar APs falsos: <b>WIPS</b> (Wireless Intrusion Prevention), <b>802.11w</b> (Protected Management Frames) contra deauth, e <b>NAC</b> (Network Access Control).","highlight":"802.11w impede deauth forjado"},
{"type":"match","title":"Ataque WiFi → Descrição","pairs":[{"term":"Evil Twin","definition":"AP falso com mesmo SSID"},{"term":"Karma","definition":"AP que finge ser qualquer rede"},{"term":"PMKID","definition":"Hash direto do AP sem clientes"},{"term":"Deauth","definition":"Desconecta clientes forçadamente"}]},
{"type":"fill","sentence":"O padrão ___ protege frames de gerenciamento 802.11 contra ataques de deautenticação.","options":["802.11w","802.11ac","802.11n"],"correctText":"802.11w","explanation":"802.11w (PMF) autentica frames de gerenciamento, impedindo deauth forjado."}
]}
])

with open(P,'w') as f: json.dump(L,f,ensure_ascii=False,indent=2)
print(f"✅ {len(L)} lessons (expanded 5.1→5.1a/b, 5.2→5.2a/b)")
