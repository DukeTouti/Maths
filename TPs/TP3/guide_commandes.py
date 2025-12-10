import numpy as np
from scipy.optimize import linprog
import math
import matplotlib.pyplot as plt

print ("Création du tableau A de taille 2x2")
A = np.array([[1,2] , [3,4]]) # cree un tableau de taille 2x2 (matrice carré), 1ere ligne 1 2, 2eme ligne 3 4
print (A, "\n")

print ("Retourner l'élément d'indices (0, 0)")
A[0, 0] # accède à l'élément d'indices (0,0), il s'agit de l'élément de la ligne 1 et de la colonne 1, A[0 , 0] = 1
print (A[0, 0], "\n")

print ("Retourner toutes les lignes de la colonne 2")
A[:, 1] # accède à toutes les lignes de la colonne 2, cela retourne [2, 4] ; 2 (1ere ligne de la colonne 2), 4 (2eme ligne de la colonne 2)
print (A[:, 1], "\n")

print ("Retourner toutes les colonnes de la ligne 1")
A[0, :] # accède à toutes les colonnes de la ligne 1, cela retourne [1, 2] ; 1 (1ere colonne de la ligne 1), 2 (2eme colonne de la ligne 1)
print (A[0, :], "\n")

print ("Stocker le nombre de lignes dans nl et le nombre de colonnes dans nc")
nl, nc = A.shape # stocke le nombre de lignes et de colonnes dans nl et nc respectivement
print ("nl :", nl, "\nnc :", nc, "\n")

print ("Création du tableau c de taille 1x3, Retourne son type et sa dimention")
c = np.array ([[4, -2, -2]]) # cree un tableau de taille 1x3, 1 ligne et 3 colonne
print (c) # retourne le tableau c
print ("Type du tableau c :", type(c)) # retourne le type du tableau c
print ("Dimension de c :", c.ndim, "\n") # retourne la dimension du tableau c (ici 2 car on a les lignes et les colonnes)

print ("Retourner le min du tableau c")
m = np.amin(c)
print("Valeur min de c :", m, "\n");

print ("Retourner l'indice du min du tableau c")
print ("Indice du min de c :", np.argmin(c), "\n") # REMARQUE : ici le min se situe à l'indice 1 et 2, le prog retourne 1 donc on en déduit que ça retourne l'indice de la première apparition du min dans le tableau

print ("Retourner le max du tableau c et son indice")
n = np.amax(c)
print ("Valeur max de c est", n, "et se situe à l'indice", np.argmax(c), "\n")

print ("Création de deux tableaux a et v et redimensionnement de ces tableaux avec reshape")
a = np.array([[1.2, 2.5] , [3.2, 1.8] , [1.1, 4.3]]) # cree un tableau de taille 2x3
v = np.arange(0, 10) # cree un tableau de taille 1x10
vp = v.reshape(2, 5) # redimensionnement du tableau en 2x5
print ("a :\n", a, "\n\nv :\n", v, "\n\nRedimentionnement de v de 1x10 à 2x5 :\n", vp)
print ("\na :\n", a.reshape(3, 2), "\n") # affichage du tableau a redimensionné en 3x2 (aucun changement car dimension initiale)

print ("Retourne un tableau de 0 de dimensions 2x4")
print (np.zeros(shape=(2, 4)), "\n") # cree un tableau de dimensions 2x4 remplis de 0 et l'affiche

print ("Cree le tableau b de dimension 1x2 et le concatène avec le tableau a de dimension 3x2 (tableau a juste au dessus)")
b = np.array([[4.1, 2.6]]) # cree le tableau b de dimensions 1x2
d = np.zeros(shape=(3,1)) # creer le tableau d de dimensions 3x1
print ("Tableau a (3x2) :\n", a, "\nTableau b (1x2) :\n", b, "\n")
c = np.append(a, b, axis=0) # concatene le tableau a et b (rajoute b à la fin de a en tant que ligne) (possible car ont le meme nombre de colonnes) et le stocke dans c
print ("Concaténation de a et b ;\n", c, "\n")
print ("Tableau a (3x2) :\n", a, "\nTableau d (3x1) :\n", d, "\n")
e = np.append(a, d, axis=1) # concatene le tableau a et d (rajoute d à la fin de a en tant que colonne) (possible car ont le meme nombre de lignes) et le stocke dans e
print ("Concaténation de a et d ;\n", e, "\n")

print ("Insertion du tableau b dans le tableau a à l'indice 1")
print ("Tableau a (3x2) :\n", a, "\nTableau b (1x2) :\n", b, "\n")
print ("Insertion de b dans a à l'indice 1 (ligne) :\n", np.insert(a, 1, b, axis=0), "\n") # insere le tableau b de dimension 1x2 dans le tableau a de dimension 3x2 en tant que ligne à l'indice 1

print ("Suppression de la ligne d'indice 1 du tableau a")
print ("Tableau a :\n", a, "\nTableau a après suppression de la ligne d'indice 1 :\n", np.delete(a, 1, axis=0), "\n")

print ("Séléctionne toutes les lignes du tableau v comprises entre les indices 0 et 2 (2 exclus)")
v = np.array([[1.2, 2.5] , [3.2, 1.8] , [1.1, 4.3]])
print ("Tableau v :\n", v, "\nLignes 1 et 3 (indice 0 et 2) du tableau v :\n", v[0:2, :], "\n")

print ("Séléctionne la dernière ligne du tableau v")
print ("Tableau v :\n", v, "\nLa dernière ligne du tableau v :\n", v[-1, :], "\n")

print ("Séléctionne les 2 dernières lignes du tableau v")
print ("Tableau v :\n", v, "\nLes 2 dernières lignes du tableau v :\n", v[-2:, :], "\n")

print ("Affiche le maximum de chaque colonne du tableau v")
print ("Tableau v :\n", v, "\nVoici les maximum de chaque colonne de v :\n", np.max(v, axis=0), "\n")









