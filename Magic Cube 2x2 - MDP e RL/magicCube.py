## ALGORITMO MARKOV DECISION PROCESS PARA RESOLUÇÃO DE UM CUBO MÁGICO 2X2

##OBS: SE NÃO RODAR, REDUZIR TESTE.

TESTE = 3;
EMBARALHAR = 5;


import random;
from copy import deepcopy;
import numpy

## sf é o estado final que o cubo precisa se encontrar

sf= (('G1','G2','G3','G4'),
     ('O1','O2','O3','O4'),
     ('Y1','Y2','Y3','Y4'),
     ('W1','W2','W3','W4'),
     ('B1','B2','B3','B4'),
     ('R1','R2','R3','R4'))

sf = list(sf);
for i in range(0,6):
	sf[i] = list(sf[i]);
for i in range(0,6):
	for j in range(0,4):
		sf[i][j] = list(sf[i][j]);


# A TUPLA DE REFERÊNCIA SIGNIFICA QUE OLHANDO A FACE 1 (ref[1-1] = GREEN), A COR DE CIMA
# É A 6 (RED), A DA DIREITA É A 3 (YELLOW), A DE BAIXO É 2 (ORANGE) E DA ESQUERDA
# É 4 (WHITE)
ref = ((6,3,2,4),(1,3,5,4),(1,6,5,2),(1,2,5,6),(2,3,6,4),(5,3,1,4))
GREEN = 1
ORANGE = 2
YELLOW = 3
WHITE = 4
BLUE = 5
RED = 6
TOP = 1
RIGHT = 2
BOTTOM = 3
LEFT = 4

# TUPLA DE TODAS AS AÇÕES POSSÍVEIS, SENDO O #NUMERO, A FACE QUE IRÁ SER ROTACIONADA
# 'R' -> MOVER DIREITA, 'L' -> MOVER ESQUERDA, 'F' -> MOVER A FACE, 'T' -> MOVER
# O TOPO E 'B' -> MOVER EMBAIXO.
# 'CW' -> MOVER NO SENTIDO HORÁRIO E 'CCW' -> MOVER NO SENTIDO ANTIHORÁRIO

ACOES =((1,'R','CW'),(1,'L','CW'),(1,'F','CW'),(1,'T','CW'),(1,'B','CW'),
        (1,'R','CCW'),(1,'L','CCW'),(1,'F','CCW'),(1,'T','CCW'),(1,'B','CCW'),
        (2,'R','CW'),(2,'L','CW'),(2,'F','CW'),(2,'T','CW'),(2,'B','CW'),
        (2,'R','CCW'),(2,'L','CCW'),(2,'F','CCW'),(2,'T','CCW'),(2,'B','CCW'),
        (3,'R','CW'),(3,'L','CW'),(3,'F','CW'),(3,'T','CW'),(3,'B','CW'),
        (3,'R','CCW'),(3,'L','CCW'),(3,'F','CCW'),(3,'T','CCW'),(3,'B','CCW'),
        (4,'R','CW'),(4,'L','CW'),(4,'F','CW'),(4,'T','CW'),(4,'B','CW'),
        (4,'R','CCW'),(4,'L','CCW'),(4,'F','CCW'),(4,'T','CCW'),(4,'B','CCW'),
        (5,'R','CW'),(5,'L','CW'),(5,'F','CW'),(5,'T','CW'),(5,'B','CW'),
        (6,'R','CCW'),(5,'L','CCW'),(5,'F','CCW'),(5,'T','CCW'),(5,'B','CCW'),
        (6,'R','CW'),(6,'L','CW'),(6,'F','CW'),(6,'T','CW'),(6,'B','CW'),
        (6,'R','CCW'),(6,'L','CCW'),(6,'F','CCW'),(6,'T','CCW'),(6,'B','CCW'),
        )

