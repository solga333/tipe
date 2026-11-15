# Calcul des données
import numpy as np

# Animation du pendule
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

########################################################################

# Valeurs initiales et constantes

l_1 = 1.0
l_2 = 1.0
m_1 = 1.0
m_2 = 1.0
theta_init_1 = np.pi
theta_init_2 = np.pi / 4
g = 9.81
h = 0.05
duree_sim = 12

"""
Paramètres:
- l_1, l_2: Longueurs des cordes (m)
- m_1, m_2: Masses des pendules (kg)
- theta_init_1, theta_init_2: Angles initiaux des deux pendules par rapport à l'axe vertical (rad)
- g: Constante de pesanteur terrestre (en m/s²)
- h: Durée entre chaque image de la simulation (s)
- duree_sim: Durée totale de la simulation (s)
"""

########################################################################

# Calcul du nombre total d'étapes
nb_etapes = int(duree_sim / h)

# Initialisation des tableaux pour stocker les angles et les temps
theta_1_p1 = np.zeros(nb_etapes)
theta_2_p1 = np.zeros(nb_etapes)
theta_1_p2 = np.zeros(nb_etapes)
theta_2_p2 = np.zeros(nb_etapes)
t = np.linspace(0, duree_sim, nb_etapes)

# Angles initiaux pour les deux pendules
theta_1_p1[0] = theta_init_1
theta_2_p1[0] = theta_init_2
theta_1_p2[0] = theta_init_1 + 0.001  # Différence d'un millième de radian
theta_2_p2[0] = theta_init_2

# Vitesse angulaire initiale
dot_theta_1_p1, dot_theta_2_p1 = 0.0, 0.0
dot_theta_1_p2, dot_theta_2_p2 = 0.0, 0.0

# Tableaux pour stocker les positions de l'extrémité des pendules doubles (de chaque masse)
x2_trajectoire_p1 = np.zeros(nb_etapes)
y2_trajectoire_p1 = np.zeros(nb_etapes)
x2_trajectoire_p2 = np.zeros(nb_etapes)
y2_trajectoire_p2 = np.zeros(nb_etapes)


# Fonction pour calculer les dérivées des angles, plus particulièrement pour obtenir l'accélération de chaque pendule
def deriver(theta_1, theta_2, dot_theta_1, dot_theta_2):
    delta = theta_1 - theta_2
    gamma1 = (m_1 + m_2) * l_1 - m_2 * l_1 * np.cos(delta) ** 2
    gamma2 = (l_2 / l_1) * gamma1

    ddot_theta_1 = (
        m_2 * g * np.sin(theta_2) * np.cos(delta)
        - m_2
        * np.sin(delta)
        * (l_2 * dot_theta_2**2 + l_1 * dot_theta_1**2 * np.cos(delta))
        - (m_1 + m_2) * g * np.sin(theta_1)
    ) / gamma1

    ddot_theta_2 = (m_1 + m_2) * (
        l_1 * dot_theta_1**2 * np.sin(delta)
        - g * np.sin(theta_2)
        + g * np.sin(theta_1) * np.cos(delta)
    ) + (m_2 * l_2 * dot_theta_2**2 * np.sin(delta) * np.cos(delta)) / gamma2

    return np.array([dot_theta_1, dot_theta_2, ddot_theta_1, ddot_theta_2])


