import numpy as np

# Suppression de la limite de digits pour les valeurs
import sys

sys.set_int_max_str_digits(0)

########################################################################

# Fichier ou sont stockés les données du mouvement du pendule
fichier_source = "mvts_pendule.txt"

# Fichier où stocker la seed
fichier_graine = "seed.txt"

########################################################################

# Initialiser une liste pour contenir les colonnes
colonnes = []

# Lire les lignes du fichier
f_pendule = open(fichier_source, "r")
lignes = f_pendule.readlines()
for line in lignes:
    # Diviser la ligne en valeurs séparées par des tabulations
    values = line.strip().split("\t")
    # Ajouter les valeurs à leurs colonnes respectives
    for i in range(len(values)):
        if i < len(colonnes):
            colonnes[i].append(values[i])
        else:
            colonnes.append([values[i]])

col = [[] for _ in range(len(colonnes))]

for i in range(len(colonnes)):
    for value in colonnes[i]:
        col[i].append(np.abs(int(float(value.replace(",", ".")) * 1000)))

chaine = ""
for i in range(len(col)):
    for j in range(len(col[0])):
        chaine += str(bin(col[i][j])[2:])

########################################################################

f_seed = open(fichier_graine, "w")
f_seed.write(str(int(chaine, 2)))

f_seed.close()
f_pendule.close()