# DADO UM ESTADO E UMA AÇÃO, PARA QUAL NOVO ESTADO EU VOU
def ResultadoDaAcao(estado,acao):

    face,movimento,sentido = acao;

    ##TRATANDO TUPLES DO PYTHON PARA MUDAR VALORES
    estadoInicial = list(estado);
    estadoFinal = list(estado);
    
    for i in range(0,6):
        estadoInicial[i] = list(estadoInicial[i]);
        estadoFinal[i] = list(estadoFinal[i]);
    for i in range(0,6):
        for j in range(0,4):
            estadoInicial[i][j] = list(estadoInicial[i][j]);
            estadoFinal[i][j] = list(estadoFinal[i][j]);

    ## REALIZANDO TROCAS
    if(movimento == 'R'):
        if(face == GREEN or face == ORANGE or face == BLUE or face == RED):
            if(sentido == 'CW'):
                r = TOP # Vai Buscar os Topos
                estadoFinal[YELLOW-1][1-1] = estadoInicial[YELLOW-1][3-1];
                estadoFinal[YELLOW-1][2-1] = estadoInicial[YELLOW-1][1-1];
                estadoFinal[YELLOW-1][3-1] = estadoInicial[YELLOW-1][4-1];
                estadoFinal[YELLOW-1][4-1] = estadoInicial[YELLOW-1][2-1];
            elif(sentido == 'CCW'):
                r = BOTTOM # Vai Buscar os Bottoms
                estadoFinal[YELLOW-1][1-1] = estadoInicial[YELLOW-1][2-1];
                estadoFinal[YELLOW-1][2-1] = estadoInicial[YELLOW-1][4-1];
                estadoFinal[YELLOW-1][3-1] = estadoInicial[YELLOW-1][1-1];
                estadoFinal[YELLOW-1][4-1] = estadoInicial[YELLOW-1][3-1];
                
            i = (ref[face-1][r-1])-1;
            j = face-1;
            
            while((face-1)!=i):
                estadoFinal[i][2-1]=estadoInicial[j][2-1];
                estadoFinal[i][4-1]=estadoInicial[j][4-1];
                j = i;
                i = (ref[i][r-1])-1;
                
            estadoFinal[i][2-1]=estadoInicial[j][2-1];
            estadoFinal[i][4-1]=estadoInicial[j][4-1];
            
        elif(face == YELLOW):
                if(sentido == 'CW'):
                    estadoFinal[YELLOW-1][2-1]=estadoInicial[BLUE-1][4-1];
                    estadoFinal[YELLOW-1][4-1]=estadoInicial[BLUE-1][3-1];
                    
                    estadoFinal[BLUE-1][4-1]=estadoInicial[WHITE-1][3-1];
                    estadoFinal[BLUE-1][3-1]=estadoInicial[WHITE-1][1-1];
                    
                    estadoFinal[WHITE-1][3-1]=estadoInicial[GREEN-1][1-1];
                    estadoFinal[WHITE-1][1-1]=estadoInicial[GREEN-1][2-1];

                    estadoFinal[GREEN-1][1-1]=estadoInicial[YELLOW-1][2-1];
                    estadoFinal[GREEN-1][2-1]=estadoInicial[YELLOW-1][4-1];

                    estadoFinal[RED-1][1-1] = estadoInicial[RED-1][3-1];
                    estadoFinal[RED-1][2-1] = estadoInicial[RED-1][1-1];
                    estadoFinal[RED-1][3-1] = estadoInicial[RED-1][4-1];
                    estadoFinal[RED-1][4-1] = estadoInicial[RED-1][2-1];
	    
                elif(sentido == 'CCW'):
                    estadoFinal[YELLOW-1][2-1]=estadoInicial[GREEN-1][1-1];
                    estadoFinal[YELLOW-1][4-1]=estadoInicial[GREEN-1][2-1];
                    
                    estadoFinal[GREEN-1][1-1]=estadoInicial[WHITE-1][3-1];
                    estadoFinal[GREEN-1][2-1]=estadoInicial[WHITE-1][1-1];

                    estadoFinal[WHITE-1][3-1]=estadoInicial[BLUE-1][4-1];
                    estadoFinal[WHITE-1][1-1]=estadoInicial[BLUE-1][3-1];
                    
                    estadoFinal[BLUE-1][4-1]=estadoInicial[YELLOW-1][2-1];
                    estadoFinal[BLUE-1][3-1]=estadoInicial[YELLOW-1][4-1];
                
                    estadoFinal[RED-1][1-1] = estadoInicial[RED-1][2-1];
                    estadoFinal[RED-1][2-1] = estadoInicial[RED-1][4-1];
                    estadoFinal[RED-1][3-1] = estadoInicial[RED-1][1-1];
                    estadoFinal[RED-1][4-1] = estadoInicial[RED-1][3-1];
	
        elif(face == WHITE):
                if(sentido == 'CW'):
                    estadoFinal[WHITE-1][2-1]=estadoInicial[BLUE-1][1-1];
                    estadoFinal[WHITE-1][4-1]=estadoInicial[BLUE-1][2-1];
                    
                    estadoFinal[BLUE-1][1-1]=estadoInicial[YELLOW-1][3-1];
                    estadoFinal[BLUE-1][2-1]=estadoInicial[YELLOW-1][1-1];
                    
                    estadoFinal[YELLOW-1][3-1]=estadoInicial[GREEN-1][4-1];
                    estadoFinal[YELLOW-1][1-1]=estadoInicial[GREEN-1][3-1];

                    estadoFinal[GREEN-1][4-1]=estadoInicial[WHITE-1][2-1];
                    estadoFinal[GREEN-1][3-1]=estadoInicial[WHITE-1][4-1];

                    estadoFinal[ORANGE-1][1-1] = estadoInicial[ORANGE-1][3-1];
                    estadoFinal[ORANGE-1][2-1] = estadoInicial[ORANGE-1][1-1];
                    estadoFinal[ORANGE-1][3-1] = estadoInicial[ORANGE-1][4-1];
                    estadoFinal[ORANGE-1][4-1] = estadoInicial[ORANGE-1][2-1];

                elif(sentido == 'CCW'):
                    estadoFinal[WHITE-1][2-1]=estadoInicial[GREEN-1][4-1];
                    estadoFinal[WHITE-1][4-1]=estadoInicial[GREEN-1][3-1];

                    estadoFinal[GREEN-1][4-1]=estadoInicial[YELLOW-1][3-1];
                    estadoFinal[GREEN-1][3-1]=estadoInicial[YELLOW-1][1-1];

                    estadoFinal[YELLOW-1][3-1]=estadoInicial[BLUE-1][1-1];
                    estadoFinal[YELLOW-1][1-1]=estadoInicial[BLUE-1][2-1];
                    
                    estadoFinal[BLUE-1][1-1]=estadoInicial[WHITE-1][2-1];
                    estadoFinal[BLUE-1][2-1]=estadoInicial[WHITE-1][4-1];

                    estadoFinal[ORANGE-1][1-1] = estadoInicial[ORANGE-1][2-1];
                    estadoFinal[ORANGE-1][2-1] = estadoInicial[ORANGE-1][4-1];
                    estadoFinal[ORANGE-1][3-1] = estadoInicial[ORANGE-1][1-1];
                    estadoFinal[ORANGE-1][4-1] = estadoInicial[ORANGE-1][3-1];
            
    if(movimento == 'L'):
        if(face == GREEN or face == ORANGE or face == BLUE or face == RED):
            if(sentido == 'CCW'):
                r = TOP 
                estadoFinal[WHITE-1][1-1] = estadoInicial[WHITE-1][2-1];
                estadoFinal[WHITE-1][2-1] = estadoInicial[WHITE-1][4-1];
                estadoFinal[WHITE-1][3-1] = estadoInicial[WHITE-1][1-1];
                estadoFinal[WHITE-1][4-1] = estadoInicial[WHITE-1][3-1];
            elif(sentido == 'CW'):
                r = BOTTOM
                estadoFinal[WHITE-1][1-1] = estadoInicial[WHITE-1][3-1];
                estadoFinal[WHITE-1][2-1] = estadoInicial[WHITE-1][1-1];
                estadoFinal[WHITE-1][3-1] = estadoInicial[WHITE-1][4-1];
                estadoFinal[WHITE-1][4-1] = estadoInicial[WHITE-1][2-1];
                
            i = (ref[face-1][r-1])-1;
            j = face-1;
            
            while((face-1)!=i):
                estadoFinal[i][1-1]=estadoInicial[j][1-1];
                estadoFinal[i][3-1]=estadoInicial[j][3-1];
                j = i;
                i = (ref[i][r-1])-1;
                
            estadoFinal[i][1-1]=estadoInicial[j][1-1];
            estadoFinal[i][3-1]=estadoInicial[j][3-1];
            
        elif(face == YELLOW):
                if(sentido == 'CCW'):
                    estadoFinal[YELLOW-1][1-1]=estadoInicial[BLUE-1][2-1];
                    estadoFinal[YELLOW-1][3-1]=estadoInicial[BLUE-1][1-1];
                    
                    estadoFinal[BLUE-1][2-1]=estadoInicial[WHITE-1][4-1];
                    estadoFinal[BLUE-1][1-1]=estadoInicial[WHITE-1][2-1];
                    
                    estadoFinal[WHITE-1][4-1]=estadoInicial[GREEN-1][3-1];
                    estadoFinal[WHITE-1][2-1]=estadoInicial[GREEN-1][4-1];

                    estadoFinal[GREEN-1][3-1]=estadoInicial[YELLOW-1][1-1];
                    estadoFinal[GREEN-1][4-1]=estadoInicial[YELLOW-1][3-1];

                    estadoFinal[ORANGE-1][1-1] = estadoInicial[ORANGE-1][2-1];
                    estadoFinal[ORANGE-1][2-1] = estadoInicial[ORANGE-1][4-1];
                    estadoFinal[ORANGE-1][3-1] = estadoInicial[ORANGE-1][1-1];
                    estadoFinal[ORANGE-1][4-1] = estadoInicial[ORANGE-1][3-1];

                elif(sentido == 'CW'):
                    estadoFinal[YELLOW-1][1-1]=estadoInicial[GREEN-1][3-1];
                    estadoFinal[YELLOW-1][3-1]=estadoInicial[GREEN-1][4-1];

                    estadoFinal[GREEN-1][3-1]=estadoInicial[WHITE-1][4-1];
                    estadoFinal[GREEN-1][4-1]=estadoInicial[WHITE-1][2-1];

                    estadoFinal[WHITE-1][4-1]=estadoInicial[BLUE-1][2-1];
                    estadoFinal[WHITE-1][2-1]=estadoInicial[BLUE-1][1-1];
                    
                    estadoFinal[BLUE-1][2-1]=estadoInicial[YELLOW-1][1-1];
                    estadoFinal[BLUE-1][1-1]=estadoInicial[YELLOW-1][3-1];

                    estadoFinal[ORANGE-1][1-1] = estadoInicial[ORANGE-1][3-1];
                    estadoFinal[ORANGE-1][2-1] = estadoInicial[ORANGE-1][1-1];
                    estadoFinal[ORANGE-1][3-1] = estadoInicial[ORANGE-1][4-1];
                    estadoFinal[ORANGE-1][4-1] = estadoInicial[ORANGE-1][2-1];
                
        elif(face == WHITE):
                if(sentido == 'CW'):
                    estadoFinal[WHITE-1][1-1]=estadoInicial[GREEN-1][2-1];
                    estadoFinal[WHITE-1][3-1]=estadoInicial[GREEN-1][1-1];

                    estadoFinal[GREEN-1][2-1]=estadoInicial[YELLOW-1][4-1];
                    estadoFinal[GREEN-1][1-1]=estadoInicial[YELLOW-1][2-1];

                    estadoFinal[YELLOW-1][4-1]=estadoInicial[BLUE-1][3-1];
                    estadoFinal[YELLOW-1][2-1]=estadoInicial[BLUE-1][4-1];
                    
                    estadoFinal[BLUE-1][3-1]=estadoInicial[WHITE-1][1-1];
                    estadoFinal[BLUE-1][4-1]=estadoInicial[WHITE-1][3-1];

                    estadoFinal[RED-1][1-1] = estadoInicial[RED-1][3-1];
                    estadoFinal[RED-1][2-1] = estadoInicial[RED-1][1-1];
                    estadoFinal[RED-1][3-1] = estadoInicial[RED-1][4-1];
                    estadoFinal[RED-1][4-1] = estadoInicial[RED-1][2-1];

                elif(sentido == 'CCW'):
                    estadoFinal[WHITE-1][1-1]=estadoInicial[BLUE-1][3-1];
                    estadoFinal[WHITE-1][3-1]=estadoInicial[BLUE-1][4-1];

                    estadoFinal[BLUE-1][3-1]=estadoInicial[YELLOW-1][4-1];
                    estadoFinal[BLUE-1][4-1]=estadoInicial[YELLOW-1][2-1];

                    estadoFinal[YELLOW-1][4-1]=estadoInicial[GREEN-1][2-1];
                    estadoFinal[YELLOW-1][2-1]=estadoInicial[GREEN-1][1-1];

                    estadoFinal[GREEN-1][2-1]=estadoInicial[WHITE-1][1-1];
                    estadoFinal[GREEN-1][1-1]=estadoInicial[WHITE-1][3-1];

                    estadoFinal[RED-1][1-1] = estadoInicial[RED-1][2-1];
                    estadoFinal[RED-1][2-1] = estadoInicial[RED-1][4-1];
                    estadoFinal[RED-1][3-1] = estadoInicial[RED-1][1-1];
                    estadoFinal[RED-1][4-1] = estadoInicial[RED-1][3-1];
            
    elif(movimento == 'F'):
        if(face == GREEN):
            if(sentido == 'CW'):
                estadoFinal[RED-1][3-1] = estadoInicial[WHITE-1][2-1];
                estadoFinal[RED-1][4-1] = estadoInicial[WHITE-1][1-1];
                estadoFinal[WHITE-1][2-1] = estadoInicial[ORANGE-1][2-1];
                estadoFinal[WHITE-1][1-1] = estadoInicial[ORANGE-1][1-1];
                estadoFinal[ORANGE-1][2-1] = estadoInicial[YELLOW-1][2-1];
                estadoFinal[ORANGE-1][1-1] = estadoInicial[YELLOW-1][1-1];
                estadoFinal[YELLOW-1][2-1] = estadoInicial[RED-1][3-1];
                estadoFinal[YELLOW-1][1-1] = estadoInicial[RED-1][4-1];
                
                estadoFinal[GREEN-1][1-1] = estadoInicial[GREEN-1][3-1];
                estadoFinal[GREEN-1][2-1] = estadoInicial[GREEN-1][1-1];
                estadoFinal[GREEN-1][3-1] = estadoInicial[GREEN-1][4-1];
                estadoFinal[GREEN-1][4-1] = estadoInicial[GREEN-1][2-1];
                
            elif(sentido == 'CCW'):
                estadoFinal[GREEN-1][1-1] = estadoInicial[GREEN-1][2-1];
                estadoFinal[GREEN-1][2-1] = estadoInicial[GREEN-1][4-1];
                estadoFinal[GREEN-1][3-1] = estadoInicial[GREEN-1][1-1];
                estadoFinal[GREEN-1][4-1] = estadoInicial[GREEN-1][3-1];

                estadoFinal[RED-1][3-1] = estadoInicial[YELLOW-1][2-1];
                estadoFinal[RED-1][4-1] = estadoInicial[YELLOW-1][1-1];
                estadoFinal[YELLOW-1][2-1] = estadoInicial[ORANGE-1][2-1];
                estadoFinal[YELLOW-1][1-1] = estadoInicial[ORANGE-1][1-1];
                estadoFinal[ORANGE-1][2-1] = estadoInicial[WHITE-1][2-1];
                estadoFinal[ORANGE-1][1-1] = estadoInicial[WHITE-1][1-1];
                estadoFinal[WHITE-1][2-1] = estadoInicial[RED-1][3-1];
                estadoFinal[WHITE-1][1-1] = estadoInicial[RED-1][4-1];
                
        elif(face == ORANGE):
            estadoFinal = ResultadoDaAcao(estadoInicial,(WHITE,'R',sentido));

        elif(face == BLUE):
            if(sentido == 'CW'):
                estadoFinal[BLUE-1][1-1] = estadoInicial[BLUE-1][3-1];
                estadoFinal[BLUE-1][2-1] = estadoInicial[BLUE-1][1-1];
                estadoFinal[BLUE-1][3-1] = estadoInicial[BLUE-1][4-1];
                estadoFinal[BLUE-1][4-1] = estadoInicial[BLUE-1][2-1];

                estadoFinal[ORANGE-1][3-1] = estadoInicial[WHITE-1][3-1];
                estadoFinal[ORANGE-1][4-1] = estadoInicial[WHITE-1][4-1];
                estadoFinal[WHITE-1][3-1] = estadoInicial[RED-1][2-1];
                estadoFinal[WHITE-1][4-1] = estadoInicial[RED-1][1-1];
                estadoFinal[RED-1][2-1] = estadoInicial[YELLOW-1][3-1];
                estadoFinal[RED-1][1-1] = estadoInicial[YELLOW-1][4-1];
                estadoFinal[YELLOW-1][3-1] = estadoInicial[ORANGE-1][3-1];
                estadoFinal[YELLOW-1][4-1] = estadoInicial[ORANGE-1][4-1];
                
            elif(sentido == 'CCW'):
                estadoFinal[BLUE-1][1-1] = estadoInicial[BLUE-1][2-1];
                estadoFinal[BLUE-1][2-1] = estadoInicial[BLUE-1][4-1];
                estadoFinal[BLUE-1][3-1] = estadoInicial[BLUE-1][1-1];
                estadoFinal[BLUE-1][4-1] = estadoInicial[BLUE-1][3-1];

                estadoFinal[RED-1][2-1] = estadoInicial[WHITE-1][3-1];
                estadoFinal[RED-1][1-1] = estadoInicial[WHITE-1][4-1];
                estadoFinal[WHITE-1][3-1] = estadoInicial[ORANGE-1][3-1];
                estadoFinal[WHITE-1][4-1] = estadoInicial[ORANGE-1][4-1];
                estadoFinal[ORANGE-1][3-1] = estadoInicial[YELLOW-1][3-1];
                estadoFinal[ORANGE-1][4-1] = estadoInicial[YELLOW-1][4-1];
                estadoFinal[YELLOW-1][3-1] = estadoInicial[RED-1][2-1];
                estadoFinal[YELLOW-1][4-1] = estadoInicial[RED-1][1-1];
                
        elif(face == RED):
            estadoFinal = ResultadoDaAcao(estadoInicial,(WHITE,'L',sentido));

        elif(face == YELLOW):
            estadoFinal = ResultadoDaAcao(estadoInicial,(GREEN,'R',sentido));

        elif(face == WHITE):
            estadoFinal = ResultadoDaAcao(estadoInicial,(GREEN,'L',sentido));
            
    elif(movimento == 'T'):
        if(face == GREEN):
            estadoFinal = ResultadoDaAcao(estadoInicial,(YELLOW,'R',sentido));

        elif(face == ORANGE):
            estadoFinal = ResultadoDaAcao(estadoInicial,(GREEN,'F',sentido));

        elif(face == BLUE):
            estadoFinal = ResultadoDaAcao(estadoInicial,(ORANGE,'F',sentido));

        elif(face == RED):
            estadoFinal = ResultadoDaAcao(estadoInicial,(BLUE,'F',sentido));

        elif(face == YELLOW):
            estadoFinal = ResultadoDaAcao(estadoInicial,(GREEN,'F',sentido));

        elif(face == WHITE):
            estadoFinal = ResultadoDaAcao(estadoInicial,(GREEN,'F',sentido));

    elif(movimento == 'B'):
        if(face == GREEN):
            estadoFinal = ResultadoDaAcao(estadoInicial,(YELLOW,'L',sentido));

        elif(face == ORANGE):
            estadoFinal = ResultadoDaAcao(estadoInicial,(BLUE,'F',sentido));

        elif(face == BLUE):
            estadoFinal = ResultadoDaAcao(estadoInicial,(RED,'F',sentido));

        elif(face == RED):
            estadoFinal = ResultadoDaAcao(estadoInicial,(GREEN,'F',sentido));

        elif(face == YELLOW):
            estadoFinal = ResultadoDaAcao(estadoInicial,(BLUE,'F',sentido));

        elif(face == WHITE):
            estadoFinal = ResultadoDaAcao(estadoInicial,(BLUE,'F',sentido));

    
    return estadoFinal

