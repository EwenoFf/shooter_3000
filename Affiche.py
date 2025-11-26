
def image(file) :
    liste_final = []
    with open(file,"r") as fichier :
        lignes = fichier.readlines()
    # Supprimer les caractères de nouvelle ligne (\n) de chaque ligne
    lignes = [ligne.strip() for ligne in lignes]
    for element in lignes :
        petite_liste = []
        for elmt in element :
            petite_liste.append(elmt)
        liste_final.append(petite_liste)
    return liste_final


def add(a_ajouter, x, y, img) :
    x_de_base = x
    for i in range(len(a_ajouter)) : 
        x = x_de_base
        for j in range(len(a_ajouter[i])) :
            if a_ajouter[i][j] != "h" and a_ajouter[i][j] != " " :
                img[y][x] = a_ajouter[i][j]
            x+=1
        y += 1
    return img
