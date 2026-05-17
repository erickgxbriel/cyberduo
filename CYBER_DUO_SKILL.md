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

Para replicar o jogo em um novo módulo, o array `phases` deve seguir este esquema:

```javascript
const phases = [
    {
        icon: 'fa-lock', // Ícone FontAwesome
        concept: 'Nome da Skill', // Ex: "Criptografia de Chave"
        desc: 'Explicação curta com <span class="highlight-cyan">termos coloridos</span>.', 
        task: 'Pergunta que induz o raciocínio técnico?',
        options: [
            'Opção errada 1',
            'Opção correta (idêntica ao correctText)',
            'Opção errada 2'
        ],
        correctText: 'Opção correta (texto exato)',
        explanation: 'O "porquê" da resposta ser esta, focado em gravar na mente.'
    }
];
```

---

## ⚙️ Lógica de Motor (JS)

Para manter a qualidade, o motor deve implementar:

1.  **Shuffle (Aleatoriedade):** Algoritmo de Fisher-Yates para embaralhar o array de opções a cada renderização.
2.  **Validação por Texto:** Comparar `selectedOptionText === correctText` em vez de índices fixos (evita vício de posição).
3.  **Scroll Reset:** `area.scrollTop = 0` in cada nova lição para garantir que o usuário veja o topo do card.
4.  **Lives Management:** Decrementar corações no erro e disparar `location.reload()` (Game Over) se chegar a zero.

---

## 🚀 Como Replicar em Novos Módulos

1.  **Entrada de Dados (HTML/Texto):** O conteúdo base pode ser enviado via chat ou **colocado diretamente na pasta `/content/`** (ex: salvos via SingleFile).
2.  **Extração Autônoma:** Quando arquivos HTML externos forem fornecidos em `/content/`, utilizar ferramentas como `grep`, `run_shell_command` ou `read_file` para identificar os blocos de texto pedagógico (`<p>`, `<li>`, `<strong>`), filtrando scripts e estilos irrelevantes.
3.  **Filtragem de Conteúdo:** Seguir rigorosamente o mandato de **Foco em Certificação** e **Neutralidade de Contexto**, removendo nomes de empresas ou laboratórios fictícios durante a extração.
4.  **Transformação Didática:** Identificar os tópicos principais no texto (do básico ao avançado) e converter cada tópico em uma lição visual (Card + Pergunta Explicativa) focada em fixação.
5.  **Boilerplate & Injeção:** Utilizar o template HTML/CSS padrão (baseado no Módulo 6) e substituir o array `phases`.

---

### 🎨 Paleta de Cores Recomendada
*   `--cyber-blue`: `#00f2ff` (Protocolos/IDs)
*   `--cyber-green`: `#00ff41` (Sucesso/Defesa)
*   `--cyber-red`: `#ff003c` (Riscos/Erros)
*   `--cyber-yellow`: `#ffb800` (Atenção/Mecânicas)
