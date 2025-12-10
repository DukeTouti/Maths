import numpy as np
from scipy.optimize import linprog
import math
import matplotlib.pyplot as plt

# ============================== FONCTIONS POUR L'ALGORITHME DU SIMPLEXE ==============================

def generate_tabinitial(A, b, c):
	# Construit le tableau initial du simplexe
	# A : matrice des contraintes (m x n)
	# b : vecteur des termes de droite (m x 1)
	# c : vecteur des coefficients de la fonction objectif (1 x n)
	
	m, n = A.shape # m lignes (contraintes), n colonnes (variables)
	
	# Création de la matrice identité pour les variables d'écart
	I = np.eye(m) # matrice identité de taille m x m
	
	# Construction de la matrice augmentée [A | I] qui donne alpha
	A_augmentee = np.append(A, I, axis=1) # concatene A et I horizontalement
	
	# Construction du vecteur c augmenté [c | 0...0]
	zeros = np.zeros(m) # vecteur de m zéros pour les variables d'écart
	c_augmente = np.append(c, zeros) # concatene c et les zeros
	
	# Construction du tableau initial selon la structure du TP
	# Ligne du haut : [alpha | b_barre]
	# Ligne du bas : [c_barre | z]
	
	b = b.reshape(m, 1) # transformation de b en vecteur colonne
	tableau_haut = np.append(A_augmentee, b, axis=1) # ajoute b comme dernière colonne
	
	z = np.array([[0]]) # valeur initiale de z = 0
	c_ligne = np.append(c_augmente, z) # ajoute z à la fin de c
	c_ligne = c_ligne.reshape(1, n + m + 1) # transformation en ligne
	
	tableau = np.append(tableau_haut, c_ligne, axis=0) # concatene verticalement
	
	return tableau


def positivite(v):
	# Vérifie si toutes les composantes du vecteur v sont positives
	# Retourne : (True/False, valeur_min, indice_min)
	
	val_min = np.amin(v) # valeur minimale du vecteur
	indice_min = np.argmin(v) # indice de la valeur minimale
	
	if val_min >= 0:
		return True, val_min, indice_min # toutes les composantes sont positives ou nulles
	else:
		return False, val_min, indice_min # au moins une composante est négative


def rapportmin(b, a):
	# Retourne l'indice du rapport minimum positif b[i]/a[i] avec a[i] > 0
	# Si tous les a[i] <= 0, retourne -1 (problème non borné)
	
	rapports = [] # liste pour stocker les rapports
	indices = [] # liste pour stocker les indices correspondants
	
	for i in range(len(a)):
		if a[i] > 0: # on ne considère que les a[i] strictement positifs pour eviter les divisions par 0 ou par des valeurs negatives
			rapports.append(b[i] / a[i]) # calcul du rapport
			indices.append(i) # sauvegarde de l'indice
	
	if len(rapports) == 0: # aucun a[i] > 0
		return -1 # problème non borné
	
	indice_min = rapports.index(min(rapports)) # indice du rapport minimum dans la liste rapports
	return indices[indice_min] # retourne l'indice correspondant dans le vecteur original


def pivotgauss(T, r, s):
	# Effectue le pivot de Gauss sur le tableau T
	# r : indice de la ligne pivot
	# s : indice de la colonne pivot
	
	pivot = T[r, s] # élément pivot alpha_rs
	T[r, :] = T[r, :] / pivot # divise la ligne pivot par le pivot
	
	# Mise à zéro des autres éléments de la colonne pivot
	for i in range(T.shape[0]): # parcours de toutes les lignes
		if i != r: # sauf la ligne pivot
			facteur = T[i, s] # facteur multiplicatif
			T[i, :] = T[i, :] - facteur * T[r, :] # soustraction de la ligne pivot multipliée par le facteur
	
	return T


