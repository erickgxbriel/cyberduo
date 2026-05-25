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
    lessons = [lesson for lesson in lessons if lesson.get("module") != "9"]

    module_9_lessons = [
        {
            "filename": "9.0-introducao.html",
            "module": "9",
            "title": "Por Que o Relatório Decide o Valor do Pentest",
            "victory_title": "Excelente!",
            "victory_msg": "RELATÓRIO INICIADO!",
            "steps": [
                {
                    "type": "teach",
                    "icon": "fa-file-signature",
                    "title": "O Entregável Que Fecha o Engajamento (Cisco 9.0.1)",
                    "content": "Depois de executar reconhecimento, exploração e validação, ainda falta a fase mais importante: o <b>relatório final</b>. Esse report é um dos principais <b>entregáveis</b> do engajamento e permite ao cliente entender as descobertas, priorizar correções e perceber o valor do projeto.",
                    "highlight": "Sem relatório de qualidade, o pentest perde grande parte do seu valor de negócio."
                },
                {
                    "type": "teach",
                    "icon": "fa-notes-medical",
                    "title": "Documentação Contínua Evita Lacunas Críticas (Cisco 9.0.1)",
                    "content": "Durante o teste, cada evidência precisa ser registrada: comandos executados, horários, vulnerabilidades, credenciais de teste, logs e caminhos de exploração. Essa <b>documentação</b> sustenta o relatório. Se você confiar apenas na memória, será difícil reconstruir tudo com precisão na hora de redigir o documento.",
                    "highlight": "Anote enquanto testa, não depois."
                },
                {
                    "type": "example",
                    "icon": "fa-terminal",
                    "title": "Exemplo - Evidência Registrada no Momento Certo",
                    "scenario": "Um pentester encontra um painel administrativo exposto e registra imediatamente o caminho, a prova de acesso e o impacto técnico para usar depois no relatório:",
                    "code": "[i] Host: portal.pixelparadise.local\n[i] URL: https://portal.pixelparadise.local/admin\n[+] Credencial válida de teste: auditor:Winter2026!\n[+] Impacto: acesso a exportação de dados de clientes\n[$] screenshot salvo em evidencias/admin-panel.png",
                    "takeaway": "Registrar evidências no momento da descoberta evita omissões e fortalece a credibilidade do relatório."
                },
                {
                    "type": "quiz",
                    "task": "Qual é o principal motivo para tratar o relatório final como a etapa mais importante do engajamento?",
                    "options": [
                        "Porque é o documento que transforma achados técnicos em ações que o cliente pode executar",
                        "Porque ele substitui completamente a necessidade de validar vulnerabilidades",
                        "Porque ele elimina a necessidade de reuniões e comunicação com o cliente"
                    ],
                    "correctText": "Porque é o documento que transforma achados técnicos em ações que o cliente pode executar",
                    "explanation": "O relatório é o elo entre a execução técnica do pentest e a remediação real no ambiente do cliente."
                },
                {
                    "type": "fill",
                    "sentence": "Esquecer comandos, evidências e caminhos de exploração é um risco comum quando o pentester não mantém a ___ durante todo o teste.",
                    "options": [
                        "documentação",
                        "ofuscação",
                        "segmentação"
                    ],
                    "correctText": "documentação",
                    "explanation": "Documentação contínua garante rastreabilidade, qualidade de relatório e respaldo técnico."
                }
            ]
        },
        {
            "filename": "9.1a-componentes-distribuicao.html",
            "module": "9",
            "title": "Público, Estrutura, CVSS e Distribuição Segura",
            "victory_title": "Excelente!",
            "victory_msg": "ESTRUTURA DOMINADA!",
            "steps": [
                {
                    "type": "teach",
                    "icon": "fa-users",
                    "title": "Dois Públicos, Duas Linguagens (Cisco 9.1.1)",
                    "content": "Um bom relatório precisa falar com o <b>público executivo</b> e com o <b>público técnico</b>. O resumo executivo traduz risco em impacto para o negócio. Já as seções técnicas precisam trazer detalhes suficientes para que TI, segurança, desenvolvimento ou terceiros consigam reproduzir e corrigir a falha.",
                    "highlight": "Executivos precisam de contexto; equipes técnicas precisam de evidência e passos claros."
                },
                {
                    "type": "teach",
                    "icon": "fa-list-check",
                    "title": "Componentes Clássicos do Relatório (Cisco 9.1.2)",
                    "content": "Entre os componentes mais comuns estão: <b>carta de apresentação</b>, <b>sumário executivo</b>, escopo, metodologia, resumo de risco, descobertas detalhadas, recomendações, conclusão e apêndices. A estrutura pode variar, mas a lógica permanece a mesma: orientar decisão e remediação.",
                    "highlight": "Estrutura consistente reduz ruído e acelera a resposta do cliente."
                },
                {
                    "type": "teach",
                    "icon": "fa-gauge-high",
                    "title": "CVE, CVSS e Priorização (Cisco 9.1.3)",
                    "content": "Ao relatar uma vulnerabilidade, o pentester pode referenciar <b>CVE</b> para identificação pública e usar <b>CVSS</b> para classificar gravidade. O CVSS combina métricas <b>Base</b>, <b>Temporais</b> e <b>Ambientais</b>, permitindo ajustar a nota ao cenário real do cliente.",
                    "highlight": "A pontuação só é útil quando reflete o ambiente real, não apenas a teoria."
                },
                {
                    "type": "example",
                    "icon": "fa-file-shield",
                    "title": "Exemplo - Mesma Falha, Públicos Diferentes",
                    "scenario": "Uma injeção SQL encontrada em um portal financeiro precisa ser descrita de forma diferente no resumo executivo e na seção técnica:",
                    "code": "[Executivo] A aplicação permite acesso não autorizado a dados financeiros, com risco de fraude e vazamento regulatório.\n\n[Técnico] O parâmetro 'invoice_id' aceita payloads UNION sem parametrização. Prova: 'invoice_id=14 UNION SELECT user(),database(),version()-- -'.",
                    "takeaway": "A mesma descoberta deve ser comunicada em níveis diferentes de profundidade, sem perder precisão."
                },
                {
                    "type": "match",
                    "title": "Associe o Conceito ao Objetivo",
                    "pairs": [
                        {
                            "term": "Resumo Executivo",
                            "definition": "Explicar impacto de negócio sem excesso de jargão técnico"
                        },
                        {
                            "term": "Seção Técnica",
                            "definition": "Trazer evidências, reprodução e recomendações detalhadas"
                        },
                        {
                            "term": "CVE",
                            "definition": "Identificador público de uma vulnerabilidade conhecida"
                        },
                        {
                            "term": "CVSS Ambiental",
                            "definition": "Ajustar a gravidade com base no contexto do cliente"
                        }
                    ]
                },
                {
                    "type": "quiz",
                    "task": "Qual prática atende melhor à distribuição segura de um relatório de pentest?",
                    "options": [
                        "Criptografar arquivos e controlar quem recebeu cada cópia física ou digital",
                        "Enviar o PDF em texto simples por e-mail para agilizar a leitura",
                        "Publicar o relatório em um compartilhamento aberto para todas as áreas"
                    ],
                    "correctText": "Criptografar arquivos e controlar quem recebeu cada cópia física ou digital",
                    "explanation": "O relatório contém instruções detalhadas de exploração e precisa de proteção tanto no armazenamento quanto na distribuição."
                },
                {
                    "type": "fill",
                    "sentence": "No CVSS, as métricas ___ permitem adaptar a pontuação ao risco real e à superfície de ameaça específica do cliente.",
                    "options": [
                        "ambientais",
                        "binárias",
                        "aleatórias"
                    ],
                    "correctText": "ambientais",
                    "explanation": "As métricas ambientais contextualizam a gravidade no ambiente avaliado."
                }
            ]
        },
        {
            "filename": "9.1b-notas-causa-raiz.html",
            "module": "9",
            "title": "Notas de Campo, Dradis e Causa Raiz",
            "victory_title": "Excelente!",
            "victory_msg": "CAUSA RAIZ IDENTIFICADA!",
            "steps": [
                {
                    "type": "teach",
                    "icon": "fa-book-open",
                    "title": "Gerenciar Notas Também Faz Parte do Pentest (Cisco 9.1.4)",
                    "content": "Um engajamento gera muitas evidências: saídas de scanners, comandos, screenshots, credenciais temporárias, hashes, requests, respostas e observações contextuais. Sem organização, a qualidade do relatório cai e o trabalho em equipe fica frágil.",
                    "highlight": "Notas desorganizadas geram relatórios incompletos."
                },
                {
                    "type": "teach",
                    "icon": "fa-diagram-project",
                    "title": "Dradis e Espaço Colaborativo (Cisco 9.1.6)",
                    "content": "O <b>Dradis Framework</b> foi criado para centralizar notas, importar resultados de ferramentas e facilitar colaboração. A <b>Community Edition</b> é aberta e extensível; a <b>Professional Edition</b> adiciona recursos mais fortes de projeto e geração de relatórios.",
                    "highlight": "Ferramenta de notas boa reduz retrabalho e melhora consistência."
                },
                {
                    "type": "teach",
                    "icon": "fa-magnifying-glass-chart",
                    "title": "Analisar Causa Raiz Vai Além do Scanner (Cisco 9.1.7)",
                    "content": "Um scanner pode mostrar uma porta 21 aberta, mas isso não explica o risco real. A <b>causa raiz</b> aparece quando o pentester correlaciona descoberta técnica, contexto operacional e entrevistas com o dono do ativo. É isso que transforma sintoma em correção útil.",
                    "highlight": "Relatório forte explica por que o problema existe, não apenas onde ele aparece."
                },
                {
                    "type": "example",
                    "icon": "fa-folder-tree",
                    "title": "Exemplo - FTP Legado e Exposição Indevida",
                    "scenario": "Durante o teste, o scanner não marcou criticidade alta no FTP, mas a investigação manual mostrou um problema maior:",
                    "code": "[i] Nessus: porta 21 aberta sem CVE crítico associado\n[i] Entrevista com o responsável: serviço deveria ter sido desativado há anos\n[+] Evidência adicional: servidor exposto à internet\n[+] Logs indicam uso contínuo para transferir dados sensíveis",
                    "takeaway": "A causa raiz não era apenas o FTP ativo, mas falha de governança, descomissionamento e uso inseguro do serviço."
                },
                {
                    "type": "quiz",
                    "task": "Qual ação ajuda mais a determinar a causa raiz de um servidor não documentado exposto à internet?",
                    "options": [
                        "Entrevistar os responsáveis pelo ativo e correlacionar o uso real com as evidências técnicas",
                        "Confiar apenas na severidade automática do scanner de vulnerabilidade",
                        "Ignorar o contexto operacional para evitar aumentar o escopo"
                    ],
                    "correctText": "Entrevistar os responsáveis pelo ativo e correlacionar o uso real com as evidências técnicas",
                    "explanation": "Causa raiz exige contexto de negócio e operação, não só telemetria técnica."
                },
                {
                    "type": "quiz",
                    "task": "Por que a validação manual das saídas de ferramentas é obrigatória antes de publicar achados?",
                    "options": [
                        "Porque falsos positivos custam tempo, dinheiro e credibilidade",
                        "Porque scanners nunca encontram nenhuma vulnerabilidade útil",
                        "Porque relatórios só podem conter evidências coletadas manualmente"
                    ],
                    "correctText": "Porque falsos positivos custam tempo, dinheiro e credibilidade",
                    "explanation": "Achados não validados podem induzir o cliente a corrigir um problema inexistente."
                },
                {
                    "type": "fill",
                    "sentence": "Quando o pentester investiga o motivo estrutural de uma falha, ele está realizando uma análise de ___.",
                    "options": [
                        "causa raiz",
                        "superfície externa",
                        "porta padrão"
                    ],
                    "correctText": "causa raiz",
                    "explanation": "A análise de causa raiz conecta vulnerabilidade, processo e contexto operacional."
                }
            ]
        },
        {
            "filename": "9.2a-controles-remediacao.html",
            "module": "9",
            "title": "Achados, Recomendações e Controles de Remediação",
            "victory_title": "Excelente!",
            "victory_msg": "REMEDIAÇÃO MAPEADA!",
            "steps": [
                {
                    "type": "teach",
                    "icon": "fa-screwdriver-wrench",
                    "title": "Boa Recomendação Precisa Ser Executável (Cisco 9.2.1)",
                    "content": "Descobertas devem terminar com <b>ações de remediação claras</b>. Não basta escrever 'corrigir'. O relatório precisa indicar o que mudar, em qual camada, qual risco reduz e, quando possível, qual prioridade aplicar.",
                    "highlight": "Achado útil sempre aponta um caminho de correção."
                },
                {
                    "type": "teach",
                    "icon": "fa-shield-halved",
                    "title": "Controles Técnicos, Administrativos, Operacionais e Físicos (Cisco 9.2.2)",
                    "content": "As recomendações podem envolver <b>controles técnicos</b> como MFA, hardening e parametrização de consultas; <b>controles administrativos</b> como RBAC e políticas; <b>controles operacionais</b> como treinamento e segregação de funções; e <b>controles físicos</b> como mantraps, câmeras e biometria.",
                    "highlight": "Nem toda correção é tecnológica; muitas dependem de processo e governança."
                },
                {
                    "type": "teach",
                    "icon": "fa-network-wired",
                    "title": "Zero Trust e Redução de Movimento Lateral (Cisco 9.2.2)",
                    "content": "A Cisco destaca o uso de <b>microsegmentação Zero Trust</b> para controlar tráfego leste-oeste próximo à carga de trabalho. Isso limita o movimento lateral e melhora a contenção quando uma máquina ou aplicação é comprometida.",
                    "highlight": "Segmentar perto da aplicação reduz blast radius."
                },
                {
                    "type": "example",
                    "icon": "fa-code",
                    "title": "Exemplo - Recomendação para SQL Injection",
                    "scenario": "Após validar uma falha de SQL Injection em um formulário de cobrança, o relatório técnico pode orientar a correção de forma objetiva:",
                    "code": "Achado: entrada 'invoice_id' aceita payload SQL arbitrário.\nRecomendação técnica: implementar consultas parametrizadas e validação server-side.\nRecomendação administrativa: incluir revisão de segurança no SDLC.\nPrioridade: alta, por risco de vazamento financeiro.",
                    "takeaway": "Uma remediação forte combina correção técnica imediata com prevenção de recorrência."
                },
                {
                    "type": "match",
                    "title": "Associe o Controle ao Exemplo",
                    "pairs": [
                        {
                            "term": "Técnico",
                            "definition": "MFA, hardening e consultas parametrizadas"
                        },
                        {
                            "term": "Administrativo",
                            "definition": "RBAC, política de senha e Secure SDLC"
                        },
                        {
                            "term": "Operacional",
                            "definition": "Treinamento, férias obrigatórias e job rotation"
                        },
                        {
                            "term": "Físico",
                            "definition": "Biometria, câmeras e mantraps"
                        }
                    ]
                },
                {
                    "type": "quiz",
                    "task": "Qual recomendação reduz melhor o risco de movimento lateral após o comprometimento de uma carga de trabalho?",
                    "options": [
                        "Aplicar microsegmentação alinhada a uma arquitetura Zero Trust",
                        "Aumentar apenas o tamanho do storage do servidor",
                        "Remover os logs para melhorar a performance da aplicação"
                    ],
                    "correctText": "Aplicar microsegmentação alinhada a uma arquitetura Zero Trust",
                    "explanation": "A microsegmentação restringe o tráfego entre cargas de trabalho e reduz o impacto de uma intrusão."
                },
                {
                    "type": "fill",
                    "sentence": "Para impedir que dados de entrada sejam executados como comandos SQL, o relatório deve recomendar a ___ das consultas.",
                    "options": [
                        "parametrização",
                        "compressão",
                        "replicação"
                    ],
                    "correctText": "parametrização",
                    "explanation": "Consultas parametrizadas separam dados de instruções SQL e reduzem o risco de injeção."
                }
            ]
        },
        {
            "filename": "9.2b-comunicacao-pos-entrega.html",
            "module": "9",
            "title": "Comunicação Durante o Teste e Encerramento Seguro",
            "victory_title": "Excelente!",
            "victory_msg": "ENGAJAMENTO FINALIZADO!",
            "steps": [
                {
                    "type": "teach",
                    "icon": "fa-comments",
                    "title": "Quando Comunicar Antes do Relatório Final (Cisco 9.2.3)",
                    "content": "Nem toda descoberta deve esperar o relatório. Se você encontrar uma <b>falha crítica</b> com impacto imediato, comunique rapidamente ao cliente. Se houver indício de comprometimento real pré-existente, a simulação deve parar e o caso precisa ser escalado para resposta a incidentes. Essas <b>atividades pós</b> e de escalonamento precisam estar previstas no processo.",
                    "highlight": "Achado crítico e incidente real exigem comunicação imediata."
                },
                {
                    "type": "teach",
                    "icon": "fa-handshake-angle",
                    "title": "Comunicação Sem Arrogância (Cisco 9.1.1 e 9.2.3)",
                    "content": "O relatório e o debriefing devem preservar um tom <b>profissional e respeitoso</b>. O objetivo não é constranger a equipe do cliente, mas ajudá-la a entender o risco, priorizar ações e melhorar a postura de segurança.",
                    "highlight": "Relatório bom corrige problemas sem criar atrito desnecessário."
                },
                {
                    "type": "teach",
                    "icon": "fa-broom-ball",
                    "title": "Pós-Entrega e Limpeza do Ambiente (Cisco 9.2.4)",
                    "content": "No encerramento do engajamento, o pentester deve remover shells reversos, contas criadas, scripts, serviços persistentes e qualquer alteração temporária. Depois disso, realiza-se a sanitização segura dos dados do cliente armazenados nas estações do time, seguindo boas práticas como <b>NIST SP 800-88</b>.",
                    "highlight": "Sair do ambiente com segurança é parte do trabalho."
                },
                {
                    "type": "example",
                    "icon": "fa-terminal",
                    "title": "Exemplo - Encerramento Pós-Engajamento",
                    "scenario": "Antes do sign-off, a equipe registra a remoção dos artefatos deixados durante o teste e a exclusão do material coletado:",
                    "code": "[+] Conta temporária removida: audit_tmp\n[+] Serviço persistente removido: updaterd.service\n[+] Web shell apagada: /var/www/html/tmp/shell.php\n[+] Dados do cliente sanitizados do notebook de teste\n[i] Referência adotada: NIST SP 800-88",
                    "takeaway": "A limpeza final protege o cliente e reduz o risco de deixar novas portas abertas no ambiente."
                },
                {
                    "type": "match",
                    "title": "Associe a Atividade ao Objetivo",
                    "pairs": [
                        {
                            "term": "Debriefing",
                            "definition": "Apresentar verbalmente achados, impacto e próximos passos"
                        },
                        {
                            "term": "Retest",
                            "definition": "Validar se a remediação corrigiu a vulnerabilidade"
                        },
                        {
                            "term": "Limpeza pós-engajamento",
                            "definition": "Remover contas, shells, serviços e artefatos deixados"
                        },
                        {
                            "term": "Sanitização de mídia",
                            "definition": "Excluir com segurança os dados sensíveis coletados"
                        }
                    ]
                },
                {
                    "type": "quiz",
                    "task": "Qual deve ser a reação do pentester ao encontrar um backdoor ativo deixado por um invasor real durante o teste?",
                    "options": [
                        "Parar o engajamento simulado e escalar imediatamente para a equipe de resposta a incidentes",
                        "Explorar o backdoor em silêncio e só mencionar o caso no apêndice",
                        "Manter o teste normalmente para não atrasar a entrega"
                    ],
                    "correctText": "Parar o engajamento simulado e escalar imediatamente para a equipe de resposta a incidentes",
                    "explanation": "Quando há evidência de incidente real, a prioridade muda de simulação para contenção e resposta."
                },
                {
                    "type": "fill",
                    "sentence": "A remoção de shells, usuários temporários e serviços criados durante o teste faz parte da etapa de ___ pós-engajamento.",
                    "options": [
                        "limpeza",
                        "enumeração",
                        "persistência"
                    ],
                    "correctText": "limpeza",
                    "explanation": "A limpeza pós-engajamento restaura o ambiente e evita riscos residuais deixados pelo próprio teste."
                }
            ]
        }
    ]

    lessons.extend(module_9_lessons)
    save_json(JSON_PATH, lessons)
    print(f"Modulo 9 reestruturado com {len(module_9_lessons)} licoes.")


if __name__ == "__main__":
    main()
