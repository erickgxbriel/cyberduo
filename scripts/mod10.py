import json
import os

JSON_PATH = "/home/gabriel/Documentos/dev/cyberduo/scripts/lesson_definitions.json"


def load_json(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def main():
    lessons = load_json(JSON_PATH)
    lessons = [lesson for lesson in lessons if lesson.get("module") != "10"]

    module_10_lessons = [
        {
            "filename": "10.0-introducao.html",
            "module": "10",
            "title": "Por Que Ferramentas e Código Fecham o Ciclo do Pentest",
            "victory_title": "Excelente!",
            "victory_msg": "ARSENAL INICIADO!",
            "steps": [
                {
                    "type": "teach",
                    "icon": "fa-toolbox",
                    "title": "Ferramentas Aceleram, Mas Não Pensam Por Você (Cisco 10.0.1)",
                    "content": "Pentest não é só apertar botões em ferramentas. O profissional precisa combinar <b>metodologia</b>, leitura crítica de resultados, noções de <b>scripting</b> e entendimento do que o código realmente faz. Ferramentas escalam o trabalho, mas não substituem julgamento técnico.",
                    "highlight": "Ferramenta sem interpretação gera falso positivo, ruído e decisões ruins."
                },
                {
                    "type": "teach",
                    "icon": "fa-code",
                    "title": "Saber Programar Amplia o Alcance do Pentester (Cisco 10.0.1)",
                    "content": "Ao longo do trabalho, você precisará adaptar scripts, automatizar tarefas repetitivas, ler exploits públicos e analisar amostras suspeitas. Por isso, o módulo aborda <b>Bash, Python, PowerShell</b> e a classificação de <b>ferramentas</b> por caso de uso.",
                    "highlight": "Programação transforma um operador de ferramenta em um profissional adaptável."
                },
                {
                    "type": "example",
                    "icon": "fa-terminal",
                    "title": "Exemplo - Quando Não Existe Ferramenta Pronta",
                    "scenario": "Durante um teste interno, o scanner não exporta os hosts exatamente no formato exigido pelo cliente. O pentester cria um script curto para reorganizar a saída e seguir o trabalho sem perder horas em tarefas manuais.",
                    "code": "$ cat hosts.txt | sort | uniq > ativos-final.txt\n[i] 312 hosts normalizados para o formato do relatório\n[+] Tarefa repetitiva automatizada sem depender de nova ferramenta",
                    "takeaway": "Scripting reduz atrito operacional e mantém o ritmo do engajamento."
                },
                {
                    "type": "quiz",
                    "task": "Qual é a principal razão para estudar ferramentas e scripting no contexto de pentest?",
                    "options": [
                        "Porque isso permite automatizar tarefas, adaptar fluxos e interpretar melhor código ofensivo",
                        "Porque ferramentas eliminam a necessidade de metodologia e validação manual",
                        "Porque certificações exigem decorar nomes de programas sem contexto"
                    ],
                    "correctText": "Porque isso permite automatizar tarefas, adaptar fluxos e interpretar melhor código ofensivo",
                    "explanation": "O valor real vem da combinação entre automação, análise crítica e adaptação ao cenário do cliente."
                },
                {
                    "type": "fill",
                    "sentence": "Neste módulo, o aluno aprende a classificar ___ de pentesting por caso de uso e a analisar código antes de executá-lo.",
                    "options": [
                        "ferramentas",
                        "imagens",
                        "planilhas"
                    ],
                    "correctText": "ferramentas",
                    "explanation": "A proposta do módulo é conectar ferramental, análise de código e automação prática."
                }
            ]
        },
        {
            "filename": "10.1a-logica-estruturas.html",
            "module": "10",
            "title": "Lógica, Estruturas e Bases do Scripting",
            "victory_title": "Excelente!",
            "victory_msg": "LÓGICA DE AUTOMAÇÃO DOMINADA!",
            "steps": [
                {
                    "type": "teach",
                    "icon": "fa-code-branch",
                    "title": "Construções Lógicas (Cisco 10.1.2)",
                    "content": "Toda linguagem útil para pentest precisa de <b>loops</b>, <b>condicionais</b>, operadores booleanos, operadores de string e operadores aritméticos. Esses blocos permitem iterar hosts, filtrar resultados, comparar respostas e construir automações repetíveis.",
                    "highlight": "Automação começa com controlar fluxo, decisão e repetição."
                },
                {
                    "type": "example",
                    "icon": "fa-repeat",
                    "title": "Exemplo - Loop para Varredura Básica",
                    "scenario": "Um analista precisa testar rapidamente se portas web estão respondendo em uma faixa curta de IPs e usa um loop simples para repetir a ação:",
                    "code": "for ip in 10.10.10.11 10.10.10.12 10.10.10.13; do\n  curl -I http://$ip:80 | head -n 1\ndone",
                    "takeaway": "O loop encapsula repetição sem exigir que o operador dispare o mesmo comando manualmente várias vezes."
                },
                {
                    "type": "teach",
                    "icon": "fa-database",
                    "title": "Estruturas de Dados Mais Comuns (Cisco 10.1.4)",
                    "content": "Na prática, o pentester lida o tempo todo com <b>JSON</b>, listas, arrays, dicionários, CSV e árvores. APIs devolvem JSON, varreduras viram CSV, e automações internas dependem de coleções estruturadas para não quebrar facilmente.",
                    "highlight": "Sem estrutura de dados, toda automação vira texto solto e frágil."
                },
                {
                    "type": "match",
                    "title": "Associe a Estrutura ao Uso",
                    "pairs": [
                        {
                            "term": "JSON",
                            "definition": "Formato leve usado com frequência em APIs e integrações"
                        },
                        {
                            "term": "Dicionário",
                            "definition": "Coleção baseada em pares chave e valor"
                        },
                        {
                            "term": "CSV",
                            "definition": "Arquivo simples útil para exportar dados tabulares"
                        },
                        {
                            "term": "Lista",
                            "definition": "Sequência ordenada de elementos manipuláveis por script"
                        }
                    ]
                },
                {
                    "type": "quiz",
                    "task": "Qual estrutura aparece com mais frequência quando um script de pentest consome uma API REST moderna?",
                    "options": [
                        "JSON",
                        "Bitmap",
                        "PDF"
                    ],
                    "correctText": "JSON",
                    "explanation": "JSON é o formato leve mais comum para transportar dados estruturados entre aplicações e APIs."
                },
                {
                    "type": "fill",
                    "sentence": "Quando um script precisa decidir entre continuar ou não uma ação com base em uma resposta, ele depende de estruturas ___ como `if`, `and` e `or`.",
                    "options": [
                        "lógicas",
                        "gráficas",
                        "estáticas"
                    ],
                    "correctText": "lógicas",
                    "explanation": "Condicionais e operadores lógicos são a base do fluxo de decisão no código."
                }
            ]
        },
        {
            "filename": "10.1b-scripts-bibliotecas.html",
            "module": "10",
            "title": "Bibliotecas, Funções e Linguagens do Arsenal",
            "victory_title": "Excelente!",
            "victory_msg": "SCRIPTING ORGANIZADO!",
            "steps": [
                {
                    "type": "teach",
                    "icon": "fa-book",
                    "title": "Bibliotecas, Procedimentos, Funções e Classes (Cisco 10.1.6-10.1.9)",
                    "content": "Bibliotecas reúnem código reutilizável. Procedimentos e funções encapsulam tarefas repetidas. Classes organizam objetos e comportamento. Esses conceitos ajudam o pentester a ler código de terceiros, adaptar automações internas e evitar scripts monolíticos difíceis de manter.",
                    "highlight": "Código modular é mais seguro de entender e mais fácil de auditar."
                },
                {
                    "type": "teach",
                    "icon": "fa-terminal",
                    "title": "Bash, Python e PowerShell (Cisco 10.1.1 e 10.1.12)",
                    "content": "<b>Bash</b> domina a automação nativa em Linux. <b>Python</b> é a linguagem mais versátil para integrar rede, web e parsing. <b>PowerShell</b> é essencial em ambientes Windows e Active Directory. O profissional também encontra Ruby, Perl e JavaScript em tooling ofensivo e em exploits públicos.",
                    "highlight": "Python, Bash e PowerShell cobrem a maior parte da automação prática do pentest."
                },
                {
                    "type": "example",
                    "icon": "fa-sitemap",
                    "title": "Exemplo - Função Reutilizável em Python",
                    "scenario": "Em vez de repetir o mesmo código de requisição em vários pontos, o analista encapsula a tarefa em uma função para reaproveitar e testar melhor:",
                    "code": "import requests\n\ndef consulta(host):\n    return requests.get(f'http://{host}/health', timeout=2).status_code\n\nprint(consulta('10.10.20.15'))",
                    "takeaway": "Funções reduzem duplicação e deixam o script mais previsível para manutenção."
                },
                {
                    "type": "match",
                    "title": "Associe a Linguagem ao Cenário",
                    "pairs": [
                        {
                            "term": "Bash",
                            "definition": "Automação rápida e nativa em Linux e Kali"
                        },
                        {
                            "term": "Python",
                            "definition": "Integração ampla com bibliotecas e criação de ferramentas customizadas"
                        },
                        {
                            "term": "PowerShell",
                            "definition": "Administração e automação em Windows e Active Directory"
                        },
                        {
                            "term": "Biblioteca",
                            "definition": "Conjunto reutilizável de recursos e rotinas de código"
                        }
                    ]
                },
                {
                    "type": "quiz",
                    "task": "Qual linguagem tende a ser mais importante quando o pentester precisa automatizar tarefas em um domínio Windows com Active Directory?",
                    "options": [
                        "PowerShell",
                        "CSS",
                        "Lua"
                    ],
                    "correctText": "PowerShell",
                    "explanation": "PowerShell foi desenhado para administração e automação profunda em ambientes Microsoft."
                },
                {
                    "type": "fill",
                    "sentence": "No Linux, a linguagem de script mais imediata para orquestrar comandos do sistema e pipelines é o ___.",
                    "options": [
                        "Bash",
                        "Photoshop",
                        "COBOL"
                    ],
                    "correctText": "Bash",
                    "explanation": "Bash é o shell mais familiar em distribuições Linux usadas em segurança ofensiva."
                }
            ]
        },
        {
            "filename": "10.2a-ferramentas-caso-uso.html",
            "module": "10",
            "title": "Ferramentas por Caso de Uso: Ofensiva, Rede e Credenciais",
            "victory_title": "Excelente!",
            "victory_msg": "FERRAMENTAS CLASSIFICADAS!",
            "steps": [
                {
                    "type": "teach",
                    "icon": "fa-layer-group",
                    "title": "Classificar Ferramentas Evita Uso Aleatório (Cisco 10.2)",
                    "content": "Uma boa prática é agrupar ferramentas por objetivo: <b>captura e análise de rede</b>, <b>quebra de credenciais</b>, <b>enumeração</b>, <b>exploração</b>, <b>forense</b> e <b>engenharia reversa</b>. Isso reduz improviso e melhora a escolha técnica em cada fase do engajamento.",
                    "highlight": "Ferramenta certa depende do objetivo, do contexto e do limite do escopo."
                },
                {
                    "type": "teach",
                    "icon": "fa-network-wired",
                    "title": "Wireshark, Hydra, John the Ripper e Hashcat",
                    "content": "<b>Wireshark</b> ajuda a inspecionar tráfego e protocolos. <b>Hydra</b> automatiza tentativas online de credenciais. <b>John the Ripper</b> e <b>Hashcat</b> quebram hashes offline com foco em velocidade e wordlists. Cada uma atua em uma camada diferente do problema.",
                    "highlight": "Online guessing e offline cracking são coisas diferentes e têm riscos diferentes."
                },
                {
                    "type": "example",
                    "icon": "fa-terminal",
                    "title": "Exemplo - Credenciais Online vs Offline",
                    "scenario": "Em um portal SSH, o analista usa Hydra para testar logins online. Já após obter um dump de hashes NTLM, migra para Hashcat no host de ataque para quebrar as senhas sem interagir mais com o alvo.",
                    "code": "$ hydra -l admin -P rockyou.txt ssh://10.10.30.9\n$ hashcat -m 1000 hashes.txt rockyou.txt",
                    "takeaway": "Hydra depende da rede e pode gerar alertas; Hashcat e John the Ripper operam offline contra hashes roubados."
                },
                {
                    "type": "teach",
                    "icon": "fa-bug",
                    "title": "Sqlmap, Metasploit e Frameworks C2",
                    "content": "<b>Sqlmap</b> automatiza exploração de SQL Injection. <b>Metasploit</b> organiza exploits, payloads e módulos auxiliares. Frameworks de <b>C2</b> como Empire ou Cobalt Strike focam persistência, beacons e pós-exploração de longo prazo.",
                    "highlight": "Metasploit tende a ganhar acesso inicial; C2 tende a sustentar operação pós-comprometimento."
                },
                {
                    "type": "match",
                    "title": "Associe a Ferramenta ao Caso de Uso",
                    "pairs": [
                        {
                            "term": "Wireshark",
                            "definition": "Analisar pacotes, sessões e protocolos de rede"
                        },
                        {
                            "term": "Hydra",
                            "definition": "Força bruta online contra serviços como SSH ou HTTP"
                        },
                        {
                            "term": "Hashcat / John the Ripper",
                            "definition": "Quebrar hashes offline com wordlists e regras"
                        },
                        {
                            "term": "Sqlmap",
                            "definition": "Automatizar exploração de SQL Injection"
                        }
                    ]
                },
                {
                    "type": "quiz",
                    "task": "Qual ferramenta é mais adequada para inspecionar tráfego capturado de rede e entender o comportamento de protocolos no detalhe?",
                    "options": [
                        "Wireshark",
                        "Hydra",
                        "Hashcat"
                    ],
                    "correctText": "Wireshark",
                    "explanation": "Wireshark é a referência para análise detalhada de pacotes e sessões de rede."
                },
                {
                    "type": "fill",
                    "sentence": "Quando o objetivo é quebrar senhas a partir de hashes roubados sem falar com o alvo, a abordagem correta é cracking ___ com ferramentas como Hashcat ou John the Ripper.",
                    "options": [
                        "offline",
                        "visual",
                        "manual"
                    ],
                    "correctText": "offline",
                    "explanation": "Cracking offline remove latência e bloqueios do serviço alvo e depende da potência do host atacante."
                }
            ]
        },
        {
            "filename": "10.2b-analise-codigo-reversa.html",
            "module": "10",
            "title": "Análise de Exploits, Malware e Engenharia Reversa",
            "victory_title": "Excelente!",
            "victory_msg": "ANÁLISE DE CÓDIGO CONSOLIDADA!",
            "steps": [
                {
                    "type": "teach",
                    "icon": "fa-microscope",
                    "title": "Nunca Execute Exploit Sem Ler o Código (Cisco 10.2)",
                    "content": "Exploit público pode conter comportamento inesperado, backdoor ou destruição não autorizada. Antes de executar, o pentester deve entender <b>CVE</b>, versões afetadas, vetor de ataque, impacto e trechos perigosos do script ou binário.",
                    "highlight": "Analisar primeiro evita comprometer o cliente e a própria credibilidade da equipe."
                },
                {
                    "type": "teach",
                    "icon": "fa-file-code",
                    "title": "Ghidra, Radare2, IDA e Debuggers",
                    "content": "Na engenharia reversa, <b>Ghidra</b> ajuda a descompilar e entender binários. Ferramentas como IDA, Radare2, GDB e OllyDbg apoiam inspeção de fluxo, memória, chamadas de sistema e comportamento em tempo de execução.",
                    "highlight": "Reversa responde a pergunta central: o que esse código realmente faz?"
                },
                {
                    "type": "example",
                    "icon": "fa-bug-slash",
                    "title": "Exemplo - Revisando um Exploit Antes do Uso",
                    "scenario": "O analista abre o código de um exploit público e percebe que, além da prova de conceito, ele cria um usuário administrativo persistente no alvo. A equipe decide remover esse trecho e validar o comportamento em laboratório antes do engajamento.",
                    "code": "# trecho suspeito encontrado no PoC\nsystem(\"useradd audit-backdoor && echo 'audit-backdoor:Temp123!' | chpasswd\")\n\n[i] Ajuste: remover payload persistente e testar apenas a exploração controlada",
                    "takeaway": "Ler e adaptar o código reduz risco operacional e evita efeitos colaterais fora do escopo."
                },
                {
                    "type": "match",
                    "title": "Associe a Ferramenta ao Papel",
                    "pairs": [
                        {
                            "term": "Ghidra",
                            "definition": "Descompilar e navegar em binários com apoio visual"
                        },
                        {
                            "term": "GDB",
                            "definition": "Depurar binários e observar execução em Linux"
                        },
                        {
                            "term": "Metasploit",
                            "definition": "Organizar módulos de exploração e payloads"
                        },
                        {
                            "term": "CVE",
                            "definition": "Identificador público de vulnerabilidade associada ao exploit"
                        }
                    ]
                },
                {
                    "type": "quiz",
                    "task": "Por que Ghidra é relevante para um pentester que analisa código ofensivo ou malware suspeito?",
                    "options": [
                        "Porque ajuda a descompilar binários e entender comportamento antes da execução",
                        "Porque substitui completamente a necessidade de validar o exploit em laboratório",
                        "Porque é uma ferramenta de captura de pacotes de rede em tempo real"
                    ],
                    "correctText": "Porque ajuda a descompilar binários e entender comportamento antes da execução",
                    "explanation": "Ghidra é valioso para leitura estrutural de binários, fluxo de funções e indícios de comportamento malicioso."
                },
                {
                    "type": "fill",
                    "sentence": "Na engenharia reversa aplicada ao pentest, ferramentas como ___ ajudam a abrir binários e inspecionar sua lógica antes que o código seja executado em produção.",
                    "options": [
                        "Ghidra",
                        "Hydra",
                        "Aircrack-ng"
                    ],
                    "correctText": "Ghidra",
                    "explanation": "Ghidra é um descompilador e analisador amplamente usado para estudar executáveis e malware."
                }
            ]
        }
    ]

    lessons.extend(module_10_lessons)
    save_json(JSON_PATH, lessons)
    print(f"Modulo 10 reestruturado com {len(module_10_lessons)} licoes.")


if __name__ == "__main__":
    main()
