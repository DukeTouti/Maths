import numpy as np

# Affiche le tableau d'allocation de manière formatée
def afficher_tableau_allocation(allocation, couts, offre, demande, titre=""):
	m, n = allocation.shape
	
	print(f"\n{'='*70}")
	print(f"{titre}")
	print(f"{'='*70}\n")
	
	# En-tête
	header = "      "
	for j in range(n):
		header += f"  D{j+1}    "
	header += "  Offre"
	print(header)
	print("-" * len(header))
	
	# Lignes
	for i in range(m):
		row = f"O{i+1}  "
		for j in range(n):
			if allocation[i][j] > 0:
				row += f"  {int(allocation[i][j]):2d}({couts[i][j]:2d}) "
			else:
				row += f"   -({couts[i][j]:2d}) "
		row += f"    {offre[i]}"
		print(row)
	
	# Demandes
	dem_row = "Dem "
	for j in range(n):
		dem_row += f"   {demande[j]:2d}    "
	print("-" * len(header))
	print(dem_row)
	print()

# Calcule le coût total d'une allocation
def calculer_cout_total(allocation, couts):
	m, n = allocation.shape
	cout_total = 0
	for i in range(m):
		for j in range(n):
			cout_total += allocation[i][j] * couts[i][j]
	return cout_total

# Affiche la matrice des coûts
def afficher_matrice_couts(couts):
	m, n = couts.shape
	print("\nMatrice des coûts:")
	print("-" * 40)
	
	# En-tête
	header = "     "
	for j in range(n):
		header += f" D{j+1}  "
	print(header)
	
	# Lignes
	for i in range(m):
		row = f"O{i+1}  "
		for j in range(n):
			row += f" {couts[i][j]:3d} "
		print(row)
	print()




