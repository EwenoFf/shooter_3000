import Affiche as affiche
import Vaisseau as v
import sys,time,tty,termios,select

class Tir : pass
liste_couleurs = ["\u001b[48;5;116m ","\u001b[48;5;220m ","\u001b[48;5;144m ","\u001b[48;5;216m ","\u001b[48;5;27m ","\u001b[48;5;20m ","\u001b[48;5;250m ","\u001b[48;5;202m ","\u001b[48;5;124m ","\u001b[48;5;152m ","\u001b[48;5;31m ","\u001b[48;5;58m ","\u001b[48;5;28m ","\u001b[48;5;94m ","\u001b[48;5;244m ","\u001b[48;5;17m ","\u001b[48;5;232m "]

def create(x,y,img, shoot= True ):
    t = Tir()
    t.x = x
    t.y = y
    t.img = affiche.image(img)
    t.shoot = shoot
    return t

def move(t):
    if t.shoot :
        t.y -= 1
        if t.y == 0 :
            t.shoot = False
    return t 

def erase(t):
    x = str(int(t.x))
    y = str(int(t.y)) 
    while t.y <= 0 :
        show_all("bullet.txt",liste_couleurs)
        t.shot = False
 
        
       
def set_img(t,img):
    t.img = affiche.image(img)

    
def est_sorti(t,hauteur):
    return t.y <= 0 or t.y >= hauteur-1


def show_all(img, liste_couleurs) :
    liste_lettre = ["a","b","c","d","e","f","g"]
    for i in range(len(img)) :
        for j in range(len(img[0])) :
            txt = "\033["+str(i)+";"+str(j)+"H"     
            sys.stdout.write(txt)
            try :
                sys.stdout.write(liste_couleurs[int(img[i][j])]) #si img[i][j] est un int
            except :
                for w in range(len(liste_lettre)) :
                    if img[i][j] == liste_lettre[w] :
                        sys.stdout.write(liste_couleurs[10+w])
    sys.stdout.write(liste_couleurs[16])

