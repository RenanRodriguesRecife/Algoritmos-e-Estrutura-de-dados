# Heaps (Binários)

### 1 Regra

- Heaps de máximo: Pais são maiores que os filhos

- Heaps de mínimo: Pais são menores que os filhos

### 3 regra

- A arvore deve sempre está completa, exceto a ultima linha a direita

## Algoritmo de ordenação do Heap (HEAP SORT)

1 - Primeiro preenche o HEAP conforme o heap é preenchido vai ordenando conforme a primeira regra

2 - Depois que a arvore estiver preenchida começa o processo de remoção dos elementos da árvore e ordenação em um vetor.

3 - O número que está na raiz é enviado a ultima posição do vetor

4 - O número que está na ultima casa é enviado a raíz.

5 - Ordena a raíz seguindo a primeira regra: Repete o processo 3,4 e 5 até preencher o vetor.
