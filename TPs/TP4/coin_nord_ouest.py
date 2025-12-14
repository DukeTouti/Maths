import numpy as np
import copy

# Calcule le minimum entre l'offre et la demande à l'étape (i, j)
def calculer_minimum(offre, demande, i, j):
	return min(offre[i], demande[j])

# Met à jour les vecteurs offre et demande après chaque allocation
def mettre_a_jour(offre, demande, i, j, allocation):
	offre[i] -= allocation
	demande[j] -= allocation

# Implémente l'algorithme du Coin Nord-Ouest
def coin_nord_ouest(offre, demande):

	# Travailler sur des copies pour ne pas modifier les originaux
	offre_copy = copy.deepcopy(offre)
	demande_copy = copy.deepcopy(demande)
	
	m = len(offre)
	n = len(demande)
	allocation = np.zeros((m, n))
	
	i = 0
	j = 0
	
	print("\n=== Méthode du Coin Nord-Ouest ===\n")
	
	while i < m and j < n:
		# Calculer l'allocation
		alloc = calculer_minimum(offre_copy, demande_copy, i, j)
		allocation[i][j] = alloc
		
		print(f"Cellule ({i+1}, {j+1}): allocation = {alloc}")
		
		# Mettre à jour offre et demande
		mettre_a_jour(offre_copy, demande_copy, i, j, alloc)
		
		# Avancer selon l'algorithme
		if offre_copy[i] == 0:
			i += 1
		elif demande_copy[j] == 0:
			j += 1
	
	return allocation
	
	
	
