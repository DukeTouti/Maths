/*********************************************
 * OPL 22.1.1.0 Model
 * Author: hathouti
 * Creation Date: 19 nov. 2025 at 21:43:49
 *********************************************/

 
 /***** trasnport1.mod *****/ 

 
 /* Paramètres */
int nbEntrepots = ...;
int nbClients = ...;

range Entrepots = 1..nbEntrepots;
range Clients = 1..nbClients;

float cout[Entrepots][Clients] = ...; /* coût de transport de l'entrepôt i vers le client j */
float stock[Entrepots] = ...; /* disponibilité à chaque entrepôt */
float demande[Clients] = ...; /* demande de chaque client */

/* Variables de décision */
dvar float x[Entrepots][Clients]; /* quantité transportée de l'entrepôt i vers le client j */

/* Fonction objectif : minimiser le coût total de transport */
minimize 
	sum(i in Entrepots, j in Clients) cout[i][j] * x[i][j];

/* Contraintes */
subject to {
  /* Contrainte de capacité : ne pas dépasser le stock disponible à chaque entrepôt */
  forall(i in Entrepots)
      sum(j in Clients) x[i][j] <= stock[i];
  
  /* Contrainte de demande : satisfaire la demande de chaque client */
  forall(j in Clients)
      sum(i in Entrepots) x[i][j] >= demande[j];
  
  /* Contrainte de positivité */
  forall(i in Entrepots, j in Clients)
      x[i][j] >= 0;
}
 
 