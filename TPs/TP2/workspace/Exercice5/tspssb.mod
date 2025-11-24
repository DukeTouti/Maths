/*********************************************
 * OPL 22.1.1.0 Model
 * Author: hathouti
 * Creation Date: 21 nov. 2025 at 21:07:40
 *********************************************/

 
   /***** tspssb.mod *****/ 
 
 
/***** tspssb.mod *****/

/* Parametres */
int n = ...;
range Villes = 1..n;
range Villes2 = 2..n;
float d[Villes][Villes] = ...;

/* Variables de decision */
dvar boolean x[Villes][Villes];
dvar boolean u[Villes2][Villes2];

/* Fonction objectif */
minimize 
	sum(i in Villes, j in Villes: i != j) d[i][j] * x[i][j];

/* Contraintes */
subject to {
  /* (1) Chaque ville doit avoir exactement une sortie */
  forall(i in Villes)
      sum(j in Villes: j != i) x[i][j] == 1;
  
  /* (2) Chaque ville doit avoir exactement une entree */
  forall(j in Villes)
      sum(i in Villes: i != j) x[i][j] == 1;
  
  /* (3) Si on va directement de i vers j, alors i precede j */
  forall(i in Villes2, j in Villes2: i != j)
      u[i][j] >= x[i][j];
  
  /* (4) Entre deux villes i et j, l'une precede forcement l'autre */
  forall(i in Villes2, j in Villes2: i < j)
      u[i][j] + u[j][i] == 1;
  
  /* (5) Contrainte de transitivite */
  forall(i in Villes2, j in Villes2, k in Villes2: i != j && j != k && i != k)
      u[i][j] + u[j][k] + u[k][i] <= 2;
}






