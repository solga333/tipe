# Ouverture et lecture des images
from PIL import Image

# Suppression de la limite de digits pour les valeurs
import sys

sys.set_int_max_str_digits(0)

########################################################################

# Image à analyser
fichier_image = "img_lampe.png"

# Fichier texte où stocker la graine
fichier_graine = "seed.txt"

########################################################################


# Transformer l'image en une matrice : longueur * largeur * [R,V,B]
def image_matrice(image):
    img = Image.open(image)
    # Convertir l'image en mode RVB
    img = img.convert("RGB")
    largeur, hauteur = img.size
    matrice = []
    for y in range(hauteur):
        ligne = []
        for x in range(largeur):
            rouge, vert, bleu = img.getpixel((x, y))
            ligne.append([rouge, vert, bleu])
        matrice.append(ligne)
    return matrice


# Transformer les valeurs de la matrice en une graine à utiliser
def matrice_graine(matrice):
    chaine = ""
    lenX = len(matrice)
    lenY = len(matrice[0])
    for i in range(lenX):
        for j in range(lenY):
            for k in range(3):
                nombre_binaire = bin(matrice[i][j][k])[2:]
                nombre_binaire = nombre_binaire.zfill(
                    8
                )  # remplissage de zéros à gauche
                chaine += str(nombre_binaire)
    return int(chaine, 2)


########################################################################

matrice_image = image_matrice(fichier_image)

seed = matrice_graine(matrice_image)

fichier = open(fichier_graine, "w")
fichier.write(str(seed))
fichier.close()
