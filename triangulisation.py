
# So we have 
# Grandeur des côtés d'un triangle => Rectangle = ?
# Nombre => Premier ?
# (divisible uniquement par lui-même ou par 1)

def triangulisation(longueur_cote_a: float, longueur_cote_b: float, longueur_cote_c: float) -> bool:

    liste_de_cotes = [longueur_cote_a, longueur_cote_b, longueur_cote_c]
    liste_de_cotes_triee = sorted(liste_de_cotes)
    print(liste_de_cotes_triee)
    liste_des_cathetes = [liste_de_cotes_triee[0], liste_de_cotes_triee[1]]
    hypothenuse = liste_de_cotes_triee[2]

    carre_de_lhypotenuse = hypothenuse**2
    print(carre_de_lhypotenuse)
    carre_du_cathete_a = liste_des_cathetes[0]**2
    carre_du_cathete_b = liste_des_cathetes[1]**2
    somme_des_carres_des_cathetes = carre_du_cathete_a + carre_du_cathete_b
    if round(carre_de_lhypotenuse, 4) == round(somme_des_carres_des_cathetes, 4):
        return True
    else:
        return False
    

print(triangulisation(3.33333,4.44444,5.55555))