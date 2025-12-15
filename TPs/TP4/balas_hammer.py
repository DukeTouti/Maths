import numpy as np
import copy

# Calcule le minimum entre l'offre et la demande à l'étape (i, j)
def calculer_minimum(offre, demande, i, j):
	return min(offre[i], demande[j])

# Met à jour les vecteurs offre et demande après chaque allocation
def mettre_a_jour(offre, demande, i, j, allocation):
	offre[i] -= allocation
	demande[j] -= allocation

# Calcule les différences pour chaque ligne et colonne
def calculer_differences(couts, offre, demande):
	m, n = couts.shape
	diff_lignes = []
	diff_colonnes = []
	
	# Différences pour les lignes
	for i in range(m):
		if offre[i] > 0:
			# Trouver les deux plus petits coûts disponibles dans la ligne
			couts_disponibles = []
			for j in range(n):
				if demande[j] > 0:
					couts_disponibles.append(couts[i][j])
			
			if len(couts_disponibles) >= 2:
				couts_disponibles.sort()
				diff = couts_disponibles[1] - couts_disponibles[0]
			elif len(couts_disponibles) == 1:
				diff = 0
			else:
				diff = -1
			diff_lignes.append(diff)
		else:
			diff_lignes.append(-1)
	
	# Différences pour les colonnes
	for j in range(n):
		if demande[j] > 0:
			# Trouver les deux plus petits coûts disponibles dans la colonne
			couts_disponibles = []
			for i in range(m):
				if offre[i] > 0:
					couts_disponibles.append(couts[i][j])
			
			if len(couts_disponibles) >= 2:
				couts_disponibles.sort()
				diff = couts_disponibles[1] - couts_disponibles[0]
			elif len(couts_disponibles) == 1:
				diff = 0
			else:
				diff = -1
			diff_colonnes.append(diff)
		else:
			diff_colonnes.append(-1)
	
	return diff_lignes, diff_colonnes

# Détermine la position optimale pour l'allocation actuelle
def trouver_position_optimale(couts, differences, offre, demande):
	diff_lignes, diff_colonnes = differences
	m, n = couts.shape
	
	# Trouver la différence maximale
	max_diff_ligne = max(diff_lignes) if diff_lignes else -1
	max_diff_colonne = max(diff_colonnes) if diff_colonnes else -1
	max_diff = max(max_diff_ligne, max_diff_colonne)
	
	# Déterminer si c'est une ligne ou une colonne
	if max_diff == max_diff_ligne and max_diff >= 0:
		# C'est une ligne
		i = diff_lignes.index(max_diff)
		# Trouver la cellule avec le coût minimum dans cette ligne
		min_cout = float('inf')
		j_min = -1
		for j in range(n):
			if demande[j] > 0 and couts[i][j] < min_cout:
				min_cout = couts[i][j]
				j_min = j
		return i, j_min
	else:
		# C'est une colonne
		j = diff_colonnes.index(max_diff)
		# Trouver la cellule avec le coût minimum dans cette colonne
		min_cout = float('inf')
		i_min = -1
		for i in range(m):
			if offre[i] > 0 and couts[i][j] < min_cout:
				min_cout = couts[i][j]
				i_min = i
		return i_min, j

# Implémente l'algorithme de Balas-Hammer
def balas_hammer(offre, demande, couts):
	# Copier pour ne pas modifier les originaux
	offre_copy = copy.deepcopy(offre)
	demande_copy = copy.deepcopy(demande)
	
	m = len(offre)
	n = len(demande)
	allocation = np.zeros((m, n))
	
	iteration = 1
	print("\n=== Méthode de Balas-Hammer ===\n")
	
	while sum(offre_copy) > 0 and sum(demande_copy) > 0:
		print(f"Itération {iteration}:")
		
		# Calculer les différences
		differences = calculer_differences(couts, offre_copy, demande_copy)
		diff_lignes, diff_colonnes = differences
		
		print(f"  Différences lignes: {diff_lignes}")
		print(f"  Différences colonnes: {diff_colonnes}")
		
		# Trouver la position optimale
		i, j = trouver_position_optimale(couts, differences, offre_copy, demande_copy)
		
		# Calculer l'allocation
		alloc = calculer_minimum(offre_copy, demande_copy, i, j)
		allocation[i][j] = alloc
		
		print(f"  Cellule choisie: ({i+1}, {j+1}) avec coût {couts[i][j]}")
		print(f"  Allocation: {alloc}\n")
		
		# Mettre à jour
		mettre_a_jour(offre_copy, demande_copy, i, j, alloc)
		
		iteration += 1
	
	return allocation
	
	
	
	

