import math

# Suppression de la limite de digits pour les valeurs
import sys

sys.set_int_max_str_digits(0)

########################################################################

# Fichier où est stockée la graine
fichier_seed = "seed.txt"

# Fichier pour stocker les nombres aléatoires
fichier_nombres = "generation.txt"

# Nombre de générations
nb_generations = 10**7

# Choix de l'intervalle : génération des nombres entre 1 et n
n = 100

########################################################################


# Algorithme BBS utilisé pour la génération des nombres
def blumBlumShub(seed):

    # Choix de deux nombres p et q congrus à 3 mod 4
    p = 2**107 - 1
    q = 2**127 - 1
    M = p * q

    # Nombre de bits réellement aléatoires
    k = max(1, math.floor(math.log2(math.log2(M))))
    masque_k = (1 << k) - 1

    # Nombre de bits nécessaires pour générer un nombre entre 1 et n
    bits_par_nombre = (n - 1).bit_length()
    masque_nombre = (1 << bits_par_nombre) - 1

    x = seed % M
    while math.gcd(x, M) != 1:
        x -= 1

    x = pow(x, 2, M)

    print(f"p = {p}")
    print(f"q = {q}")
    print(f"M = {M}")
    print(f"k = {k}")
    print(f"n = {bits_par_nombre}")

    # Génération des bits et écriture dans le fichier
    bit_buffer = 0
    bit_count = 0
    lignes_buffer = []
    generes = 0

    while generes < nb_generations:

        while bit_count < bits_par_nombre:
            x = pow(x, 2, M)
            bit_buffer = (bit_buffer << k) | (x & masque_k)
            bit_count += k

        bit_count -= bits_par_nombre
        valeur = (bit_buffer >> bit_count) & masque_nombre
        bit_buffer &= (1 << bit_count) - 1

        if valeur < n:
            lignes_buffer.append(f"{valeur + 1}\n")
            generes += 1

            if len(lignes_buffer) >= 100000:
                f_nombres.writelines(lignes_buffer)
                lignes_buffer.clear()

    if lignes_buffer:
        f_nombres.writelines(lignes_buffer)
    return


########################################################################

with open(fichier_seed, "r") as f_seed:
    int_seed = int(f_seed.read().strip())

with open(fichier_nombres, "w") as f_nombres:
    blumBlumShub(int_seed)
