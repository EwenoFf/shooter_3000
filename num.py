import Affiche as affiche
import Background as background
import termios
import sys,select,tty,time
class Num :
    liste_couleurs = ["\u001b[48;5;116m ","\u001b[48;5;220m ","\u001b[48;5;144m ","\u001b[48;5;216m ","\u001b[48;5;27m ","\u001b[48;5;20m ","\u001b[48;5;250m ","\u001b[48;5;202m ","\u001b[48;5;124m ","\u001b[48;5;152m ","\u001b[48;5;31m ","\u001b[48;5;58m ","\u001b[48;5;28m ","\u001b[48;5;94m ","\u001b[48;5;244m ","\u001b[48;5;17m ","\u001b[48;5;232m "]
    def __init__( self,x, y, img):
        
        self.x = x - 20
        self.y = y - 15
        self.img = affiche.image(img)

    def set_x(self, val) : self.x = val
    def set_y(self, val) : self.y = val
        

    def show_all(self,img, liste_couleurs) :
        liste_lettre = ["a","b","c","d","e","f","g"]
        sys.stdout.write("\033[?25l")
        for i in range(len(self.img)) :
            for j in range(len(self.img[0])) :
                txt = "\033["+str(i)+";"+str(j)+"H"     
                sys.stdout.write(txt)
                try :
                    sys.stdout.write(liste_couleurs[int(self.img[i][j])]) #si img[i][j] est un int
                except :
                    for w in range(len(liste_lettre)) :
                        if self.img[i][j] == liste_lettre[w] :
                            sys.stdout.write(liste_couleurs[10+w])
        sys.stdout.write(liste_couleurs[16])
        sys.stdout.write("\033[?25h")

    def is_data():
        return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])


    def run(self, data):
        
        if data["life"] == 3 :
            affiche.add(affiche.image("coeur.txt"),170,2,data["img"])

        elif data["life"] == 2 :
            affiche.add(affiche.image("coeur1.txt"), 170, 2, data["img"])
        elif data["life"] == 1 :
            affiche.add(affiche.image("coeur2.txt"), 170, 2, data["img"])
                
    def score(self, data) :
        for i in range(len(str(data["score"]))) :
            affiche.add(affiche.image(str(data["score"])[i]+".txt"),self.x+5*i, self.y, data["img"] )
        
    

        

            




