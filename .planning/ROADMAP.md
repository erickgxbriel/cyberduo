# GSD Roadmap: CyberDuo 🛡️🔥

Este documento gerencia as fases de desenvolvimento, priorizando a execução focada (GSD). As fases concluídas foram arquivadas/resumidas para limpar o escopo.

---

## ✅ FASES CONCLUÍDAS (Histórico Recente)

- **Phase 1:** Migração para Motor Interativo (Teach, Example, Quiz, Fill) - 100% migrado.
- **Phase 2 & 3:** Expansão de Conteúdo Base e Cobertura - 100% integrado.
- **Phase 4:** Refatoração Didática (Microlearning) - 100% aplicado. (Desmembramento de lições pesadas como 6.8 CSRF/SSRF).
- **Phase 5:** Auditoria Didática e Expansão Crítica - 100% concluída. (Injeção em massa de Microlearning em 18+ lições densas resultando em 69 lições modulares no hub).

---

## 🚀 FASES ATIVAS & FUTURAS (Próximos Passos Relevantes)

### Phase 6: Simulador de Terminal Interativo (JS) 💻
**Goal:** Substituir as lacunas estáticas (fill-in-the-blanks) nos Módulos 3 (OSINT/Recon) e 10 (Arsenal) por um mini-emulador de terminal real no navegador. 
- **Plan 6.1:** Desenvolver motor JS básico para aceitar comandos de texto (ex: `nmap`, `sqlmap`).
- **Plan 6.2:** Mapear *outputs* pré-definidos (mock data) simulando o Kali Linux.
- **Plan 6.3:** Substituir os passos `fill` da UI pelo novo componente de `<terminal-view>`.

### Phase 7: Persistência de Progresso (Gamificação) 🏆
**Goal:** Criar senso de evolução e engajamento salvando o progresso do aluno via `localStorage`.
- **Plan 7.1:** Implementar mecanismo de *trigger* ao vencer uma lição (tela de vitória) que salva o ID da lição no `localStorage`.
- **Plan 7.2:** Atualizar a `index.html` e os menus de módulo para renderizar um *check* visual ou barra de progresso em lições já vencidas.
- **Plan 7.3:** (Opcional) Sistema simples de medalhas/badges ao finalizar 100% de um módulo.

### Phase 8: Simulador de Explorações Gráficas (Playground) 🛡️
**Goal:** Adicionar interatividade visual dinâmica nos ataques Web (Módulo 6).
- **Plan 8.1:** Criar componentes onde o aluno "injeta" um payload `<script>` e a interface simula um pop-up de `alert(1)` pulando na tela.
- **Plan 8.2:** Simular visualmente o roubo de cookies ou injeção SQL no DOM do próprio curso.

### Phase 9: Recombinação Didática (Profundidade > Fragmentação) 🧩
**Goal:** Consolidar lições excessivamente fragmentadas (arquivos `a`, `b`, `c`, `d`) de volta em blocos lógicos coesos. O princípio fundamental do CyberDuo não é "ter arquivos curtos", mas sim **garantir profundidade em cada conceito** (tríade `Teach ➔ Example ➔ Quiz`). É perfeitamente aceitável e desejável ter uma lição com 12 passos hiper-didáticos agrupando ferramentas/teorias complementares, do que espalhar isso em 3 arquivos.
- **Plan 9.1:** Auditar `lesson_definitions.json` e unificar lições que foram desnecessariamente separadas (ex: juntar `10.1a` e `10.1b` de volta, ou juntar vulnerabilidades parecidas) sem perder a tríade pedagógica interna.
- **Plan 9.2:** Ajustar o `lesson_definitions.json` para refletir os arrays agrupados.
- **Plan 9.3:** Atualizar as descrições no roteador `update_modules.py` e deletar os arquivos HTML fragmentados que sobraram na pasta.

### Phase 10: Auditoria de Coerência Teoria-Avaliação (Caça aos Órfãos) 🕵️‍♂️
**Goal:** Garantir que 100% das perguntas, lacunas (`fill`) e associações (`match`) testem EXCLUSIVAMENTE conceitos que foram explicitamente apresentados nos blocos `teach` e `example` anteriores. Nenhum conceito "alienígena" pode ser cobrado.
- **Plan 10.1:** Desenvolver um script Python de NLP ou heurística para varrer o `lesson_definitions.json` e cruzar os `terms` e `correctText` das avaliações com o conteúdo de ensino da respectiva lição.
- **Plan 10.2:** Gerar um relatório de "Conceitos Órfãos" listando onde a quebra de coerência acontece.
- **Plan 10.3:** Corrigir em lotes, módulo por módulo, reescrevendo as perguntas ou adicionando os blocos teóricos faltantes.