# Calcul des angles pour chaque image
for i in range(1, nb_etapes):
    # Pendule 1
    k1_p1 = deriver(
        theta_1_p1[i - 1], theta_2_p1[i - 1], dot_theta_1_p1, dot_theta_2_p1
    )
    k2_p1 = deriver(
        theta_1_p1[i - 1] + 0.5 * h * k1_p1[0],
        theta_2_p1[i - 1] + 0.5 * h * k1_p1[1],
        dot_theta_1_p1 + 0.5 * h * k1_p1[2],
        dot_theta_2_p1 + 0.5 * h * k1_p1[3],
    )
    k3_p1 = deriver(
        theta_1_p1[i - 1] + 0.5 * h * k2_p1[0],
        theta_2_p1[i - 1] + 0.5 * h * k2_p1[1],
        dot_theta_1_p1 + 0.5 * h * k2_p1[2],
        dot_theta_2_p1 + 0.5 * h * k2_p1[3],
    )
    k4_p1 = deriver(
        theta_1_p1[i - 1] + h * k3_p1[0],
        theta_2_p1[i - 1] + h * k3_p1[1],
        dot_theta_1_p1 + h * k3_p1[2],
        dot_theta_2_p1 + h * k3_p1[3],
    )

    theta_1_p1[i] = theta_1_p1[i - 1] + (h / 6) * (
        k1_p1[0] + 2 * k2_p1[0] + 2 * k3_p1[0] + k4_p1[0]
    )
    theta_2_p1[i] = theta_2_p1[i - 1] + (h / 6) * (
        k1_p1[1] + 2 * k2_p1[1] + 2 * k3_p1[1] + k4_p1[1]
    )
    dot_theta_1_p1 += (h / 6) * (k1_p1[2] + 2 * k2_p1[2] + 2 * k3_p1[2] + k4_p1[2])
    dot_theta_2_p1 += (h / 6) * (k1_p1[3] + 2 * k2_p1[3] + 2 * k3_p1[3] + k4_p1[3])

    # Pendule 2
    k1_p2 = deriver(
        theta_1_p2[i - 1], theta_2_p2[i - 1], dot_theta_1_p2, dot_theta_2_p2
    )
    k2_p2 = deriver(
        theta_1_p2[i - 1] + 0.5 * h * k1_p2[0],
        theta_2_p2[i - 1] + 0.5 * h * k1_p2[1],
        dot_theta_1_p2 + 0.5 * h * k1_p2[2],
        dot_theta_2_p2 + 0.5 * h * k1_p2[3],
    )
    k3_p2 = deriver(
        theta_1_p2[i - 1] + 0.5 * h * k2_p2[0],
        theta_2_p2[i - 1] + 0.5 * h * k2_p2[1],
        dot_theta_1_p2 + 0.5 * h * k2_p2[2],
        dot_theta_2_p2 + 0.5 * h * k2_p2[3],
    )
    k4_p2 = deriver(
        theta_1_p2[i - 1] + h * k3_p2[0],
        theta_2_p2[i - 1] + h * k3_p2[1],
        dot_theta_1_p2 + h * k3_p2[2],
        dot_theta_2_p2 + h * k3_p2[3],
    )

    theta_1_p2[i] = theta_1_p2[i - 1] + (h / 6) * (
        k1_p2[0] + 2 * k2_p2[0] + 2 * k3_p2[0] + k4_p2[0]
    )
    theta_2_p2[i] = theta_2_p2[i - 1] + (h / 6) * (
        k1_p2[1] + 2 * k2_p2[1] + 2 * k3_p2[1] + k4_p2[1]
    )
    dot_theta_1_p2 += (h / 6) * (k1_p2[2] + 2 * k2_p2[2] + 2 * k3_p2[2] + k4_p2[2])
    dot_theta_2_p2 += (h / 6) * (k1_p2[3] + 2 * k2_p2[3] + 2 * k3_p2[3] + k4_p2[3])

    # Calcul des positions de l'extrémité des pendules doubles
    x1_p1 = l_1 * np.sin(theta_1_p1[i])
    y1_p1 = -l_1 * np.cos(theta_1_p1[i])
    x2_trajectoire_p1[i] = x1_p1 + l_2 * np.sin(theta_2_p1[i])
    y2_trajectoire_p1[i] = y1_p1 - l_2 * np.cos(theta_2_p1[i])

    x1_p2 = l_1 * np.sin(theta_1_p2[i])
    y1_p2 = -l_1 * np.cos(theta_1_p2[i])
    x2_trajectoire_p2[i] = x1_p2 + l_2 * np.sin(theta_2_p2[i])
    y2_trajectoire_p2[i] = y1_p2 - l_2 * np.cos(theta_2_p2[i])


# Création du plot pour l'animation
fig, ax = plt.subplots()
ax.set_xlim(-l_1 - l_2 - 0.1, l_1 + l_2 + 0.1)
ax.set_ylim(-l_1 - l_2 - 0.1, l_1 + l_2 + 0.1)
ax.set_aspect("equal")
(line_p1,) = ax.plot([], [], "o-", lw=2, color="blue")
(line_p2,) = ax.plot([], [], "o-", lw=2, color="red")
(trajectoire_p1,) = ax.plot([], [], "b-", lw=1, alpha=0.7)
(trajectoire_p2,) = ax.plot([], [], "r-", lw=1, alpha=0.7)
time_text = ax.text(0.02, 0.95, "", transform=ax.transAxes)


# Fonction d'initialisation pour l'animation
def init():
    line_p1.set_data([], [])
    line_p2.set_data([], [])
    trajectoire_p1.set_data([], [])
    trajectoire_p2.set_data([], [])
    time_text.set_text("")

    return line_p1, line_p2, trajectoire_p1, trajectoire_p2, time_text


# Fonction d'animation pour mettre à jour les données
def update(frame):
    x1_p1 = l_1 * np.sin(theta_1_p1[frame])
    y1_p1 = -l_1 * np.cos(theta_1_p1[frame])
    x2_p1 = x1_p1 + l_2 * np.sin(theta_2_p1[frame])
    y2_p1 = y1_p1 - l_2 * np.cos(theta_2_p1[frame])
    line_p1.set_data([0, x1_p1, x2_p1], [0, y1_p1, y2_p1])
    trajectoire_p1.set_data(x2_trajectoire_p1[:frame], y2_trajectoire_p1[:frame])

    x1_p2 = l_1 * np.sin(theta_1_p2[frame])
    y1_p2 = -l_1 * np.cos(theta_1_p2[frame])
    x2_p2 = x1_p2 + l_2 * np.sin(theta_2_p2[frame])
    y2_p2 = y1_p2 - l_2 * np.cos(theta_2_p2[frame])
    line_p2.set_data([0, x1_p2, x2_p2], [0, y1_p2, y2_p2])
    trajectoire_p2.set_data(x2_trajectoire_p2[:frame], y2_trajectoire_p2[:frame])

    time_text.set_text(f"t = {t[frame]:.2f} s")
    return line_p1, line_p2, trajectoire_p1, trajectoire_p2, time_text


# Création de l'animation
ani = FuncAnimation(
    fig,
    update,
    frames=nb_etapes,
    init_func=init,
    blit=True,
    interval=h * 1000,
)

plt.show()
