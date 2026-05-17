# 🎮 Skill: CyberDuo Design System

Este documento define o padrão técnico, visual e didático para a criação de lições de fixação da plataforma CyberDuo, otimizadas para o aprendizado de Cibersegurança.

---

## 🏗️ Core Mandates (Princípios Fundamentais)

1.  **Mobile-First Absoluto:** O jogo deve ser 100% utilizável em celulares, usando `100dvh` para altura dinâmica e `clamp()` para tipografia fluida.
2.  **Estética Cyberpunk Dark:** Fundo `#05070a`, fontes *Inter* para leitura e *Fira Code* para dados técnicos.
3.  **Identidade Cromática por Trilha:** Cada módulo possui uma cor de destaque única para facilitar a navegação e o reconhecimento do tema:
    *   **Módulo 0 (Introdução):** Verde (#00ff41)
    *   **Módulo 1 (Hacking Ético):** Azul Cobalto (#2d5af5)
    *   **Módulo 2 (Planejamento):** Amarelo (#ffb800)
    *   **Módulo 3 (Coleta/Varredura):** Verde Água (#00facd)
    *   **Módulo 4 (Engenharia Social):** Roxo/Magenta (#ff00ff)
    *   **Módulo 5 (Redes):** Laranja (#ff8c00)
    *   **Módulo 6 (Web Apps):** Ciano Neon (#00f2ff)
    *   **Módulo 7 (Cloud/IoT):** Branco/Sutil (#e6edf3)
    *   **Módulo 8 (Pós-Exploração):** Vermelho (#ff003c)
    *   **Módulo 9 (Relatórios):** Esmeralda (#00ffa3)
    *   **Módulo 10 (Ferramentas):** Violeta (#8a2be2)
4.  **Foco em Certificação:** O conteúdo deve ser estritamente focado em conceitos teóricos e técnicos universais exigidos em provas de cursos e certificações.
5.  **Neutralidade de Contexto:** Não criar perguntas sobre nomes de empresas fictícias ou personas. O foco deve ser o **Skill Técnica**.
6.  **Profundidade Técnica e Exaustão:** Não há limite para a extensão de um módulo. Deve-se extrair **todos** os conceitos essenciais para provas de certificação (CompTIA, PenTest+, CEH, etc.) e as competências necessárias para a prática diária de um profissional de cibersegurança.
7.  **Foco em Resultados Práticos:** Cada lição deve ser uma preparação direta para o mercado de trabalho, priorizando comandos, metodologias reais e lógica de exploração.
8.  **UI Centralizada e Coesa:** Todos os botões de ação e overlays de feedback devem estar perfeitamente centralizados.
9.  **Resiliência (5 Vidas):** Cada lição fornece exatamente **5 corações** para suportar módulos longos e densos sem desmotivar o aluno.
10. **Nomenclatura de Temas (Header):** O cabeçalho sutil de cada fase (acima do título da skill) deve seguir obrigatoriamente o padrão: `X.Y • TEMA EM MAIÚSCULAS • Nível ${currentStep + 1}`. Exemplo: `6.4 • INJEÇÃO WEB • Nível 1`.
11. **Liberação de Módulo:** Ao finalizar a exaustão técnica de um módulo, deve-se obrigatoriamente:
    *   Atualizar o arquivo correspondente em `/modules/modulo-XX.html` removendo placeholders e listando as lições reais.
    *   Atualizar o arquivo `index.html` alterando o status do card de "Bloqueado" para "Ativo" e informando o número correto de lições.

---

## 🎨 Especificações de Design (CSS)

| Elemento | Propriedade/Valor | Motivo |
| :--- | :--- | :--- |
| **Variável de Cor** | `--cyber-blue` | Deve ser alterada de acordo com a Trilha definida nos Mandatos. |
| **Viewport** | `100dvh` | Evita que o botão "Verificar" suma sob a barra do navegador. |
| **Páginas Módulo** | `.module-name: 1.7rem` | Hierarquia elegante na navegação. |
| **Header de Nível** | `font-size: 0.6rem; font-weight: 900;` | Texto sutil mas legível para o Tema da Lição. |
| **Lições: Título** | `.question-title: 1.05rem` | Maior clareza na pergunta. |
| **Lições: Texto** | `.concept-desc: 0.95rem` | **Legibilidade otimizada para estudo denso.** |
| **Lições: Opções** | `.option-card: 0.95rem` | Facilita o toque (mobile) e a leitura. |
| **Feedback Overlay** | `display: flex; align-items: center; justify-content: center;` | Garante centralização absoluta do botão "Continuar". |
| **Footer Action** | `max-width: 400px; margin: 0 auto;` | Centraliza o botão principal. |
| **Bordas Neon** | `1px solid var(--cyber-blue)` | Cria o efeito de identidade do módulo. |
| **Botões** | `border-bottom-width: 4px` | Sensação tátil de "click" (padrão Duolingo). |

---

## 📊 Estrutura de Dados (JSON)

Para replicar o jogo em um novo módulo, o array `steps` deve substituir a antiga lógica de quizzes puros, usando 5 tipos de interações para criar uma aula rica e interativa no estilo Duolingo.

```javascript
const steps = [
    // Tipo TEACH — Tela de ensino (sem pergunta)
    {
        type: 'teach',
        icon: 'fa-shield-halved', // Ícone FontAwesome
        title: 'Segurança Ofensiva',
        content: 'O <b>Red Team</b> ataca de forma simulada para encontrar falhas. O <b>Blue Team</b> usa esse conhecimento para defender e melhorar os sistemas.',
        highlight: 'Segurança Ofensiva' // Texto opcional destacado no rodapé do card
    },
    // Tipo EXAMPLE — Exemplo prático
    {
        type: 'example',
        icon: 'fa-terminal',
        title: 'Na Prática',
        scenario: 'Descrição de um cenário real ou uso prático.',
        code: 'nmap -sV -p 80 banco.com', // Opcional: Bloco de código/comando simulado
        takeaway: 'Resumo ou lição principal deste exemplo.'
    },
    // Tipo QUIZ — Múltipla escolha
    {
        type: 'quiz',
        task: 'Pergunta que induz o raciocínio técnico?',
        options: [
            'Opção errada 1',
            'Opção correta (idêntica ao correctText)',
            'Opção errada 2'
        ],
        correctText: 'Opção correta (texto exato)',
        explanation: 'O "porquê" da resposta ser esta, focado em gravar na mente.'
    },
    // Tipo FILL — Completar a frase
    {
        type: 'fill',
        sentence: 'O ___ ataca de forma simulada para encontrar falhas.', // Use ___ para representar o espaço em branco
        options: ['Red Team', 'Blue Team', 'Firewall'],
        correctText: 'Red Team',
        explanation: 'Red team é a equipe ofensiva.'
    },
    // Tipo MATCH — Associação de pares
    {
        type: 'match',
        title: 'Associe os Termos',
        pairs: [
            { term: 'Red Team', definition: 'Simula ataques para achar falhas' },
            { term: 'Blue Team', definition: 'Defende sistemas e monitora' },
            { term: 'Hacker Ético', definition: 'Ataca com autorização' }
        ]
    }
];
```

---

## ⚙️ Lógica de Motor (JS)

Para manter a qualidade e as mecânicas, o motor de `render()` deve suportar:

1.  **Renderização Dinâmica:** Despachar layouts diferentes de acordo com o `step.type` (`teach`, `example`, `quiz`, `fill`, `match`).
2.  **Shuffle (Aleatoriedade):** Algoritmo de Fisher-Yates para embaralhar o array de opções (`quiz` e `fill`) e os arrays de pares (`match`) a cada renderização.
3.  **Validação por Texto:** No caso de `quiz` e `fill`, comparar `shuffledOptions[selectedIdx] === correctText` em vez de índices fixos (evita vício de posição).
4.  **Corações Imunes:** Telas do tipo `teach` e `example` apenas avançam, e NUNCA retiram corações ou exigem verificação de feedback.
5.  **Scroll Reset:** `area.scrollTop = 0` em cada nova lição para garantir que o usuário veja o topo do card.
6.  **Lives Management:** Decrementar corações no erro (para `quiz`, `fill`, e associações incorretas em `match`) e disparar `location.reload()` (Game Over) se chegar a zero.

---

## 🚀 Como Replicar em Novos Módulos

1.  **Entrada de Dados (HTML/Texto):** O conteúdo base pode ser enviado via chat ou **colocado diretamente na pasta `/content/`** (ex: salvos via SingleFile).
2.  **Extração Autônoma:** Quando arquivos HTML externos forem fornecidos em `/content/`, utilizar ferramentas como `grep`, `run_shell_command` ou `read_file` para identificar os blocos de texto pedagógico (`<p>`, `<li>`, `<strong>`), filtrando scripts e estilos irrelevantes.
3.  **Filtragem de Conteúdo:** Seguir rigorosamente o mandato de **Foco em Certificação** e **Neutralidade de Contexto**, removendo nomes de empresas ou laboratórios fictícios durante a extração.
4.  **Transformação Didática:** Identificar os tópicos principais no texto e formatá-los no novo modelo de fluxo didático: **Ensinar (`teach`) -> Exemplificar (`example`) -> Testar (`quiz`, `fill` ou `match`)**.
5.  **Boilerplate & Injeção:** Utilizar o novo template HTML/CSS padrão de interações Duolingo (baseado na lição 0.0) e substituir o array `steps`.

---

### 🎨 Paleta de Cores Recomendada
*   `--cyber-blue`: `#00f2ff` (Protocolos/IDs)
*   `--cyber-green`: `#00ff41` (Sucesso/Defesa)
*   `--cyber-red`: `#ff003c` (Riscos/Erros)
*   `--cyber-yellow`: `#ffb800` (Atenção/Mecânicas)
