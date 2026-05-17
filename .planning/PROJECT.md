# CyberDuo

## O que é isso?
CyberDuo é uma plataforma de aprendizado de Cibersegurança gamificada, inspirada no Duolingo. O foco é ensinar de forma interativa, prática e neutra, voltada para a preparação para certificações (CompTIA, PenTest+, CEH) e o mercado de trabalho real. 

## Valor Principal (Core Value)
O aprendizado interativo transforma conceitos complexos e massivos de cibersegurança em um fluxo didático engajador: ensinando a teoria, exemplificando a prática e validando a retenção através de exercícios variados, blindando o engajamento através de um design cyberpunk recompensador.

## Contexto
O projeto acabou de migrar do seu formato inicial (que era 100% focado em perguntas de múltipla escolha) para um "Motor Estilo Duolingo", que alterna a experiência entre ensino, exemplo e três tipos de fixação (quiz, preenchimento e associação). Os módulos estão mapeados de 1 a 10, e o material bruto didático existe na pasta `/content/`.

## Requisitos

### Validated
- ✓ Design System Cyberpunk com variáveis CSS de cores por trilha.
- ✓ Interface otimizada mobile-first (`100dvh`, fontes escaláveis, etc).
- ✓ Favicon e identidade visual (Ícone Shield).
- ✓ Motor interativo de lições validado no protótipo `0.0-boas-vindas.html`.

### Active
- [ ] Processar o material da pasta `/content/` para extração de arrays didáticos.
- [ ] Migrar os módulos 01 ao 10 para o novo formato de JSON com 5 tipos de `step`.
- [ ] Clonar e adequar o boilerplate da lição 0.0 para os arquivos finais.

### Out of Scope
- [ ] Criar back-end de autenticação ou progresso real atrelado ao banco de dados no momento (o foco é na UI e motor didático de front-end).

## Evolution
This document evolves at phase transitions and milestone boundaries.