def simplexe(A, b, c):
	# Algorithme du simplexe pour minimiser c^T x sous contrainte Ax <= b, x >= 0
	# Retourne : (solution_optimale, valeur_optimale, tableau_final)
	
	print("========== ALGORITHME DU SIMPLEXE ==========\n")
	
	# Génération du tableau initial
	T = generate_tabinitial(A, b, c)
	print("Tableau initial :")
	print(T, "\n")
	
	iteration = 0
	
	while True:
		iteration += 1
		print(f"---------- Itération {iteration} ----------")
		
		# Extraction de la ligne des coûts c_barre (dernière ligne, sans la dernière colonne)
		m, n = T.shape
		c_barre = T[-1, :-1] # tous les éléments de la dernière ligne sauf le dernier (z)
		
		# Test d'optimalité : vérifier si tous les c_barre[j] >= 0
		est_positif, val_min, indice_min = positivite(c_barre)
		
		if est_positif:
			print("Tous les coûts réduits sont >= 0")
			print("Solution optimale trouvée !\n")
			break
		
		# Choix de la colonne pivot selon la règle de Bland : premier indice j tel que c_barre[j] < 0
		s = -1
		for j in range(len(c_barre)):
			if c_barre[j] < 0:
				s = j
				break
		
		print(f"Colonne pivot s = {s} (c_barre[{s}] = {c_barre[s]})")
		
		# Extraction de la colonne pivot (sans la dernière ligne qui contient les coûts)
		colonne_s = T[:-1, s]
		
		# Vérification si le problème est non borné : si tous les alpha_is <= 0
		if np.all(colonne_s <= 0):
			print("Tous les alpha_is <= 0 pour la colonne pivot")
			print("La fonction objectif n'est pas bornée inférieurement !\n")
			return None, -np.inf, T
		
		# Extraction du vecteur b_barre (dernière colonne sans la dernière ligne)
		b_barre = T[:-1, -1]
		
		# Choix de la ligne pivot r selon le rapport minimum
		r = rapportmin(b_barre, colonne_s)
		print(f"Ligne pivot r = {r} (rapport = {b_barre[r] / colonne_s[r]})")
		
		# Pivot de Gauss
		T = pivotgauss(T, r, s)
		print("Tableau après pivot :")
		print(T, "\n")
	
	# Extraction de la solution optimale
	# Les n premières variables sont les variables de décision
	n_vars = A.shape[1] # nombre de variables de décision
	solution = np.zeros(n_vars)
	
	for j in range(n_vars):
		colonne = T[:-1, j]
		# Vérifier si c'est une variable de base (colonne avec un seul 1 et des 0)
		if np.count_nonzero(colonne) == 1 and np.max(colonne) == 1:
			indice_ligne = np.argmax(colonne)
			solution[j] = T[indice_ligne, -1]
	
	valeur_optimale = T[-1, -1] # valeur de z
	
	return solution, valeur_optimale, T


# ============================== EXEMPLE D'UTILISATION ==============================

print("============================== PROBLÈME DE PROGRAMMATION LINÉAIRE ==============================\n")
print("Problème : min z = -6x1 - 4x2")
print("Contraintes :")
print("  -3x1 + 2x2 <=  4")
print("   3x1 + 2x2 <= 16")
print("    x1 + 4x2 <= 22")
print("          x1 <=  3")
print("  x1, x2 >= 0\n")

# Définition du problème
c = np.array([-6, -4]) # fonction objectif à minimiser
A = np.array([[-3, 2], [3, 2], [1, 4], [1, 0]]) # matrice des contraintes
b = np.array([4, 16, 22, 3]) # vecteur des termes de droite

# Résolution avec notre algorithme
solution, valeur_opt, tableau_final = simplexe(A, b, c)

print("============================== RÉSULTATS DE NOTRE ALGORITHME ==============================")
print(f"Solution optimale : x = {solution}")
print(f"Valeur optimale : z = {valeur_opt}\n")

# ============================== COMPARAISON AVEC LINPROG ==============================

print("============================== COMPARAISON AVEC LINPROG (SCIPY) ==============================\n")

res = linprog(c, A_ub=A, b_ub=b)
print(res)
print('Optimal value :', res.fun, '\nX :', res.x)
