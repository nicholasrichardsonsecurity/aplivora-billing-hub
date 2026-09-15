# Segurança

O Billing Hub tratará informações de clientes, assinaturas, pagamentos, webhooks e integrações financeiras. Segurança é requisito de produto.

## Não publique em Issues

Não publique vulnerabilidades, tokens, credenciais, payloads reais, dados pessoais ou informações de produção em Issues, Pull Requests ou discussões públicas.

Use um canal privado da Aplivora para comunicar uma vulnerabilidade.

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
- validar assinatura e origem de webhooks;
- não armazenar dados brutos de cartão;
- aplicar menor privilégio;
- revisar migrations destrutivas;
- manter testes de segurança e CI;
- registrar eventos financeiros sensíveis;
- aplicar LGPD e políticas internas.

Testes contra produção somente podem ocorrer com autorização expressa.
