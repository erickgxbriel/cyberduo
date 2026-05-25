# Guia Metodológico de Reestruturação de Módulos (Cisco ➔ CyberDuo)

Este documento atua como o manual técnico e pedagógico para reestruturar e modularizar qualquer módulo do **CyberDuo** com base no currículo oficial da Cisco. Ele garante consistência conceitual, profundidade didática, interatividade cyberpunk e automação no pipeline de compilação.

---

## 1. Visão Geral do Fluxo Didático (Microlearning)

O princípio fundamental do CyberDuo é o **Microlearning de Alta Retenção**. Não empilhamos conteúdo extenso em slides intermináveis. Dividimos cada tópico principal em sub-lições menores (ex: `X.1a`, `X.1b`), onde cada lição é governada pela tríade pedagógica:

1.  **TEORIA (Teach)**: Conceitos teóricos explicados de forma limpa, direta e visual, com termos de destaque em negrito (`<b>`) e alertas de iluminação/dicas (`highlight`).
2.  **EXEMPLO PRÁTICO (Example)**: Um cenário do mundo real do mercado ou de certificações (como PenTest+), incluindo logs de terminal, scripts, payloads ou códigos reais (`code`) e uma conclusão chave (`takeaway`).
3.  **FIXAÇÃO INTERATIVA (Quiz / Fill / Match)**:
    *   **Quiz**: Perguntas com múltiplas opções para avaliar a compreensão direta do conceito.
    *   **Fill (Preenchimento)**: Sentenças com lacunas (`___`) onde o aluno preenche com o termo técnico correto, ideal para fixar comandos ou definições.
    *   **Match (Associação)**: Um painel de pares (4 termos e 4 definições correspondentes) ideal para mapear ferramentas, protocolos, portas ou conceitos.

---

## 2. Passo a Passo da Reestruturação Técnica

Para migrar/atualizar qualquer módulo, siga rigorosamente as seguintes fases:

### Fase A: Preparação e Coleta do Conteúdo Bruto
1.  **Verifique a Extração**: O material do curso original deve estar extraído da pasta `/content` para a pasta `/extracted`. Se necessário, rode o script extrator:
    ```bash
    python3 scripts/extract_content.py
    ```
2.  **Mapeie o Contexto Consolidade**: Acesse o arquivo `/extracted/modulo_XX_context.txt` para ler a ementa do módulo desejado, identificando as seções da Cisco (ex: `8.1.1`, `8.1.2`, etc.) e os termos técnicos críticos.

### Fase B: Projeto de Divisão das Aulas (Modularização)
Mapeie a divisão ideal de arquivos estáticos. Evite colocar mais de 10-12 passos (steps) por arquivo HTML. 
*   **Aulas de Introdução (X.0)**: Geralmente são curtas, abordando a motivação (`Por que fazer?`) e objetivos (`O que aprenderei?`).
*   **Divisão de Tópicos Densos (X.1, X.2)**: Divida em sufixos `a` e `b` agrupando conceitos complementares (ex: se o tópico aborda Shells e C2, divida-o em `X.1a-shells-c2` e a continuação técnica em `X.1b-persistencia-avancada`).

### Fase C: Criação do Script de Definições Python (`modX.py`)
Para manter a robustez do banco de definições, nunca edite o `lesson_definitions.json` manualmente. Em vez disso, crie ou edite um script Python (ex: `scripts/mod8.py`) que automatiza a alteração do JSON:

```python
import json

# 1. Carregar JSON atual
PATH = '/home/gabriel/Documentos/dev/cyberduo/scripts/lesson_definitions.json'
with open(PATH, 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# 2. Filtrar e remover definições antigas daquele módulo para evitar duplicatas
lessons = [l for l in lessons if l['module'] != '8']

# 3. Adicionar novas lições
lessons.extend([
  {
    "filename": "8.0-introducao.html",
    "module": "8",
    "title": "Título da Lição",
    "victory_msg": "MENSAGEM DE VITÓRIA!",
    "steps": [
      {
        "type": "teach",
        "icon": "fa-shield-halved",
        "title": "Título do Slide",
        "content": "Conteúdo formatado com HTML básico: <b>termo</b> e quebras de linha.",
        "highlight": "Mensagem destacada em lâmpada."
      },
      {
        "type": "quiz",
        "task": "Pergunta?",
        "options": ["Opção Correta", "Opção Errada 1", "Opção Errada 2"],
        "correctText": "Opção Correta",
        "explanation": "Explicação pedagógica mostrada no feedback."
      }
    ]
  }
])

# 4. Salvar JSON de volta
with open(PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, ensure_ascii=False, indent=2)
```

### Fase D: Compilação das Aulas (Geração Estática)
Rode o compilador para processar as definições do JSON e gerar as páginas HTML interativas completas na pasta `/lessons`:
```bash
python3 scripts/generate_lessons.py
```
*Este script cuidará de importar o template padrão, injetar a lógica de controle de vidas (hearts), aplicar a paleta cyberpunk correta para a trilha do módulo e linkar o botão 'PRÓXIMA LIÇÃO' automaticamente de forma sequencial.*

### Fase E: Geração das Rotas do Hub (`update_modules.py`)
Rode o script roteador para reescrever as listas de links do índice dos módulos automaticamente:
```bash
python3 scripts/update_modules.py
```
*Isso garante que `modules/modulo-XX.html` exiba todos os links corretos de forma responsiva, com descrições curtas e ícones correspondentes.*

### Fase F: Auditoria de Cobertura e Qualidade
1.  **Audite a Cobertura**: Rode o script de auditoria para certificar-se de que nenhum conceito crítico foi omitido:
    ```bash
    python3 scripts/audit_coverage.py
    ```
2.  **Sincronização Inversa**: Se realizar qualquer ajuste direto no código HTML de lições na pasta `lessons/` (como ajustes rápidos de CSS ou correções ortográficas), rode o sincronizador para espelhar as alterações de volta no JSON:
    ```bash
    python3 scripts/sync_html_to_json.py
    ```

---

## 3. Diretrizes de Design Cyberpunk (Aesthetics)
Ao formular o conteúdo e interações, mantenha a linguagem visual cyberpunk do CyberDuo:
*   **Cores do Módulo**: Cada trilha possui sua própria variável de cor (ex: Módulo 8 usa vermelho `--cyber-red: #ff003c` com sombra `#b3002a`).
*   **Tags HTML Permitidas**: Use `<b>`, `<i>`, `<br>`, `•`, e tags de estilização simples para formatar o texto do conteúdo didático.
    > [!WARNING]
    > **NÃO utilize a sintaxe de asteriscos do Markdown (`**texto**`) para negrito!**
    > O renderizador frontend do CyberDuo não interpreta a formatação de texto em Markdown, fazendo com que os asteriscos sejam exibidos de forma literal na tela do usuário. Use sempre a tag HTML padrão `<b>texto</b>` para destacar termos em negrito.
*   **Códigos de Terminal**: Mantenha no formato Unix/Kali real. Use tags como `[i]` para info, `[+]` para sucesso e `[$]` para comandos executados.
