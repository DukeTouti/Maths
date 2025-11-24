/*********************************************
 * OPL 22.1.1.0 Model
 * Author: hathouti
 * Creation Date: 19 nov. 2025 at 19:35:45
 *********************************************/



 /***** diet.mod *****/
 
 /* Paramètres */
int m = ...; /* nombre d'éléments nutritifs */
int n = ...; /* nombre d'aliments */

range Nutritifs = 1..m;
range Aliments = 1..n;

float c[Aliments] = ...; /* prix unitaire des aliments */
float q[Nutritifs][Aliments] = ...; /* quantité de nutriment i dans aliment j */
float d[Nutritifs] = ...; /* quantité minimale requise de nutriment i */

/* Variables de décision */
dvar float x[Aliments]; /* quantité d'aliment j à acheter */

/* Fonction objectif : minimiser le coût total */
minimize 
	sum(j in Aliments) c[j] * x[j];

/* Contraintes */
subject to {
  /* Contrainte de satisfaction des besoins nutritionnels */
  forall(i in Nutritifs)
      sum(j in Aliments) q[i][j] * x[j] >= d[i];
      
  /* Contrainte de positivité */
  forall(j in Aliments)
      x[j] >= 0;
}