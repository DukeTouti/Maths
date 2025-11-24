/*********************************************
 * OPL 22.1.1.0 Model
 * Author: hathouti
 * Creation Date: 19 nov. 2025 at 22:14:23
 *********************************************/

 
  /***** tspmtz.mod *****/ 
 
 
 /* Paramètres */
int n = ...; /* nombre de villes */

range Villes = 1..n;
range Villes2 = 2..n; /* villes sans la ville de départ (ville 1) */

float d[Villes][Villes] = ...; /* matrice des distances d[i][j] */

/* Variables de décision */
dvar boolean x[Villes][Villes]; /* x[i][j] = 1 si l'arc (i,j) fait partie du tour, 0 sinon */
dvar int u[Villes]; /* u[i] = ordre de visite de la ville i */

/* Fonction objectif : minimiser la distance totale du tour */
minimize
  sum(i in Villes, j in Villes) d[i][j] * x[i][j];

/* Contraintes */
subject to {
  /* (1) Chaque ville doit avoir exactement une sortie */
  forall(i in Villes)
      sum(j in Villes: j != i) x[i][j] == 1;
  
  /* (2) Chaque ville doit avoir exactement une entrée */
  forall(j in Villes)
      sum(i in Villes: i != j) x[i][j] == 1;
  
  /* (3) */
  forall(i in Villes2, j in Villes2: i != j)
      u[i] - u[j] + (n - 1) * x[i][j] <= n - 2;
  
  /* (4) */
  forall(i in Villes)
      u[i] >= 1;
  
  forall(i in Villes)
      u[i] <= n;
}
 
 