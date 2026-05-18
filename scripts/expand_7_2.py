import json
P='/home/gabriel/Documentos/dev/cyberduo/scripts/lesson_definitions.json'
with open(P,'r') as f: L=json.load(f)

L = [l for l in L if l['filename'] != '7.2-sistemas-especializados.html']
L.extend([
{"filename":"7.2a-mobile-iot.html","module":"7","title":"Mobile e IoT 7.2a","victory_msg":"MOBILE & IOT DOMINADOS!","steps":[
{"type":"teach","icon":"fa-mobile-screen","title":"Atacando Dispositivos Móveis","content":"Dispositivos móveis são alvos via <b>apps maliciosos</b>, <b>MDM bypass</b>, <b>jailbreak/root</b> e <b>interceptação de tráfego</b>. Ferramentas: <b>Frida</b>, <b>Objection</b>, <b>MobSF</b>.","highlight":"Celulares são computadores vulneráveis no bolso"},
{"type":"teach","icon":"fa-mobile-retro","title":"Vulnerabilidades Móveis","content":"Principais riscos: <b>armazenamento inseguro</b> de dados no dispositivo, <b>comunicação sem TLS</b>, <b>autenticação fraca</b>, <b>binary protections</b> ausentes e <b>side-loading</b> de APKs.","highlight":"OWASP Mobile Top 10 lista os riscos"},
{"type":"quiz","task":"Qual ferramenta é usada para análise dinâmica de apps móveis via hooking?","options":["Frida","Nmap","Aircrack-ng"],"correctText":"Frida","explanation":"Frida injeta scripts em apps mobile em tempo real para análise dinâmica e bypass de proteções (ex: SSL Pinning)."},
{"type":"teach","icon":"fa-microchip","title":"Atacando IoT","content":"Dispositivos IoT têm superfície de ataque ampla: <b>firmware inseguro</b>, <b>credenciais default</b>, <b>protocolos sem criptografia</b> (MQTT, CoAP), <b>interfaces expostas</b> (UART, JTAG).","highlight":"IoT = muitos dispositivos, pouca segurança"},
{"type":"teach","icon":"fa-tower-broadcast","title":"Protocolos IoT","content":"<b>MQTT</b>: protocolo pub/sub leve, frequentemente sem autenticação. <b>CoAP</b>: versão IoT do HTTP. <b>Zigbee/Z-Wave</b>: redes de curto alcance doméstico. <b>LoRaWAN</b>: longo alcance, baixo consumo.","highlight":"Protocolos IoT priorizam eficiência sobre segurança"},
{"type":"match","title":"Protocolo IoT → Descrição","pairs":[{"term":"MQTT","definition":"Pub/sub leve (sem auth comum)"},{"term":"CoAP","definition":"HTTP para IoT (UDP)"},{"term":"Zigbee","definition":"Mesh de curto alcance"},{"term":"LoRaWAN","definition":"Longo alcance e baixo consumo"}]},
{"type":"fill","sentence":"Uma das vulnerabilidades mais exploradas em roteadores e câmeras IoT é o uso de ___ e senhas padrão de fábrica que nunca são alteradas.","options":["credenciais default","certificados SSH","chaves PGP"],"correctText":"credenciais default","explanation":"A maioria dos ataques IoT tenta 'admin/admin' ou senhas similares de fábrica."}
]},
{"filename":"7.2b-ics-scada-embedded.html","module":"7","title":"ICS/SCADA, Embarcados e Especializados 7.2b","victory_msg":"ICS/SCADA & EMBARCADOS DOMINADOS!","steps":[
{"type":"teach","icon":"fa-industry","title":"ICS e SCADA (Tecnologia Operacional)","content":"Sistemas <b>ICS</b> (Industrial Control Systems) e <b>SCADA</b> controlam infraestrutura crítica (água, energia). Uma invasão em ambientes de <b>OT (Operational Technology)</b> causa danos físicos no mundo real (ex: Stuxnet).","highlight":"No mundo OT, segurança significa segurança FÍSICA e continuidade."},
{"type":"teach","icon":"fa-plug","title":"PLCs e Protocolos OT","content":"Máquinas são controladas por <b>PLCs</b> (Programmable Logic Controllers). Protocolos industriais clássicos como <b>Modbus</b> e <b>DNP3</b> foram criados sem criptografia ou autenticação, confiando no isolamento da rede (Air Gap).","highlight":"Modbus envia comandos industriais em texto claro."},
{"type":"quiz","task":"Qual protocolo é amplamente utilizado em sistemas industriais (SCADA/ICS) para comunicação entre PLCs, mas não possui criptografia ou autenticação nativa?","options":["Modbus","HTTPS","SSH"],"correctText":"Modbus","explanation":"Modbus é um protocolo antigo (1979) e não seguro por padrão, sendo muito visado em ataques OT."},
{"type":"teach","icon":"fa-car","title":"Sistemas Embarcados e CAN Bus","content":"Veículos modernos usam o protocolo <b>CAN bus</b> para comunicação interna (freios, direção). Injeção de mensagens no CAN bus (ex: OBD-II port) permite assumir controle do carro.","highlight":"CAN bus não tem autenticação de origem."},
{"type":"teach","icon":"fa-credit-card","title":"PoS, RFID e NFC","content":"Sistemas de Ponto de Venda (<b>PoS</b>) são alvos de RAM scrapers (roubo de cartões). Tecnologias de rádio como <b>RFID</b> (crachás) e <b>NFC</b> podem ser clonadas usando proxmark3 ou interceptadas de perto.","highlight":"Clonagem de RFID abre portas físicas no pentest."},
{"type":"match","title":"Tecnologia → Aplicação","pairs":[{"term":"SCADA","definition":"Controle industrial (energia/água)"},{"term":"CAN bus","definition":"Comunicação veicular (carros)"},{"term":"RFID","definition":"Controle de acesso físico (crachás)"},{"term":"PoS","definition":"Ponto de Venda (caixas de loja)"}]},
{"type":"fill","sentence":"O isolamento total de uma rede OT (Industrial) da Internet e de outras redes é chamado de ___.","options":["Air Gap","Firewall","Sandboxing"],"correctText":"Air Gap","explanation":"O 'Air Gap' é uma barreira física de rede, frequentemente violada por pendrives (ex: Stuxnet)."}
]}
])
with open(P,'w') as f: json.dump(L,f,ensure_ascii=False,indent=2)
print(f"✅ {len(L)} lessons (expanded 7.2)")
