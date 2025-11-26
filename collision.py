def collision(x1, y1, img1, x2, y2, img2) :
    liste_1 = []
    liste_2 = []
    for i in range(len(img1)) :
        for j in range(len(img1[0])) :
            liste_1.append((i+x1,j+y1)) 
    for i in range(len(img2)) :
        for j in range(len(img2[0])) :
                liste_2.append((i+x2, j+y2))
    for element in liste_1 :
         if element in liste_2 :
              return True
    return False