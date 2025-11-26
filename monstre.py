import Affiche, random
import collision
class Monstre : pass 


def create(data,tir = False) :
    m = Monstre()
    m.x = random.randint(3, 180)
    m.y = 0
    m.img = Affiche.image("monstre.txt")
    m.tir = tir
    m.time = 0
    m.alive = True
    m.life = False 
    data["nombre_ennemi"] += 1
    return m 

def move_left(m) :
    m.x -= 1

def move_right(m) :
    m.x += 1

def move_down(m, data):
    if m.alive :
        if m.y < 35 :
            m.y += 1
        else :
            data["nombre_ennemi"] -= 1
            m.alive = False
            data["life"]-=1

def death(m,t,data) :
    if m.alive :
        if collision.collision(m.x, m.y, m.img, t.x, t.y, t.img) and t.shoot     :
            m.alive = False 
            data["score"] += 1
            data["nombre_ennemi"] -= 1

