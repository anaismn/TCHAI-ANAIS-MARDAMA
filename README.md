# Projet TP : Systèmes d'information avancés

## __Mise en place de l'environnement et des outils__

**Objectif : concevoir un système de transactions électroniques avec une intégrité garantie, accessible
par le protocole HTTP.** (Le choix des technologies employées est libre.)

### Outils choisis
* Langage de programmation : **Python**  
C'est le langage de prédilection pour les experts de la manipulation des grandes bases de données.

* Framework web : **Flask**  
Naturellement, un framework reposant sur Python est donc nécessaire. De plus, on a pu l'étudier en TD.

* Système de stockage de données : **fichier.txt**  
Puisque ce projet n'est qu'un exercice qui a pour objectif l'application du hashage et de son intérêt. Il serait préférable d'avoir une petite quantité de données à manipuler.  
L'utilisation d'un outil dédier aux données n'est pas primordiale.

### Installation
_Le travail réalisé a été effectué sur un environnement Windows._

Pour lancer le serveur Flask sur Windows dans le *cmd* :  
```
> cd venv\Scripts   
> activate
> set FLASK_APP= <path:file.py>
> flask run
```

Pour visualiser la page web générée : http://localhost:5000/

La base de données est le fichier _*data.txt*_  
Elle est construite comme ci-dessous : 
> Personne1 Personne2 Montant Date

La date est sous le format : **Y-m-d** (Année-Mois-Jour)

## Tchai 1
### Script Attaque
_Les attaques ont étés fait par le biais de PowerShell_  
**Attaque :** modifier directement le fichier de données, en changeant le montant d’une transaction.  

Le montant a changé est repéré par sa valeur. Il faut donc donner la valeur du montant que l'on souhaîte changé.
```
> .\tests\tchai1_Attaque.ps1 <ancienMontant> <nouveauMontant> <path:data.txt> 
```

### Test
1. Lancer le serveur Flask et visualiser les transactions sur la page localhost  
Relever la valeur du montant que vous souhaitez modifier (ce sera votre `<ancienMontant>`)
2. Executer le script d'attaque dans Powershell
3. Relancer le serveur et visualiser dans une nouvelle page les transactions

En comparant les deux listes de transactions, vous pourrez observer que le changement a bien été fait.

## Auteur
Anaïs Mardama Nayagom : a.mardama@rt-iut.re