# FUNÇÃO PARA IMPRIMIR O ESTADO DO CUBO
def printState(state):
    for i in range(0,6):
        print(state[i][0][0]+state[i][0][1] + " " + state[i][1][0]+state[i][1][1]);
        print(state[i][2][0]+state[i][2][1] + " " + state[i][3][0]+state[i][3][1]+'\n');

    print('---------------');


# FUNÇÃO PARA DEFINIR A RECOMPENSA DO ESTADO

def recompensaQ(state):

        if(state == sf):
                return 100;

        return 1;

def recompensaMDP(state):

        if(state == sf):
                return 1;

        return -0.04;

# FUNÇÃO PARA MONTAR PARTE DOS ESTADOS DISPONÍVEIS PARA DEFINIÇÃO DE S
# OU SEJA, VEJO TODOS OS ESTADOS FORMADOS DE sf EXECUTANDO TODAS AS AÇÕES,
# CADA ESTADO ALCANÇADO EXECUTA TODAS AS AÇÕES, E ASSIM POR DIANTE.

def montarTodosOsEstados():
        S = [];
        S.append(sf);
        j = 0;
        teste = 0;
        while teste < TESTE:
                for i in range(0,len(S)):
                        for a in ACOES:
                                state=ResultadoDaAcao(S[i],a);
                                if(state not in S):
                                        S.append(state);
                teste = teste + 1;
                
        return S  

