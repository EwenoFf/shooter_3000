import sys
import time
import select
import tty
import termios
import Background as background
import Affiche as affiche
class Interface: pass

liste_couleurs = ["\u001b[48;5;116m ","\u001b[48;5;220m ","\u001b[48;5;144m ","\u001b[48;5;216m ","\u001b[48;5;27m ","\u001b[48;5;20m ","\u001b[48;5;250m ","\u001b[48;5;202m ","\u001b[48;5;124m ","\u001b[48;5;152m ","\u001b[48;5;31m ","\u001b[48;5;58m ","\u001b[48;5;28m ","\u001b[48;5;94m ","\u001b[48;5;244m ","\u001b[48;5;17m ","\u001b[48;5;232m "]

def inter(bienvenue, x, y, img):
    x = x - 20
    y = y - 15
    affiche.add(bienvenue[0], x + 15, y + 15,  img)
    affiche.add(bienvenue[1],x + 15,y + 30 , img)
    affiche.add(bienvenue[2],x+45,y+45,img)
def show_space(bienvenue,x,y,img):
    x = x - 20
    y = y - 15
    affiche.add(bienvenue[1],x + 15,y + 30 , img)


def show_all(img, liste_couleurs, blink=True):
    liste_lettre = ["a","b","c","d","e","f","g"]
    sys.stdout.write("\033[?25l")
    for i in range(len(img)):
        for j in range(len(img[0])):
            txt = "\033["+str(i)+";"+str(j)+"H"
            sys.stdout.write(txt)
            if blink:
                try:
                    sys.stdout.write(liste_couleurs[int(img[i][j])])
                except:
                    for w in range(len(liste_lettre)):
                        if img[i][j] == liste_lettre[w]:
                            sys.stdout.write(liste_couleurs[10+w])
            else:
                sys.stdout.write(" ")  # Effacer la ligne si blink=False
    sys.stdout.write(liste_couleurs[16])
    sys.stdout.write("\033[?25h")

def is_data():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def run(bienvenue, data):
    c = 0
    blink = True
    while c < 15 and data["game"] == "menu":  # Mettez ici votre condition variable c
        img = background.create("g", 200, 45)
        show_space(bienvenue,46,5,img)
        inter(bienvenue, 46, 5, img)
        show_all(img, liste_couleurs, blink)
        blink = not blink  # Inverser l'état de clignotement
        time.sleep(1) # Temps d'attente entre chaque inversion
        
        c += 1  # Augmenter la variable c à chaque itération
        
        if is_data():
            f = sys.stdin.read(1)
            if f == " ":
                data["game"] = "jeu"
            if f == "i":
                data["game"] = "info"
    show_all(img, liste_couleurs, blink=True)  # Afficher le texte sans clignotement
    



  
def bienvenue(data) : 
    ecriture_bienvenue = affiche.image("bienvenue.txt")
    space = affiche.image("space.txt")
    info = affiche.image("info.txt")
    alphabet = [ecriture_bienvenue,space,info]
    run(alphabet, data)
