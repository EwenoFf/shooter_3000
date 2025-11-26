import sys,time,tty,termios,select
import Affiche as affiche

liste_couleurs = ["\u001b[48;5;116m ","\u001b[48;5;220m ","\u001b[48;5;144m ","\u001b[48;5;216m ","\u001b[48;5;27m ","\u001b[48;5;20m ","\u001b[48;5;250m ","\u001b[48;5;202m ","\u001b[48;5;124m ","\u001b[48;5;152m ","\u001b[48;5;31m ","\u001b[48;5;58m ","\u001b[48;5;28m ","\u001b[48;5;94m ","\u001b[48;5;244m ","\u001b[48;5;17m ","\u001b[48;5;232m "]


class Vaisseau : pass

def create(x, y, img) :
    v = Vaisseau()
    v.x = x
    v.y = y
    v.img = affiche.image(img)
    return v

def get_x(v) : return  v.x
def get_y(v) : return v.y
def get_img(v) : return v.img
    

def set_x(v,x) : 
    v.x = x

def set_y(v,y) :
    v.y = y 

def set_img(v, img):
    v.img = affiche.image(img)

def go_right(v) :
    if v.x < 175 :
        v.x += 3
        return v

def go_left(v) :
    if v.x > 1 :
        v.x -= 3
        return v

def go_up(v) :
    if v.y > 1 :
        v.y -= 1
        return v 

def go_down(v) :
    if v.y < 38 :
        v.y += 1
        return v 

def add(v,img) :
    x_de_base = v.x
    x = v.x
    y = v.y
    for i in range(len(v.img)) : 
        x = x_de_base
        for j in range(len(v.img[i])) :
            if v.img[i][j] != "h" and v.img[i][j] != " " :
                img[y][x] = v.img[i][j]
            x+=1
        y += 1
    return img

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



        
        
        