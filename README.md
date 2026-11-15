# TIPE : Génération de nombres aléatoires à l'aide de systèmes chaotiques

**Information importante :** ce projet n'est plus mis à jour depuis sa présentation lors de mon TIPE en juillet 2025.

## Présentation du projet

Ce projet contient le code source de mon **TIPE (Travaux d'Initiative Personnelle Encadrés)** en CPGE portant sur la génération de nombres pseudo-aléatoires à partir de sources d'entropie physiques chaotiques (lampe à lave et pendule double).

## Descriptif des fichiers

### 1. Sources d'entropie et génération de la graine
- **`pendule_double.py`** : Simulation numérique du pendule double par la méthode de **Runge-Kutta d'ordre 4 (RK4)**. Observation du phénomène chaotique grâce au lancement de deux pendules à $10^{-3}$ radian d'écart.

- **`pendule_graine.py`** : Exploitation d'une chronophotographie expérimentale du mouvement d'un pendule (`mvts_pendule.txt`) pour obtenir une seed.

- **`graine_lampe.py`** : Extraction d'entropie depuis une photo d'une lampe à lave.


### 2. Générateur pseudo-aléatoire
- **`graine_nombres.py`** : Implémentation du générateur cryptographique **Blum-Blum-Shub** et génération de 10 millions d'entiers entre 1 et 100.

### 3. Analyse statistique
- **`analyse_nombres.py`** : Analyse des résultats obtenus avec le test du $\chi^2$.

## Dépendances

- `Python 3.11+`
- `NumPy`
- `Matplotlib`
- `Pillow`

## Exécution

Il est possible d'utiliser `uv` avec les fichiers `uv.lock` et `pyproject.toml`. Chaque fichier d'exemple nécessaire est déjà fourni (`mvts_pendule.txt`, `img_lampe.png`, `seed.txt`), libre à vous de les changer pour tester avec vos paramètres.