> [!CAUTION]
Ce travail s'effectue dans [l'environnement Github](https://perso.esiee.fr/~courivad/courses/utils/misc-01-github-environment.html)

# Liste de Syracuse

Cet exercice est la continuité d'un exercice précédent sur [les suites de Syracuse](https://perso.esiee.fr/~courivad/courses/exercices/ex04-suites-syracuse.html) pour lequel les valeurs de la suite étaient calculées à la volée sans mémorisation. L'objectif est ici de les stocker dans une liste pour post traitement.

Le fichier ``main.py`` contient :

- une fonction secondaire ``syr_plot()`` (NE PAS MODIFIER) qui permet de construire un graphique. 

- une fonction secondaire ``syracuse_l()``
  
  - qui prend en argument un entier ``n`` ;
  - et retourne la liste des valeurs de la suite.

- une fonction secondaire ``temps_de_vol()``
  
  - qui prend en argument une liste de Syracuse ``l`` ;
  - et retourne son temps de vol.

- une fonction secondaire ``temps_de_vol_en_altitude()``
  
  - qui prend en argument une liste de Syracuse ``l`` ;
  - et retourne son temps de vol en altitude.

- une fonction secondaire ``altitude_maximale()``
  
  - qui prend en argument une liste de Syracuse ``l`` ;
  - et retourne son altitude maximale.

- la fonction principale ``main()`` qui fait appel aux fonctions secondaires pour vérifier leur bon fonctionnement .

## To do

1️⃣ Ecrire (ou modifier) le code de la fonction secondaire.

2️⃣ Si nécessaire, ajouter (ou modifier) les appels à la fonction secondaire logés dans la fonction principale ``main()``. Cela permet de tester la fonction secondaire sur quelques cas simples.

3️⃣ Exécuter le programme depuis le terminal. Tant que la fonction secondaire ne retourne pas les résultats attendus, répéter le cycle 1️⃣ 2️⃣ 3️⃣.

    $ python main.py

4️⃣ Lorsque les résultats obtenus à l'étape 3️⃣ sont satisfaisants, soumettre le code à une procédure de test plus robuste, les tests unitaires.

    $ pytest .python

Le score de test ``ST`` obtenu est le pourcentage de tests réussis. Tant que certains tests échouent, répéter le cycle 1️⃣ 2️⃣ 3️⃣ 4️⃣

5️⃣ Lorsque le score de test ``ST`` est satisfaisant, s'intéresser à la [qualité du code](https://perso.esiee.fr/~courivad/courses/utils/sources/python-23-codequality.html).

    $ pylint main.py

Si le score de qualité ``SQ`` n'est pas maximal, répéter l'étape 5️⃣ en tenant compte des messages dans le terminal

6️⃣ Lorsque les scores ``ST`` et ``SQ`` sont satisfaisants, initialiser les variables d'environnement fournies dans BlackBoard puis pusher le travail pour évaluation

    $ git add .
    $ git commit -m "un message explicatif"
    $ git push

> [!CAUTION]
En cas de soumissions multiples, seule la première est prise en compte.