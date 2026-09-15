# Documentação do Billing Hub

Use este índice para revisar a fundação, identificar decisões pendentes e validar os documentos. Público: mantenedor e equipe técnica. Ainda não há API ou painel executável neste repositório.

## Documentos disponíveis

| Documento | Objetivo |
|---|---|
| [Auditoria da fundação](./auditoria-fundacao.md) | Conferir achados, correções e limites |
| [Requisitos técnicos](./requisitos-tecnicos.md) | Revisar critérios propostos antes de implementar |
| [Segurança](../SECURITY.md) | Orientar relatos e tratamento de dados |
| [Contribuição](../CONTRIBUTING.md) | Preparar mudanças para revisão |

OpenAPI, SDKs e guias de instalação serão adicionados quando houver implementação validada. Não existem endpoints utilizáveis para testar aqui.

## Validação local

Requisito: Python 3.10 ou superior. Execute na raiz de uma cópia local deste repositório. Os scripts usam apenas a biblioteca padrão; não instalam dependências nem fazem chamadas de rede.

```bash
python3 scripts/check_docs.py
python3 -m unittest discover -s tests -v
git diff --check
```

O primeiro comando verifica destinos de links locais, âncoras e fechamento de blocos de código nos arquivos Markdown. Os testes exercitam o verificador; não são testes de billing.

O parser cobre links inline e títulos ATX utilizados nestes documentos. Não valida HTML, links por referência, renderização visual, URLs externas, disponibilidade dos badges, conteúdo jurídico ou ausência de segredos.

## Pendências de automação

CI e Security Gate não estão configurados nesta entrega. A integração futura deve executar a verificação documental, testes de aplicação e scanners apropriados. O mantenedor precisa revisar permissões e tornar os checks obrigatórios na branch principal.
