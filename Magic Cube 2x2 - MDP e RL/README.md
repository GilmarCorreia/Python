# Magic Cube 2x2 - MDP e Q-Learning

**Projeto:** Resolução de um cubo mágico 2x2 utilizando Markov Decision Process (MDP) e Q-Learning.

**Descrição:** Trabalho realizado para a disciplina de Inteligência Artificial 

**Autor:** Gilmar Correia Jeronimo – 11014515

## Sobre o projeto:

A ideia de projeto vem em resolver um cubo mágico 2x2 orientado, ou seja, conhecendo a posição de cada uma das faces do cubo. Por exemplo, a face 1 é a face orientada pela "centro virtual" verde, a face 2 pelo "centro" laranja e assim por diante. 
Os estados são representados pelas posições de cada face numa tupla:

<p align="center">
===============================================================
</p>
<p align="center">
==============|G1,G2| || |O1,O2| || |Y1,Y2| || |W1,W2| || |B1,B2| || |R1,R2]==============
</p>
<p align="center">
==============|G3,G4| || |O3,O4| || |Y3,Y4| || |W3,W4| || |B3,B4| || |R3,R4|==============
</p>
<p align="center">
===============================================================
</p>

<p align="center">
<img src="https://user-images.githubusercontent.com/28567780/48970833-6463f380-eff8-11e8-9ce0-42086745fc4b.PNG" height="250">
</p>

Sendo a face verde (G) a primeira posição da tupla, a laranja (O) a segunda posição da tupla, e assim por diante. Modelando o problema de modo que:

A face G é orientada de forma que Y está na direita, O em baixo, W na esquerda e R em cima, e B atrás.

## Função ResultadoDaAção(state,action)

A função ResultadoDaAcao recebe um estado atual, e uma ação executada neste estado, retornando assim o estado alterado pela ação. A modelagem do problema conta com os movimentos:

**'R','CW':** Mover à direita no sentido horário.

**'L','CW:** Mover à esquerda no sentido horário.

**'F','CW:** Mover a face no sentido horário.

**'T','CW:** Mover o topo no sentido horário.

**'B','CW:** Mover a base no sentido horário.

**'R','CCW:** Mover à direita no sentido anti-horário.

**'L','CCW:** Mover à esquerda no sentido anti-horário.

**'F','CCW:** Mover a face no sentido anti-horário.

**'T','CCW:** Mover o topo no sentido anti-horário.

**'B','CCW':** Mover a base no sentido anti-horário.

## Resultado do Markov Decision Process (MDP)

Para emular o MDP foi criado um vetor de estados S com alguns elementos amostrados.

Como S não possui todos os estados, a função de utilidade se aproxima bem para estados próximos da solução, com até dois movimentos finais. Com mais movimentos executados, o algoritmo passa a transitar aleatoriamente entre os estados vizinhos até chegar em um mais próximo da solução.

### _Ex 1:_

	Embaralhar:  (2, 'L', 'CCW'), (3, 'T', 'CCW'), (3, 'R', 'CW'), (6, 'F', 'CCW'), (2, 'L', 'CCW')
	
	Solução: (6, 'L', 'CW'), (4, 'T', 'CW'), (5, 'L', 'CW')

### _Ex 2:_

	Embaralhar:  (6, 'R', 'CCW'), (1, 'B', 'CW'), (6, 'L', 'CCW'),	 (3, 'T', 'CCW'), (3, 'B', 'CCW')
	
	Solução: Não achou solução
	
## Resultado Q-Learning

Com o Q-Learning foi possível chegar em soluções mais factíveis dependendo do estados iniciais do problema e da quantidade de iterações do algoritmo para atualizar a função Q.

### _Ex 1:_

Ao embaralhar o cubo realizando as respectivas ações aleatoriamente:
	
	(3, 'F', 'CCW') -> Rodou a face amarela no sentido anti-horário 
	(3, 'F', 'CW')  -> Rodou a face amarela no sentido horário 
	(5, 'L', 'CW')  -> Rodou a parte esquerda da face azul no sentido horário

<p align="center">
<img src="https://user-images.githubusercontent.com/28567780/48970837-734aa600-eff8-11e8-8fc2-eb435ba4bfa9.PNG" height="250">
</p>

O algoritmo retorna as melhores ações partindo do estado embaralhado: 

	(1, 'L', 'CCW') -> Rodou a parte esquerda da face verde no sentido anti-horário
	
<p align="center">
<img src="https://user-images.githubusercontent.com/28567780/48970842-8493b280-eff8-11e8-8abf-e2722b216478.PNG" height="250">
</p>	
	
Chegando assim no estado final.

### _Ex 2:_
	
	Embaralhando: (5, 'B', 'CCW'), (3, 'R', 'CCW'), (3, 'L', 'CCW'), (5, 'B', 'CW'), (1, 'R', 'CCW')

	Solução: (2, 'R', 'CW'), (3, 'R', 'CW'), (3, 'L', 'CW')

### _Ex 3:_
	
	Embaralhando: (2, 'L', 'CW'), (3, 'T', 'CCW'), (2, 'B', 'CCW'), (4, 'B', 'CCW'), (6, 'B', 'CW')

	Solução: Não achou solução.


