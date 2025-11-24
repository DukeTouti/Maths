/*********************************************
 * OPL 22.1.1.0 Model
 * Author: hathouti
 * Creation Date: 19 nov. 2025 at 11:55:13
 *********************************************/

 /***** Exercice1.mod *****/
 /* Ensembles */
 
 {string} Ouvriers = ...;
 {string} Taches = ...;
 int Eff[Ouvriers][Taches] = ...;
 int Qual[Ouvriers][Taches] = ...; //Valeurs 0/1
 
 /* Variables de décision : x[i][j] = 1 si l'ouvrier i est affecté à la tâche j */
 dvar boolean x[Ouvriers][Taches];
 
 /* Objectif : maximiser l'efficacité totale */
 maximize
 	sum (i in Ouvriers, j in Taches) Eff[i][j] * x[i][j];
 	
 /* Contraintes */
 subject to {
   /* (1) Chaque ouvrier est affecté à exactement une tâche */
   forall (i in Ouvriers)
     sum (j in Taches) x[i][j] == 1;
   
   /* (2) Chaque tâche reçoit exactement un ouvrier */
   forall (j in Taches)
     sum (i in Ouvriers) x[i][j] == 1;
     
   /* (3) Interdictions (barres "--") : on force x[i][j] = 0 si non qualifié */
   forall (i in Ouvriers, j in Taches)
     x[i][j] <= Qual[i][j];
 }
  
