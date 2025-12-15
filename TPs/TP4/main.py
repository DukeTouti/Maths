import numpy as np
from coin_nord_ouest import coin_nord_ouest
from balas_hammer import balas_hammer
from utils import afficher_tableau_allocation, calculer_cout_total, afficher_matrice_couts

# Résolution de l'Exercice 1 avec la méthode du Coin Nord-Ouest
def exercice_1():
	print("\n" + "="*70)
	print("EXERCICE 1: MÉTHODE DU COIN NORD-OUEST")
	print("="*70)
	
	# Données du problème
	couts = np.array([
		[7,  12, 1,  5,  9],
		[15, 3,  12, 6,  14],
		[8,  16, 10, 12, 7],
		[18, 8,  17, 11, 16]
	])
	
	offre = [12, 11, 14, 8]
	demande = [10, 11, 15, 5, 4]
	
	print(f"\nOffres:   {offre}")
	print(f"Demandes: {demande}")
	
	afficher_matrice_couts(couts)
	
	# Appliquer la méthode du Coin Nord-Ouest
	allocation = coin_nord_ouest(offre, demande)
	
	# Calculer le coût total
	cout_total = calculer_cout_total(allocation, couts)
	
	# Afficher les résultats
	afficher_tableau_allocation(allocation, couts, offre, demande, 
								"SOLUTION PAR COIN NORD-OUEST")
	
	print(f"{'='*70}")
	print(f"COÛT TOTAL: {cout_total}")
	print(f"{'='*70}\n")
	
	return allocation, cout_total

# Résolution de l'Exercice 2 avec la méthode de Balas-Hammer
def exercice_2():
	print("\n" + "="*70)
	print("EXERCICE 2: MÉTHODE DE BALAS-HAMMER")
	print("="*70)
	
	# Données du problème
	couts = np.array([
		[3, 6, 4, 8],
		[3, 4, 7, 9],
		[9, 4, 5, 6]
	])
	
	offre = [20, 17, 13]
	demande = [12, 10, 15, 13]
	
	print(f"\nOffres:   {offre}")
	print(f"Demandes: {demande}")
	
	afficher_matrice_couts(couts)
	
	# Appliquer la méthode de Balas-Hammer
	allocation = balas_hammer(offre, demande, couts)
	
	# Calculer le coût total
	cout_total = calculer_cout_total(allocation, couts)
	
	# Afficher les résultats
	afficher_tableau_allocation(allocation, couts, offre, demande,
								"SOLUTION PAR BALAS-HAMMER")
	
	print(f"{'='*70}")
	print(f"COÛT TOTAL: {cout_total}")
	print(f"{'='*70}\n")
	
	return allocation, cout_total

# Fonction principale
def main():

	# Résoudre les deux exercices
	alloc1, cout1 = exercice_1()
	alloc2, cout2 = exercice_2()
	
	# Résumé final
	print("\n" + "="*70)
	print("RÉSUMÉ DES RÉSULTATS")
	print("="*70)
	print(f"\nExercice 1 (Coin Nord-Ouest): Coût total = {cout1}")
	print(f"Exercice 2 (Balas-Hammer):    Coût total = {cout2}")
	print("\n" + "="*70 + "\n")

if __name__ == "__main__":
	main()






