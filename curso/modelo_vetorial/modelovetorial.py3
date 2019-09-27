import numpy as np
import scipy.linalg as la

def similaridade(vetor1, vetor2):
        return float(np.dot(vetor1,vetor2) / (la.norm(vetor1) * la.norm(vetor2)))

#interesses correspondem à: (comédia, ação, drama, horror, romance)

interesses = {"João": (3,4,4,1,4),
		   "Maria": (4,3,5,1,5),
		   "Joaquim": (2,5,1,3,1),
		   "José": (1,1,5,1,1)}

meus_interesses = (1,1,4,1,2)

classificacao = [(nome, similaridade(interesses[nome],meus_interesses)) for nome in interesses.keys()]

classificacao = sorted(classificacao, key = lambda item: item[1], reverse=True)

for i,pontuacao in enumerate(classificacao):
	print(str(i+1) + "º: ",pontuacao)