# FUNÇÃO PARA INICIAR UTILIDADE
def iniciarUtilidade(mdp):
        U = []
             
        for s in mdp[0]:
                U.append((s,0));        

        return U;

# FUNÇÃO PARA RETORNAR O VALOR DE UTILIDADE DADO UM ESTADO s'
def maxAct(U,s):

        for i in range(len(U)):
                if U[i][0] == s:
                        return U[i][1];
                else:
                        return recompensaMDP(s);
                
# FUNÇÃO PARA RETORNAR U, A PARTIR DO VALUE ITERATION
def utilidade(mdp,error):
        
        S,A,gamma = mdp
        
        delta = (error *((1-gamma)/gamma))+1;

        novoU = iniciarUtilidade(mdp);

        novoU = list(novoU)
        for i in range(len(S)):
                novoU[i] = list(novoU[i]);
                

        while delta>(error *((1-gamma)/gamma)):
                U = deepcopy(novoU);
                        
                delta = 0;

                for s in S:
                        for i in range(len(S)):
                                if U[i][0] == s:
                                        novoU[i][1] = recompensaMDP(s) + (gamma)*max(maxAct(U,ResultadoDaAcao(s,a)) for a in ACOES);
                                        delta = max(delta,abs(novoU[i][1]-U[i][1]))

        return U;        
                        
