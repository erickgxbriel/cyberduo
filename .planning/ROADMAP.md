# Roadmap

## Phase 1: Migração para Motor Interativo 🚀
**Goal:** Converter as lições existentes do formato quiz-puro para o novo motor interativo (teach, example, quiz, match, fill), migrando o boilerplate e o engine para todos os 50 arquivos de lição.

### Plan 1.1: Preparar Arquivos Base
- Clonar o boilerplate do `0.0-boas-vindas.html` (CSS + JS engine) para todos os outros arquivos de lições.
- Ajustar os caminhos de assets, configurações de cores (variáveis CSS) e link de retorno ao módulo correto.

### Plan 1.2: Migrar Conteúdo Existente (Módulos 1 a 5)
- Converter o array `phases` existente de cada lição para o novo formato `steps`.
- Transformar cada quiz antigo em um fluxo `teach → example → quiz/fill/match`.
- O conteúdo base será extraído dos HTMLs brutos em `/content/`.

### Plan 1.3: Migrar Conteúdo Existente (Módulos 6 a 10)
- Repetir o processo de conversão para os módulos 6 a 10.
- Validar corações, fluxo de vitória e cores por módulo.

---

## ~~Phase 2: Auditoria e Expansão de Conceitos~~ ✅ (merged into Phase 1)

---

## Phase 3: Expansão Profunda de Conteúdo 📖
**Goal:** Aumentar a cobertura de conceitos de 320 steps para ~500+ steps, fechando os ~85 gaps identificados na auditoria e garantindo que TODAS as subseções do material fonte sejam cobertas.

**Auditoria (dados reais):**
- Material fonte: **405 subseções** em 48 arquivos
- Cobertura atual: **320 steps** em 49 lições
- Gap: **~85 conceitos faltantes**

**Módulos mais defasados (prioridade):**
| Módulo | Subseções Fonte | Steps Atuais | Gap |
|--------|----------------|--------------|-----|
| 10.2 Ferramentas/Análise | 54 | 7 | -47 |
| 5.1 Vulns de Rede | 26 | 8 | -18 |
| 3.1 Recon Passivo | 25 | 10 | -15 |
| 10.1 Scripts | 25 | 7 | -18 |
| 5.2 Wireless | 20 | 8 | -12 |
| 3.2 Recon Ativo | 19 | 10 | -9 |
| 7.2 Sistemas Espec. | 17 | 14 | -3 |
| 7.1 Cloud | 13 | 7 | -6 |
| 6.12 Código Inseguro | 13 | 5 | -8 |
| 6.1 OWASP | 12 | 5 | -7 |

### Plan 3.1: Expandir Módulos Críticos (gap > 10)
- **10.2**: Dividir em 10.2a/10.2b/10.2c. Cobrir Metasploit em profundidade, análise de exploits públicos, payloads, pivoting.
- **5.1**: Expandir com LLMNR/NBNS poisoning, relay attacks, VLAN hopping, DNS poisoning, Responder.
- **3.1**: Expandir com DNS zone transfer, email harvesting, metadata analysis, Recon-ng, subfinder.
- **10.1**: Expandir com PowerShell para AD, automação com Python (requests, subprocess), regex para parsing.
- **5.2**: Expandir com WPA Enterprise attacks, PMKID, Karma attacks, rogue AP detection.

### Plan 3.2: Expandir Módulos Médios (gap 5-10)
- **3.2**: Adicionar SMB enumeration, SNMP walking, service fingerprinting.
- **7.1**: Adicionar Lambda exploitation, metadata service SSRF, cloud enumeration tools.
- **6.12**: Adicionar deserialization, race conditions, memory corruption.
- **6.1**: Expandir cada item do OWASP Top 10 com exemplos práticos.
- **8.1/8.2**: Adicionar técnicas de exfiltração, C2 frameworks, Cobalt Strike basics.

### Plan 3.3: Preencher Gaps Menores + Validação
- Expandir todos os módulos com gap < 5.
- Dividir lições com >20 steps em múltiplas lições (a/b/c).
- Atualizar modulo-XX.html para listar novas lições.
- Validar que todas as práticas do curso (ex: 7.2.4, 7.2.16) têm conceitos cobertos.
