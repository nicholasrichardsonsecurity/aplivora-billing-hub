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

Prefira mensagens Conventional Commits, como:

~~~text
feat: adiciona catálogo de planos
fix: corrige idempotência de webhook
security: restringe permissão administrativa
~~~