#--------------------------------MAIN MDP--------------------------------

def runMDP():
        mdp = (montarTodosOsEstados(),ACOES,0.9);
        print(len(mdp[0]));

        U = utilidade(mdp,0.00001)

        for k in range(10):
                
                #EMBARALHAR CUBO
                print('\n')
                print(" ----------------- Embaralhar - TENTATIVA:", k, "-----------------")
                print('\n')
                
                ACAO = ACOES[random.randint(0,59)];

                print(ACAO)

                so = ResultadoDaAcao(sf,ACAO);
                for i in range(EMBARALHAR-1):
                        ACAO = ACOES[random.randint(0,59)];
                        so = ResultadoDaAcao(so,ACAO);
                        print(ACAO);
                        
                #printState(so);


                # RESOLVER CUBO
                
                print('\n');
                print("RESOLVER O CUBO")
                ACTION = [];

                maxActions = 0;
                
                while so != sf and maxActions<100:
                        maximo = -1000;
                        i = 0;
                        while i < len(ACOES):

                                local = -1;
                                
                                newState = ResultadoDaAcao(so,ACOES[i]);

                                for j in range(0,len(U)):
                                        if U[j][0] == newState:
                                                local = j;
                                                break

                                if(local != -1):
                                        if U[local][1] > maximo:
                                                ACTION = ACOES[i]
                                                maximo = U[local][1];
                                        elif U[local][1] == maximo:
                                                if random.randint(0,1):
                                                    ACTION = ACOES[i]
                                                    maximo = U[local][1];    

                                i = i + 1;
                                
                        print(maximo);
                        print(ACTION);
                        if(ACTION != []):
                                so = ResultadoDaAcao(so,ACTION);
                        maxActions = maxActions + 1;

                if so != sf:
                        print("NÃO RESOLVEU - ENTROU EM LOOP - POUCOS ESTADOS EXPLORADOS")
                else:
                        print("RESOLVEU");


