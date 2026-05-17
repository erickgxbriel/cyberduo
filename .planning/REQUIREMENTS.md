# Requirements

## 1. Core Workflow
- O Motor de Lições deve suportar a estrutura do `CYBER_DUO_SKILL.md` com `step.type` variando em `teach`, `example`, `quiz`, `match`, `fill`.
- O layout de todos os módulos (`lessons/1.0-modulo.html` a `10.0-modulo.html`) deve espelhar o boilerplate base criado em `0.0-boas-vindas.html`.

## 2. Conteúdo
- Todo material na pasta `/content/` deve ser transcrito, usando inteligência artificial, para se encaixar na lógica do Motor de Lições.
- As informações fictícias e contextos de laboratórios devem ser purgadas, mantendo neutralidade de contexto.
- Os tópicos textuais extensos devem ser decompostos em passos: ensinar -> exemplificar -> testar.

## 3. UI/UX
- A temática de cores dos módulos deve ser respeitada em todos os overlays, borders e opções selecionadas (ex: `#2d5af5` no módulo 1, `#ffb800` no módulo 2).
- Os corações (`vidas`) devem ser mantidos congelados durante as transições de telas puramente educacionais (`teach` e `example`).

## 4. Cobertura de Conceitos (Phase 2)
- Cada subseção numerada no material fonte (ex: 7.2.1, 7.2.2, ..., 7.2.16) deve ter pelo menos 1 step `teach` dedicado nas lições.
- Conceitos que aparecem nas "Práticas" do curso devem ser OBRIGATORIAMENTE cobertos, pois o aluno precisa deles para responder.
- Quando uma lição ficar muito longa (>20 steps), ela deve ser dividida em múltiplas lições (ex: `7.2a`, `7.2b`).
