# PT_BR_Wordle_Solver
Este é um solver feito em Python do jogo Wordle, que recebeu sua versão PT-BR recentemente.

# Onde jogar
Os sites para se jogar mais famosos até agora são:

- https://term.ooo/

- https://www.gabtoschi.com/letreco/

# Arquivos
- Um arquivo .csv, que contém uma lista de aproximadamente 6 mil palavras da lingua portuguesa que contém cinco letras. As palavras não contém acento, nem letras maiúsculas, e apenas 5 caracteres por célula.
- Um arqivo .py, que é o próprio solver.

# Funcionamento

### Parte 1:

A partir da primeira tentativa do usuário, teremos no resultado o que chamei de "acertos": acerto verdes, amarelos e vermelhos.
De início, o usuário terá que indicar o número de cada acerto. Veja que a somatória do número de acertos é sempre 5.
Em seguida, será requisitado quais letras correspondem a cada acerto, e as posições dos acertos verdes e amarelos, variando de 0 à 4. Isto é, a primeira posição equivale a 0, a segunda a 1, e assim por diante.

Com essas informações em mãos, já é possível filtrar a base de dados, a partir dos seguintes filtros encadeados
- Filtro verde:
  - Procura todas as palavras na base de dados que tem a letra informada no local informado

- Filtro amarelo:
  - Do conjunto de palavras resultante do filtro verde, procura todas as palavras que contém a letra informada, e que não estão no local informado.

- Filtro vermelho:
  - Do conjunto de palavras resultante do filtro amarelo, procura todas as palavras que não contém a letra informdada.

Finalmente, obtendo uma lista de todas as palavras da base de dados que atendem às restrições anteriores.

### Parte 2:

Como o objetivo do jogo é acertar todas as letras da palavra, e não necessariamente acertar a palavra toda diretamente, podemos usar a frequência das letras nas palavras da lingua portuguesa a nosso favor.

Veja que podemos atribuir à cada letra uma "frequência", explicitada no site https://pt.wikipedia.org/wiki/Frequ%C3%AAncia_de_letras.

Como pode ser visto, a letra "a" tem a maior frequência de aparição na língua portuguesa, por volta de 14%. Isto nos dis que, ao pegar uma palavra aleatória da língua portuguesa, há aproximadamente 14% de chance de ser uma palavra com a letra "a".

Assim, naturalmente, palavras que contém letras que são mais frequentes na língua portuguesa tem mais chances de acertar alguma letra da palavra secreta do jogo.

Finalmente, é atribuído para cada letra do alfabeto um escalar correspondente a sua frequência, e para cada palavra no conjunto resultante dos filtros, soma-se esses valores de cada letra de uma palavra, e atribúi-se o valor da soma à palavra.

Desta forma, palaras com um valor maior tem mais chance de conter alguma letra que está na palavra secreta do jogo.

Por fim, todas as palavras do conjunto são mostradas, assim como o valor da soma associada, e começa-se a próxima iteração.

# Observações:
- Coloque o arquivo .csv e o Script na mesma pasta em seu computador para que o solver funcione.
- A base de dados ainda é pequena. Não funciona em 100% dos casos, mas é bem satisfatória.
- A rotina está bem infantil. Utilizei a oportunidade para REVISAR Python, então há muito espaço para aprimoramento, mesmo com poucas linhas de código.