## ALGORITMO Q-LEARNING RESOLUÇÃO DE UM CUBO MÁGICO 2X2

def estadosRepetidos(s0,scomparar):
        s1=[s0[1],s0[4],[s0[2][3-1],s0[2][1-1],s0[2][4-1],s0[2][2-1]],[s0[3][2-1],s0[3][4-1],s0[3][1-1],s0[3][3-1]],s0[5],s0[0]]
        s2=[s1[1],s1[4],[s1[2][3-1],s1[2][1-1],s1[2][4-1],s1[2][2-1]],[s1[3][2-1],s1[3][4-1],s1[3][1-1],s1[3][3-1]],s1[5],s1[0]]
        s3=[s2[1],s2[4],[s2[2][3-1],s2[2][1-1],s2[2][4-1],s2[2][2-1]],[s2[3][2-1],s2[3][4-1],s2[3][1-1],s2[3][3-1]],s2[5],s2[0]]
        s4=[s3[1],s3[4],[s3[2][3-1],s3[2][1-1],s3[2][4-1],s3[2][2-1]],[s3[3][2-1],s3[3][4-1],s3[3][1-1],s3[3][3-1]],s3[5],s3[0]]
        
        if(scomparar==s1 or scomparar==s2 or scomparar==s3 or scomparar==s4):
                return True;

        return False;

