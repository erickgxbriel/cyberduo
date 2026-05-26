# 🛡️ CyberDuo — Hub de Treinamento Gamificado

> **Segurança Ofensiva e Hacking Ético de forma prática, visual e interativa.**

O **CyberDuo** é uma plataforma de aprendizado gamificada desenvolvida para capacitar estudantes e profissionais na área de Segurança da Informação. Através de lições modulares interativas, desafios baseados em cenários reais e um sistema imersivo de conquistas, você aprende conceitos de Red Team, Web Hacking, Infraestrutura e Defesa Cibernética.

---

## 🚀 Demonstração do Projeto

*   **URL Oficial de Produção:** [https://erickgxbriel.github.io/cyberduo/](https://erickgxbriel.github.io/cyberduo/) _(Atualize para o link da sua nova Organização caso seja diferente!)_
*   **Aparência Moderna:** Interface inspirada em conceitos de ficção científica (cyberpunk/glassmorphism), totalmente responsiva para desktop e dispositivos móveis.

---

## 🎮 Mecânicas de Gamificação

O aprendizado é estimulado por mecânicas clássicas de jogos de RPG e hacking:

*   **Perfil do Agente:** Uma barra dinâmica de perfil que calcula o progresso geral das lições e atualiza o seu nível operativo:
    *   `RECRUTA` 🔰 (Início)
    *   `NOVATO DA REDE` 🖥️ (Progresso > 0%)
    *   `AGENTE ATIVO` ⚔️ (Progresso >= 25%)
    *   `OPERATIVO RED TEAM` 🛡️ (Progresso >= 50%)
    *   `ESPECIALISTA EM SEGURANÇA` 🕶️ (Progresso >= 75%)
    *   `PENTESTER ELITE` 👑 (Progresso 100%)
*   **Medalhas Operacionais:** Conquistas exclusivas que são desbloqueadas automaticamente na sua carteira de conquistas quando você completa 100% de cada módulo.
*   **Barras de Progresso por Módulo:** Acompanhamento visual de progresso individual para cada área de estudo.
*   **Sistema de Vida (5 Corações):** Lições e laboratórios integrados que utilizam um sistema de corações para gamificar perguntas e cenários práticos.

---

## 📚 Estrutura de Módulos (Trilha de Aprendizado)

O curso é dividido em 11 módulos pedagógicos progressivos, totalizando **62 lições**:

*   **Módulo 0 — Introdução ao Curso:** Fundamentos, boas-vindas e configuração do ambiente.
*   **Módulo 1 — Hacking Ético e Pentest:** Metodologias, ética, termos de mercado e laboratório próprio.
*   **Módulo 2 — Planejamento e Escopo:** Governança, GRC, definição de escopo e limites legais.
*   **Módulo 3 — Coleta e Varredura:** OSINT ativa/passiva, DNS, Recon-ng, Shodan e escaneamento de vulnerabilidades.
*   **Módulo 4 — Engenharia Social:** Pretexting, ataques físicos, influência e técnicas de manipulação humana.
*   **Módulo 5 — Exploração de Redes:** Fundamentos de rede, ataques Man-in-the-Middle (MitM), interceptação de tráfego e redes sem fio.
*   **Módulo 6 — Aplicações Web (OWASP Top 10):** Injeções (SQLi, Command Injection), XSS, CSRF/SSRF, falhas de autorização e autenticação.
*   **Módulo 7 — Nuvem, Móvel e IoT:** Vetores de ataque em Cloud (AWS, Azure), vulnerabilidades mobile e segurança em IoT.
*   **Módulo 8 — Pós-Exploração:** Redirecionamento de tráfego, persistência avançada, movimento lateral e bypass de segurança (Evasion).
*   **Módulo 9 — Relatórios e Comunicação:** Elaboração técnica de relatórios de pentest, escalonamento e comunicação pós-entrega.
*   **Módulo 10 — Ferramentas e Código:** Automatização de scripts em Python, análise de código e engenharia reversa básica.
*   **Módulo Especial — THE BLACK BOX:** Um arsenal interativo hacker com acesso livre para os estudantes.

---

## 🛠️ Tecnologias e Arquitetura

O projeto foi construído seguindo preceitos modernos de desenvolvimento estático rápido e robusto:

*   **HTML5 Semântico:** Estruturação limpa de páginas com acessibilidade otimizada.
*   **Tailwind CSS & CSS Vanilla:** Design personalizado de ficção científica com efeitos de brilho, micro-animações, layouts em Grid/Flexbox e total adaptabilidade mobile (Mobile-First).
*   **Vanilla JavaScript (ES6+):** Lógica limpa para persistência de progresso e desbloqueio de conquistas no cache local (`localStorage`), eliminando a necessidade de banco de dados complexo e garantindo privacidade dos dados do usuário.

---

## 💻 Como Executar Localmente

Como o projeto é estático, você não precisa compilar nada!

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/erickgxbriel/cyberduo.git
    cd cyberduo
    ```
2.  **Abra o arquivo principal:**
    *   Basta dar um duplo clique no arquivo `index.html` ou usar a extensão **Live Server** no VS Code para abrir no navegador local.

---

## 📦 Como Publicar no GitHub Pages

Para publicar e atualizar a sua versão online do projeto no GitHub Pages:

1.  No seu repositório no GitHub, vá em **Settings** ➡️ **Pages**.
2.  Em **Build and deployment**, selecione **Deploy from a branch**.
3.  Escolha o branch **`main`** e a pasta **`/(root)`** e clique em **Save**.
4.  O GitHub criará um fluxo automático que publicará seu site em instantes.

---

## 📄 Licença

Este projeto está sob a licença **MIT** — consulte o arquivo [LICENSE](file:///home/gabriel/Documentos/dev/cyberduo/LICENSE) para mais detalhes.

---

<p align="center">Desenhado e desenvolvido com ⚔️ por Gabriel.</p>
