COMPLEXIDADE

Como medir?
Métodos Empíricos - obtemos o tempo de execução através da execução propriamente dita do algoritmo, considerando-se entradas diversas.

Métodos Analíticos - obtemos uma ordem de grandeza do tempo execução através de expressões matemáticas que traduzam o comportamento de um algoritmo.

Método científico aplicado a análise de
algoritmos
Sedgewick:
• Observar uma característica do fenômeno natural
• Inferir um modelo/hipótese consistente com as observações
• Prever eventos usando a hipótese/modelo
• Verificar as predições com mais experimentos
• Repetir o processo até que o modelo seja consistente com a realidade
• Experimentos devem ser reproduzíveis
• Hipótese deve ser falseável
• Fenômeno = desempenho do computador em uma máquina real

A medida de ver independente de fatores:
 - Linguagem de programação 
 - Máquina que será executado

Ou seja a idéia central
tempo de execução = número de passos efetuados pelo algoritmo

A variável usada para calcular é o tamanho da entrada.


As Notações O, Ω e Θ

Definição (notação O)  =  limite superior para o tempo de execução.

Definição (notação Ω)  =  limite inferior para o tempo de execução.

Definição (notação Θ)  =  tempo de execução ótimo.

No geral sempre estamos procurando saber o comportamento do algoritmo no seu pior caso


Classes de comportamento assintótico

• O(1): complexidade constante. Tempo de execução independe do
tamanho da entrada.
• O(log n): complexidade logarítmica. Ocorre em algoritmos que
mapeiam o problema maior em subproblemas
• O(n): complexidade linear. Algoritmos que varrem uma lista de
tamanho n
• O(n log n): ocorre em algoritmos que quebram o problema em
subproblemas, resolve-os independentemente, e depois reuni as
soluções
• O(n^2): complexidade quadrática. Algoritmos com dois laços
aninhados (processa elementos de uma lista aos pares)
• O(n^3): complexidade cúbica. Algoritmos com três laços aninhados
(problemas de algebra linear, mult. matrizes). Úteis apenas para
problemas de tamanho pequeno (dobro da entrada = 8x tempo)
• O(2^n): complexidade exponencial. Algoritmos que processam
subconjuntos de um conjunto com n elementos (normalmente busca
exaustiva)
• O(n!): complexidade fatorial. Algoritmos que processam todas as
permutações de uma sequência de n elementos


https://www.youtube.com/watch?v=X_6LTVkymVM&list=PLGlEDy3kkSSNTESjeBOJZ9NWG46r_FJAO&index=1&t=19s

https://www.youtube.com/watch?v=pwn4y78MZFw&list=PLGlEDy3kkSSNTESjeBOJZ9NWG46r_FJAO&index=2

https://www.youtube.com/watch?v=UQzCFkRbIrE&list=PLGlEDy3kkSSNTESjeBOJZ9NWG46r_FJAO&index=3
