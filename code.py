import math

# Définition des variables
total_boules = 7  # Total des boules (3 rouges + 4 vertes)
boules_a_tirer = 2  # On tire deux boules

# 1) Tirage simultané de 2 boules sans remise (combinaison)
# Calcul des combinaisons (C_7^2)
combinaison_simultanée = math.comb(total_boules, boules_a_tirer)
print("Nombre de possibilités pour le tirage simultané (C_7^2) :", combinaison_simultanée)

# 2) Tirage successif sans remise (arrangement)
# Calcul des arrangements sans remise (A_7^2)
arrangement_sans_remise = math.perm(total_boules, boules_a_tirer)
print("Nombre de possibilités pour le tirage successif sans remise (A_7^2) :", arrangement_sans_remise)

# 3) Tirage successif avec remise
# Ici, chaque tirage est indépendant, donc on multiplie le nombre de choix possibles (7) pour chaque tirage
tirage_avec_remise = total_boules ** boules_a_tirer
print("Nombre de possibilités pour le tirage successif avec remise (7^2) :", tirage_avec_remise)
