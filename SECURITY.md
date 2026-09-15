# Segurança

O Billing Hub tratará informações de clientes, assinaturas, pagamentos, webhooks e integrações financeiras. Segurança é requisito de produto.

## Não publique em Issues

Não publique vulnerabilidades, tokens, credenciais, payloads reais, dados pessoais ou informações de produção em Issues, Pull Requests ou discussões públicas.

O canal privado de contato ainda precisa ser definido pelo mantenedor. Se a aba Security oferecer relato privado de vulnerabilidade, use essa opção. Caso ela não esteja disponível, solicite ao mantenedor um canal privado, sem enviar detalhes técnicos em público. Não há prazo de resposta publicado.

## Estado de implementação

A base auditada contém documentação, sem serviço executável ou versão suportada. As regras abaixo são requisitos, não controles implementados ou evidência de conformidade. A configuração de proteção de branches, relato privado e scanners não foi comprovada nesta revisão.

## Escopo prioritário

- autenticação e autorização;
- isolamento entre tenants;
- validação de webhooks;
- idempotência financeira;
- exposição de dados pessoais;
- gestão de segredos;
- SSRF e chamadas externas;
- injeção;
- escalada de privilégio;
- fraude de assinatura ou entitlement;
- logs e auditoria;
- dependências vulneráveis.

## Regras

- nunca commitar segredos;
- usar dados sintéticos fora de produção;
- rotacionar credenciais expostas;
- autenticar webhooks pelo mecanismo documentado pelo provedor; não presumir assinatura criptográfica ou timestamp disponíveis;
- rejeitar eventos não autenticados e persistir chaves de idempotência com restrições de unicidade;
- não armazenar dados brutos de cartão;
- aplicar menor privilégio;
- revisar migrations destrutivas;
- manter testes de segurança e CI;
- registrar eventos financeiros sensíveis;
- aplicar LGPD e políticas internas.

Testes contra produção somente podem ocorrer com autorização expressa.

## Requisitos antes de uma integração

Implemente e teste os [critérios técnicos](./docs/requisitos-tecnicos.md) antes de autorizar dados ou cobranças reais. Inclua casos negativos para isolamento entre organizações, reenvio de eventos e alteração indevida de valores.

Em caso de exposição de credenciais, revogue ou rotacione no serviço emissor. Apagar o texto ou adicionar uma regra ao Git não invalida a credencial nem remove cópias existentes.
