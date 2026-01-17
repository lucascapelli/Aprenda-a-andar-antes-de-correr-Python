# Simulados — Entrevista Técnica (descrição fiel)

Repositório com exercícios práticos em Python para treinar operações comuns em entrevistas técnicas. Cada `simuladoN.py` é pequeno e didático — contém código direto e `print()` para visualizar resultados.

Descrição fiel dos arquivos (1–6):

- `simulado1.py` — Contagem
  - Recebe uma lista de números e retorna um dicionário com a frequência de cada número.
  - O código também imprime o estado do dicionário a cada iteração (útil para aprendizado do processo de acumulação).

- `simulado2.py` — Filtro por preço (< 40)
  - Filtra e retorna apenas os livros cujo campo `preco` é menor que 40.

- `simulado3.py` — Filtro por título (>= 10)
  - Retorna livros cujo título tem comprimento maior ou igual a 10 caracteres (usa `len()` no título).

- `simulado4.py` — Exercício extra (observação de discrepância)
  - Enunciado: retornar livros com preço menor que 50 E título com mais de 10 caracteres.
  - Implementação atual: filtra por `preco >= 50` e `len(titulo) >= 10`.
  - Comentários no arquivo explicam que a condição do código difere do enunciado; o arquivo mantém a lógica original para fins didáticos.

- `simulado5.py` — Fundamentos diversos
  - Operações sobre uma lista de números: maior, menor e média.
  - Função que retorna nomes que começam com `'a'` (caso sensível — usa `startswith('a')`).
  - Contagem de frequência de números (retorna dicionário).
  - Filtro de livros por preço (implementação atual filtra por `preco >= 30`, embora o enunciado seja mais genérico).
  - Filtro por tamanho do título (>= 10).

- `simulado6.py` — Funções e list comprehension
  - Calcula quadrados de números com `for` e com list comprehension.
  - Extrai apenas os títulos de uma lista de dicionários.
  - Calcula a média de preços (proteção contra divisão por zero).
  - Retorna livros com preço maior ou igual à média (usa `>=`).
  - Une (concatena) duas listas de dicionários retornando uma nova lista.

Como executar

- Rode: `python simuladoN.py` (onde N é 1..6).
- Recomendado usar Python 3.8+.

Observações

- Os arquivos priorizam aprendizado e clareza nos comentários; nem sempre refletem otimizações ou padrões avançados.
- Este repositório é mantido no meu tempo livre e está em construção — atualizações e correções são adicionadas gradualmente.



