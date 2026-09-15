# Contribuição

O Aplivora Billing Hub é proprietário. Pull Requests externos não concedem direito de uso do código e somente serão aceitos com autorização da Aplivora.

## Antes de contribuir

- abra uma Issue;
- não inclua dados reais, credenciais ou informações financeiras;
- confirme que o trabalho não viola a licença;
- use uma branch específica;
- mantenha o escopo limitado;
- documente decisões de segurança e compatibilidade.

## Pull Request

Todo Pull Request deve incluir objetivo, impacto, riscos, testes, migrations, mudanças de API, impacto em webhooks, impacto em billing/entitlements e estratégia de rollback.

Nenhuma alteração de produção deve ser feita sem revisão, CI aprovado, Security Gate aprovado e autorização do responsável.

## Verificações nesta fase

Execute a [validação local](./docs/README.md#validação-local) para mudanças documentais. Registre comando, resultado e revisão testada no PR.

Não há aplicação para executar build, typecheck ou testes funcionais. Marque esses itens como não aplicáveis com justificativa, nunca como aprovados. CI (integração contínua) e Security Gate (verificação de segurança) ainda precisam ser configurados; checks ausentes não significam aprovação.

Use Issue, branch e Pull Request também para documentação. Não altere a branch principal diretamente. Não faça merge sem revisão humana e as verificações aplicáveis.

Prefira mensagens Conventional Commits, como:

~~~text
feat: adiciona catálogo de planos
fix: corrige idempotência de webhook
security: restringe permissão administrativa
~~~
