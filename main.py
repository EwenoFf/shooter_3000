import Vaisseau
import Affiche as affiche
import sys
import time
import select, random
import tty
import termios
import Tir as tir 
import Background as bg
import num
import Interface as interface
from copy import deepcopy
import monstre, collision,loose,info

class Main : pass
liste_couleurs = ["\u001b[48;5;116m ","\u001b[48;5;220m ","\u001b[48;5;144m ","\u001b[48;5;216m ","\u001b[48;5;27m ","\u001b[48;5;20m ","\u001b[48;5;250m ","\u001b[48;5;202m ","\u001b[48;5;124m ","\u001b[48;5;152m ","\u001b[48;5;31m ","\u001b[48;5;58m ","\u001b[48;5;28m ","\u001b[48;5;94m ","\u001b[48;5;244m ","\u001b[48;5;17m ","\u001b[48;5;232m "]
old_settings = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin.fileno())
def main() : 
    data = {}
    init(data)
    run(data)
    
  

def init(data):
    data["timestep"]=0.01
    data["background"]=bg.create("g",200,45)
    data["c"] = 0
    data["game"] = "menu" 
    data["loose"] = affiche.image("perdu.txt")
    data["vie"] = num.Num(140,15,"coeur.txt")
    data["info"] = affiche.image("info2.txt")
    data["nombre_ennemi"] = 0
    data["vaisseau"] = Vaisseau.create(90, 33, "vaisseau.txt")
    data["tir"] = [tir.create(data["vaisseau"].x,data["vaisseau"].y,"bullet.txt", False) ]
    data["monstre"] = [monstre.create(data)]
    data["bienvenue"]= affiche.image("bienvenue.txt")
    data["nombre_ennemi"] = 0
    data["life"] = 3
    data["score"] = 0
    data["affiche_score"] = num.Num(25,55, "coeur.txt")
    


def show_all(img, liste_couleurs) :
    liste_lettre = ["a","b","c","d","e","f","g"]
    sys.stdout.write("\033[?25l")#masquer le curseur pour arreter le scintillement de l'écran
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
    sys.stdout.write("\033[?25h") #remettre le curseur 
def interact(data) :
    if is_data() :
        c = sys.stdin.read(1)
        if c =="q" :
            
            Vaisseau.go_left(data["vaisseau"])
        elif c == "d":
            
            Vaisseau.go_right(data["vaisseau"])
        elif c =="\x1b" :
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
            sys.exit()
        elif c == "z" :
            Vaisseau.go_up(data["vaisseau"])
            
        elif c == "s" :
            Vaisseau.go_down(data["vaisseau"])
        elif c == " " :
            return True
            
            

def is_data() :
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])


def run(data) :
    init(data)
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
    
    while True :
        while data["game"] == "menu" :
            interface.bienvenue(data)
            
            if is_data():
                c = sys.stdin.read(1)
                if c == " ":
                    data["game"] = "jeu"
                if c == "i":
                    data["game"] = "info"

                
                    
                    
                interact(data)
        while data["game"] == "jeu" :
            img = deepcopy(data["background"])
            data["img"] = img
            affiche.add(affiche.image("h_1.txt"), 0, 0, img)
            if interact(data) : 
                data["tir"].append(tir.create(data["vaisseau"].x+5,data["vaisseau"].y,"bullet.txt"))
            for element in data["tir"]:
                if element.shoot : 
                    affiche.add(element.img, element.x, element.y, img)
                    tir.move(element)
            if random.randint(0,50) == 0 and data["nombre_ennemi"] <= 7:
                data["monstre"].append(monstre.create(data))
            
            for element in data["monstre"] :
                if element.alive :
                    affiche.add(element.img, element.x, element.y, img)
                    element.time += 10
                    
                    if element.time%100 == 0 :
                        monstre.move_down(element, data)
                    for tirer in data["tir"] :
                        monstre.death(element,tirer, data)
            
            if data["life"] !=0 : 
                data["vie"].run(data)
                data["affiche_score"].score(data)
            if data["life"] == 0 : 
                data["game"] = "mort"
                data["vie"].run(data)
                data["affiche_score"].score(data)

                             
                
                
             
            affiche.add(data["vaisseau"].img, data["vaisseau"].x, data["vaisseau"].y, img)
            
            show_all(img, liste_couleurs)
            
        while data["game"] == "mort" :
            loose.defaite(data)
            
            if interact(data) :
                init(data)
        while data['game'] == "info":
            info.information(data)
            

            

if __name__ =="__main__":
    main()



    



