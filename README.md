# Aplivora Billing Hub

> Camada financeira e operacional compartilhada para os produtos digitais do ecossistema Aplivora.

[![Status: fundação](https://img.shields.io/badge/status-funda%C3%A7%C3%A3o%20e%20arquitetura-2563eb?style=for-the-badge)](https://github.com/nicholasrichardsonsecurity/aplivora-billing-hub)
[![Licença proprietária](https://img.shields.io/badge/licen%C3%A7a-propriet%C3%A1ria-b91c1c?style=for-the-badge)](./LICENSE)
[![Documentação](https://img.shields.io/badge/docs-OpenAPI%20planejada-16a34a?style=for-the-badge)](./docs)
[![Segurança](https://img.shields.io/badge/security-LGPD%20%7C%20audit%C3%A1vel-0f766e?style=for-the-badge)](./SECURITY.md)

[![TypeScript](https://img.shields.io/badge/TypeScript-planejado-3178C6?logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Node.js](https://img.shields.io/badge/Node.js-planejado-339933?logo=node.js&logoColor=white)](https://nodejs.org/)
[![Next.js](https://img.shields.io/badge/Next.js-painel%20planejado-000000?logo=next.js&logoColor=white)](https://nextjs.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-planejado-4169E1?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-planejado-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![OpenAPI](https://img.shields.io/badge/OpenAPI-contratos%20planejados-6BA539?logo=openapiinitiative&logoColor=white)](https://www.openapis.org/)

---

## Visão geral

O **Aplivora Billing Hub** será o núcleo compartilhado de cobrança, assinaturas, pagamentos, planos, limites e direitos de acesso (entitlements) dos produtos Aplivora.

A proposta é concentrar regras financeiras e integrações sensíveis em uma camada governada, com contratos claros para os aplicativos consumidores, rastreabilidade de eventos e segurança desde o desenho.

> **Importante:** este repositório está em fase de fundação. Os itens descritos como “planejados” representam a direção arquitetural e não significam que uma API ou integração já esteja em produção.

## Ecossistema Aplivora

O Hub será preparado para atender diferentes produtos e superfícies operacionais:

[![Aplivora](https://img.shields.io/badge/Aplivora-ecossistema-0f172a?style=flat-square)](https://aplivora.com.br)
[![LinkOps Hub](https://img.shields.io/badge/LinkOps%20Hub-GovTech%20%7C%20opera%C3%A7%C3%B5es-2563eb?style=flat-square)](https://linkops.aplivora.com.br)
[![Quero Internet](https://img.shields.io/badge/Quero%20Internet-conectividade-06b6d4?style=flat-square)](https://querointernet.aplivora.com.br)
[![LoopClub](https://img.shields.io/badge/LoopClub-produto%20digital-16a34a?style=flat-square)](https://loopclub.aplivora.com.br)
[![Paperclip](https://img.shields.io/badge/Paperclip-coordena%C3%A7%C3%A3o%20de%20agentes-7c3aed?style=flat-square)](https://agentes.aplivora.com.br)
[![Banana](https://img.shields.io/badge/Banana-opera%C3%A7%C3%A3o%20t%C3%A9cnica-f59e0b?style=flat-square)](#sistemas-e-integrações)

### Sistemas e integrações previstas

- **Aplivora:** ecossistema institucional e governança de produtos.
- **LinkOps Hub:** programas, operações, parceiros e jornadas de atendimento.
- **Quero Internet:** oferta e operação de conectividade.
- **LoopClub:** produto digital e experiências de assinatura.
- **Banana:** sistema operacional/técnico da operação, quando aplicável.
- **Paperclip:** coordenação e gestão de agentes; não substitui o Billing Hub.
- **Asaas:** provedor de pagamentos e serviços financeiros, sujeito à validação do contrato e da integração.
- **Bancos, mensageria e outros provedores:** somente mediante decisão arquitetural, requisitos de segurança e implementação aprovada.

## Responsabilidades do Billing Hub

### Catálogo e planos

- produtos, ofertas e planos;
- preços, ciclos e períodos de teste;
- versões e vigência de planos;
- limites, benefícios e regras comerciais;
- moeda, impostos e condições aplicáveis.

### Clientes e organizações

- clientes individuais e organizações;
- tenants e vínculo com produtos;
- contatos e preferências de comunicação;
- status cadastral e consentimentos necessários;
- segregação por organização e ambiente.

### Cobrança e pagamentos

- assinaturas e ciclos de cobrança;
- faturas, cobranças e estados financeiros;
- pagamentos, falhas, estornos e créditos;
- cancelamentos, upgrades e downgrades;
- reconciliação e fechamento operacional.

### Entitlements

- direitos de acesso por plano;
- limites de uso e funcionalidades;
- ativação, suspensão e revogação;
- consulta segura pelos aplicativos consumidores;
- histórico de alterações.

### Eventos e integrações

- webhooks assinados e idempotentes;
- eventos de domínio versionados;
- retentativas e fila de processamento;
- correlação entre cobrança, cliente e produto;
- trilha de auditoria para operações sensíveis.

## Arquitetura de referência

~~~mermaid
flowchart LR
    A[Produtos Aplivora] --> B[Billing Hub API]
    B --> C[(PostgreSQL)]
    B --> D[Provedores de pagamento]
    B --> E[Webhooks e eventos]
    E --> A
    B --> F[Painel administrativo]
~~~

A arquitetura final será definida junto com os requisitos de volume, disponibilidade, compliance, custos, operação e integrações reais.

## Stack planejada

| Camada | Tecnologia | Finalidade |
|---|---|---|
| API | Node.js + TypeScript | Serviços, regras e contratos |
| Painel | Next.js + TypeScript | Operação administrativa |
| Persistência | PostgreSQL | Dados transacionais e auditoria |
| Contratos | OpenAPI | Documentação e integração |
| Infraestrutura | Docker | Ambientes reproduzíveis |
| Observabilidade | Logs estruturados e métricas | Diagnóstico e operação |
| Integrações | Webhooks assinados | Eventos externos e internos |

A stack acima é uma direção inicial. Dependências e escolhas definitivas devem ser registradas em ADRs ou documentação técnica antes da implementação.

## Princípios de projeto

1. **Uma única fonte para regras financeiras:** os produtos não devem duplicar regras de cobrança.
2. **Segurança por padrão:** segredos fora do Git, menor privilégio e validação de entradas.
3. **Idempotência:** repetir um evento não pode duplicar cobrança, crédito ou entitlement.
4. **Auditabilidade:** toda decisão financeira relevante deve ter histórico e correlação.
5. **Contratos versionados:** alterações de API e eventos devem ser compatíveis ou migradas.
6. **Privacidade:** minimizar dados, proteger acesso e respeitar a LGPD.
7. **Separação de responsabilidades:** billing, operação, suporte e administração devem ter perfis distintos.
8. **Operação reversível:** mudanças sensíveis devem ter plano de rollback e reconciliação.

## Estrutura esperada

~~~text
.
├── apps/
│   ├── api/                 # API do Billing Hub
│   └── admin/               # Painel administrativo
├── packages/
│   ├── contracts/           # Tipos, schemas e contratos
│   ├── sdk/                 # Cliente interno versionado
│   └── config/              # Configurações compartilhadas
├── docs/
│   ├── architecture/       # ADRs e decisões técnicas
│   ├── api/                # OpenAPI e guias de integração
│   └── operations/         # Runbooks e reconciliação
├── infra/                   # Docker, ambientes e deploy
└── .github/                 # CI, security gates e templates
~~~

A estrutura acima será criada ou ajustada conforme a implementação evoluir.

## Ambientes e URLs planejadas

| Ambiente | Endereço | Situação |
|---|---|---|
| API principal | https://api.aplivora.com.br | Planejado |
| Documentação | https://api.aplivora.com.br/docs | Planejado |
| Painel | endereço separado por ambiente | A definir |
| Sandbox | endereço separado por ambiente | A definir |

Esses endereços não significam que os serviços estejam publicados ou disponíveis.

## Segurança, privacidade e compliance

Este projeto poderá tratar dados cadastrais, comerciais e financeiros. Portanto:

- nunca commitar tokens, senhas, chaves ou certificados;
- não armazenar dados brutos de cartão;
- validar assinatura, timestamp e idempotência de webhooks;
- aplicar controle de acesso por organização, ambiente e função;
- redigir dados sensíveis em logs;
- manter trilhas de auditoria protegidas;
- documentar retenção, finalidade e descarte de dados;
- revisar integrações sob a ótica da LGPD;
- executar testes de segurança somente com autorização.

Leia [SECURITY.md](./SECURITY.md) antes de reportar ou testar vulnerabilidades.

## Desenvolvimento

O projeto ainda está sendo estruturado. Quando a primeira aplicação estiver disponível, esta seção deverá conter os comandos oficiais de instalação, desenvolvimento, testes, migrações e deploy.

Exemplo de fluxo esperado:

~~~bash
npm install
npm run dev
npm run lint
npm run typecheck
npm test
~~~

Não execute comandos acima esperando que funcionem antes da implementação dos respectivos aplicativos e scripts.

## Governança do repositório

Alterações devem seguir o fluxo:

1. abrir ou identificar uma Issue;
2. criar uma branch específica;
3. implementar a mudança com escopo controlado;
4. atualizar documentação e contratos afetados;
5. executar validações locais;
6. abrir Pull Request;
7. aguardar revisão, CI e Security Gate;
8. fazer merge somente com aprovação autorizada.

Consulte [CONTRIBUTING.md](./CONTRIBUTING.md).

## Licenciamento

Este projeto é **proprietário**. O fato de o repositório estar público temporariamente não concede autorização para copiar, modificar, redistribuir, sublicenciar, vender, hospedar ou incorporar o código em outro produto.

- [LICENSE — software](./LICENSE)
- [LICENSE-DOCUMENTATION.md — documentação](./LICENSE-DOCUMENTATION.md)
- [NOTICE.md — avisos e marcas](./NOTICE.md)
- [THIRD-PARTY-NOTICES.md — dependências de terceiros](./THIRD-PARTY-NOTICES.md)

> Para uso comercial, licenciamento de clientes ou distribuição de SDKs, deve ser criada uma licença comercial específica e revisada juridicamente.

## Contato e propriedade

**Aplivora / Nicholas Richardson**  
Repositório: [aplivora-billing-hub](https://github.com/nicholasrichardsonsecurity/aplivora-billing-hub)

Questões de segurança devem seguir o procedimento descrito em [SECURITY.md](./SECURITY.md). Não publique vulnerabilidades ou credenciais em Issues.

---

Copyright © 2026 Aplivora / Nicholas Richardson. Todos os direitos reservados.
