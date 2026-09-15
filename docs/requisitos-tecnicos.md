# Critérios para implementar o Billing Hub

Esta referência propõe requisitos para a equipe técnica e critérios para o mantenedor aprovar a implementação. Nenhum item abaixo comprova funcionalidade entregue. Responsável pela aprovação: mantenedor do projeto.

## Limites de responsabilidade

O Hub propõe centralizar cobrança e direitos de acesso dos produtos. Cada produto preserva sua operação, autenticação existente e responsabilidades específicas até uma migração aprovada.

- Não acesse bancos de outros SaaS diretamente; defina contratos versionados
- Não copie bases de produção para desenvolver ou validar a fundação
- Não associe automaticamente organizações de produtos diferentes pelo e-mail
- Mantenha credenciais por integração e ambiente, com menor privilégio
- Preserve as responsabilidades de Banana e Paperclip; agentes não recebem poder financeiro por padrão

## Critérios técnicos propostos

| Área | Requisito | Evidência esperada antes de produção |
|---|---|---|
| Isolamento | Vincular organização e produto à identidade autenticada; não confiar apenas no tenant enviado pelo cliente | Testes de leitura e escrita cruzadas retornam negação, inclusive em exportações |
| Autorização | Separar operação, suporte, leitura e administração financeira | Matriz de permissões aprovada e testes negativos por perfil |
| Valores | Usar representação decimal exata ou unidades monetárias mínimas, moeda explícita e arredondamento definido | Testes de desconto, proporcionalidade, estorno parcial e somatórios |
| Idempotência | Usar chave com escopo de organização/operação e restrição única no banco; rejeitar reuso com payload diferente | Requisições repetidas e concorrentes causam um único efeito |
| Eventos recebidos | Autenticar conforme o provedor real; só confirmar recebimento após persistência durável | Falha antes e depois da gravação, duplicação e evento inválido não perdem nem duplicam efeito |
| Ordem dos eventos | Reconciliar transições com o estado autoritativo; não presumir ordem de chegada | Evento antigo não reativa assinatura cancelada nem reverte pagamento indevidamente |
| Eventos enviados | Definir persistência transacional de eventos, retentativas limitadas e fila de falhas | Recuperação após queda entrega evento sem perder alteração financeira |
| Checkout | Não liberar benefício por redirecionamento do navegador; confirmar pelo provedor | Redirecionamento forjado não altera pagamento nem entitlement |
| Conciliação | Comparar cobranças locais e provedor; registrar divergências e resolução | Cenários de timeout com pagamento confirmado e falha de webhook |
| Entitlements | Versionar direitos e política para inadimplência, cancelamento e indisponibilidade | Eventos repetidos não oscilam acesso; comportamento offline tem limite aprovado |
| Logs | Mascarar dados pessoais, tokens e payloads sensíveis; manter correlação sem segredos | Revisão de amostras sintéticas e teste automatizado de mascaramento |
| Rede | Isolar bancos e filas; autenticar serviços; limitar saída e destinos de callbacks | Testes de URLs não autorizadas, acesso externo negado ao banco e limites de payload |
| Recuperação | Definir objetivos de perda de dados e tempo de recuperação; testar restauração | Relatório de restauração em ambiente isolado e conciliação após recuperação |
| UX financeira | Diferenciar pendente, confirmado, falhou e ação necessária; confirmar ações de impacto | Testes de teclado, foco, contraste, erro recuperável e prevenção de envio duplo |

Os mecanismos específicos de Asaas ou outro provedor precisam ser verificados em sua documentação oficial ao implementar. Não substitua autenticação por confiança no corpo da requisição ou endereço de origem.

## Decisões que exigem aprovação

Antes de escolher frameworks ou iniciar integrações, registre:

1. Qual produto será o primeiro consumidor e qual operação entrará no MVP
2. Quem será a parte contratante, recebedora e responsável pela cobrança
3. Como organizações e contas dos produtos serão vinculadas sem misturar dados
4. Qual provedor, ambiente de teste e mecanismo de autenticação serão usados
5. Quais preços, moedas, períodos de carência e regras de cancelamento se aplicam
6. Qual SLA, volume, limite de retentativas e política de continuidade serão adotados
7. Quem poderá aprovar estornos, créditos, migrações e mudanças de planos
8. Quais dados serão necessários, sua retenção e responsabilidades de privacidade

Não foram aprovadas decisões comerciais ou jurídicas nesta auditoria. O escopo de LinkOps precisa ser confirmado, pois o material anterior alterna serviços técnicos e programas públicos.

## Sequência proposta

1. Aprovar escopo do MVP e registrar decisões arquiteturais com responsável e versão
2. Configurar CI, Security Gate e regras de branch
3. Implementar uma jornada em sandbox com dados sintéticos e testes negativos
4. Validar migração e rollback por produto, sem cobrança duplicada
5. Autorizar piloto limitado após evidências técnicas e revisão humana

Ser aprovado para desenvolvimento não significa estar aprovado para produção.
