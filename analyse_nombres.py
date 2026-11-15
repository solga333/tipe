import numpy as np
import matplotlib.pyplot as plt

########################################################################

# Fichier où sont stockés les nombres aléatoires
fichier_donnees = "generation.txt"

########################################################################

# Récupération des nombres
donnees = open(fichier_donnees, "r")
lignes = donnees.readlines()
tab_nombres = []
for line in lignes:
    tab_nombres.append(int(line, 10))
donnees.close()

# Fréquence de chaque nombre
occurrences = np.zeros(100)
for nombre in tab_nombres:
    occurrences[nombre - 1] += 1

# Création du diagramme
ex_nombres = np.linspace(1, 100, 100)
plt.bar(ex_nombres, occurrences)
plt.xlabel("Nombres")
plt.axhline(
    y=100000, color="r", linestyle="-", linewidth=1, label="Fréquence théorique"
)
plt.ylabel("Occurrences")
plt.title(
    r"Fréquence d'apparition de chaque nombre | $10^7$ nombres entre $1$ et $100$"
)
plt.legend()


### Test du Chi^2
o_i = 100000
chi_2 = 0
for e_i in occurrences:
    chi_2 += ((o_i - e_i) ** 2) / e_i
print(chi_2)
chi_2_ref = 123.23  # valeur du chi_2 pour 99 degrés de liberté à 0.05
if chi_2 < chi_2_ref:
    print("Equilibré")
else:
    print("Déséquilibré")

plt.show()
