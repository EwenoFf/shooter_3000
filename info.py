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
    sys.stdout.write("\033[?25l")
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
    sys.stdout.write("\033[?25h")

def is_data():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])


def run(information, data):
    img = background.create("g", 200, 45)
    data["img"] = img
    affiche.add(affiche.image("info2.txt"), 10, 5, img)
    old_settings = termios.tcgetattr(sys.stdin)
    if is_data():
        c = sys.stdin.read(1)
        if c =="\x1b" :
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
            data["game"] = "menu" 

    show_all(img, liste_couleurs)          
  
def information(data) : 
    ecriture_information = affiche.image("info2.txt")
    alphabet_information = [ecriture_information]
    run(alphabet_information, data)
      

        




