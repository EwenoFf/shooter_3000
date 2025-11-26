import Affiche as affiche
import Background as background
import termios, num
import sys,select,tty,time
class Loose : pass 
liste_couleurs = ["\u001b[48;5;116m ","\u001b[48;5;220m ","\u001b[48;5;144m ","\u001b[48;5;216m ","\u001b[48;5;27m ","\u001b[48;5;20m ","\u001b[48;5;250m ","\u001b[48;5;202m ","\u001b[48;5;124m ","\u001b[48;5;152m ","\u001b[48;5;31m ","\u001b[48;5;58m ","\u001b[48;5;28m ","\u001b[48;5;94m ","\u001b[48;5;244m ","\u001b[48;5;17m ","\u001b[48;5;232m "]
def show(defaite, x, y, img):
    x = x - 20
    y = y - 15
    affiche.add(defaite[0], x + 15, y + 15,  img)

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

def is_data():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])


def run(defaite, data):
    img = background.create("g", 200, 45)
    data["img"] = img
    affiche.add(affiche.image("perdu.txt"), 50, 5, img)
    affiche.add(affiche.image("vaisseau_explose.txt"),80,15,img)
    data["affiche_score"].set_x(115)
    data["affiche_score"].set_y(32)
    data["affiche_score"].score(data)
    affiche.add(affiche.image("affiche_score.txt"),65,32,img)
    show_all(img, liste_couleurs)          
  
def defaite(data) : 
    ecriture_defaite = affiche.image("perdu.txt")
    alphabet_defaite = [ecriture_defaite]
    run(alphabet_defaite, data)
      

        