def updateQ(s,a,Q,alpha,gamma,sprime):

        indexAct = ACOES.index(a);
        
        for i in range(len(Q)):
                if(estadosRepetidos(Q[i][0], s)):
                        Q[i][1][indexAct] = Q[i][1][indexAct] + alpha*(recompensaQ(s) + ((gamma)*max(maxActQ(sprime,a,Q) for a in ACOES)) - Q[i][1][indexAct]);
                        break;
        

def maxActQ(sprime,a,Q):
        teste = False;
        
        for i in range(len(Q)):
                if(estadosRepetidos(Q[i][0], sprime)):
                        teste = True;
        if(teste == False ):                
                Q.append((sprime,[0]*len(ACOES)));
        
        if (sprime == sf):
                return recompensaQ(sprime);
        else:
                indexAct = ACOES.index(a);
                for i in range(len(Q)):
                        if(estadosRepetidos(Q[i][0],sprime)):
                                return Q[i][1][indexAct];        


#--------------------------------MAIN Q-LEARNING--------------------------------

def runQLearning():
        #EMBARALHAR CUBO
        k = 0;
        print('\n')
        print(" ----------------- Embaralhar - TENTATIVA:", k, "-----------------")
        print('\n')
               
        ACAO = ACOES[random.randint(0,len(ACOES)-1)];
        alpha = 0.5;
        gamma = 0.8;

        print(ACAO)

        so = ResultadoDaAcao(sf,ACAO);
        for i in range(EMBARALHAR-1):
                ACAO = ACOES[random.randint(0,len(ACOES)-1)];
                so = ResultadoDaAcao(so,ACAO);
                print(ACAO);

        Q = [];
        Q.append((so,[0]*len(ACOES)));

        print('\n');
        print("RESOLVER");

        for i in range(200):
                s = so
                print('i: ',i);
                for j in range(10):
                        a = ACOES[random.randint(0,len(ACOES)-1)];
                        sprime = ResultadoDaAcao(s,a);
                        updateQ(s,a,Q,alpha,gamma,sprime);
                        s = sprime;

        maxChance = 0;
        print('Quantidade de Estados Explorados: ',len(Q));

        
        while (estadosRepetidos(so,sf) == False) and maxChance < 100:
                for i in range(len(Q)):
                        if(estadosRepetidos(Q[i][0],so)):
                                indiceAcao = Q[i][1].index(max(Q[i][1]));
                                break
                print(ACOES[indiceAcao]);
                so = ResultadoDaAcao(so,ACOES[indiceAcao]);

                maxChance = maxChance + 1;

        if (estadosRepetidos(so,sf) == False):
                print("NÃO RESOLVEU - ENTROU EM LOOP - POUCOS ESTADOS EXPLORADOS")
        else:
                print("RESOLVEU");


        
#runMDP();
runQLearning();

