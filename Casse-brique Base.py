# Créé par Geoffroy, le 24/12/2015 en Python 3.2
from tkinter import *
from math import sqrt
import random
from winsound import *
x1 ,y1=300,400
dx1, dy1=5,5
yb, xb, dxb, cc=470,250,10,80
drapeau=0
gauche,droite=0,0
canX=600
banane = 0
listeBriques = []
score = 0
hitSound = "hit.wav"
breakSound = "break.wav"
overSound = "annoying.wav"
class Brique:
    def generer(self,height):
        self.brick = can1.create_rectangle(banane*50, height, banane*50+30, height+20, fill = self.couleur)

    def __init__(self, height, couleur):
        global banane, listeBriques
        banane +=1
        self.id = banane
        self.coords = [banane*50, height]
        listeBriques.append(self)
        self.couleur = couleur
        self.scorevalue = 0
        if self.couleur == "blue":
            self.hp = 1
        elif self.couleur == "red":
            self.hp = 2
        elif self.couleur == "green":
            self.hp = 3
        elif self.couleur == "gold2":
            self.hp = 10
            self.scorevalue = 5
        self.generer(height)
    def damage(self):
        global score 
        self.hp -= 1
        score += self.scorevalue
        if self.hp <=0:
            if self.couleur == "blue":
                self.scorevalue = 10
            elif self.couleur == "red":
                self.scorevalue = 15
            elif self.couleur == "green":
                self.scorevalue = 20
            elif self.couleur == "gold2":
                self.scorevalue = 50
                bonus_big(25000)
            score += self.scorevalue
            can1.delete(self.brick)
            listeBriques.remove(self)
            PlaySound(hitSound, SND_ASYNC)
            bonus_big(100)
        else:
            PlaySound(breakSound, SND_ASYNC)







def retablir_taille():
    global cc
    cc = 80

def bonus_big(duration):
    global cc
    cc = 120
    fen.after(duration, retablir_taille)

def direction(x):
    global dx1, dy1
    dx1=x/10
    dy1=-5

def les_briques_qui_se_cassent_lol():
    for brick in listeBriques:
        global x1, y1,dx1, dy1, txtscore
        if x1-20<=brick.coords[0]<=x1+40:
            if y1-20<=brick.coords[1]<=y1+40:
                
                brick.damage()
                print("touché brique " + brick.couleur + ", hp restants: " + str(brick.hp) + ", score+" + str(brick.scorevalue))
                dx1=-dx1
                dy1=-dy1
                can1.delete(txtscore)
                txtscore = can1.create_text(550, 450, anchor =E, text ="Score: " + str(score),fill ="black", font="Arial 10 bold")






    fen.after(15, les_briques_qui_se_cassent_lol)

def bouge_balle():

    global x1, y1, dx1, dy1, drapeau
    x1=x1 + dx1
    y1=y1 + dy1

    if x1 >570:
        x1=570
        dx1=-dx1
        dy1=dy1
        PlaySound(breakSound, SND_ASYNC)

    if y1 <5:
        y1=5
        dy1=-dy1
        PlaySound(breakSound, SND_ASYNC)

    if x1 <5:
        x1=5
        dx1=-dx1
        dy1=dy1
        PlaySound(breakSound, SND_ASYNC)

    if y1 >450:
        if x1>xb-cc:
            if x1<xb+cc:
                direction(x1-xb)
                print("debug")
                PlaySound(breakSound, SND_ASYNC)

            else :
                game_over()
        else :
            game_over()
    can1.coords(balle1,x1,y1,x1+20,y1+20)

    if listeBriques == []:
        win()

    if drapeau==1:
        fen.after(15,bouge_balle)


def bord_barre():
    global xb,cc
    if xb-cc< 0:
        barre= can1.create_rectangle(xb-cc,470,xb+cc,480,width=0,fill="white")
        xb=cc
        barre= can1.create_rectangle(xb-cc,470,xb+cc,480,width=0,fill="black")

    if xb+cc>600:
        barre= can1.create_rectangle(xb-cc,470,xb+cc,480,width=0,fill="white")
        xb=600-cc
        barre= can1.create_rectangle(xb-cc,470,xb+cc,480,width=0,fill="black")

    fen.after(15, bord_barre)

def barre_gauche():
    global xb,dxb
    barre= can1.create_rectangle(xb-cc,470,xb+cc,480,width=0,fill="white")
    xb=xb-dxb
    barre= can1.create_rectangle(xb-cc,470,xb+cc,480,width=0,fill="black")
    if gauche<0:
        fen.after(15, barre_gauche)

def barre_droite():
    global xb,dxb
    barre= can1.create_rectangle(xb-cc,470,xb+cc,480,width=0,fill="white")
    xb=xb+dxb
    barre= can1.create_rectangle(xb-cc,470,xb+cc,480,width=0,fill="black")
    if droite<0:
        fen.after(15, barre_droite)

def start_gauche(event=None):
    gauche=1
    barre_gauche()

def start_droite(event=None):
    droite=1
    barre_droite()

def stop_gauche(event=None):
    gauche=0

def stop_droite(event=None):
    droite=0

def start(event=None):
    global drapeau
    if drapeau==0:
        drapeau=1
        bouge_balle()

def game_over():
    global drapeau
    drapeau=0
    can1.create_text(canX/2, 200, anchor =CENTER, text ="GAME OVER",fill ="black", font="Arial 50 bold")
    PlaySound(overSound, SND_ASYNC)


def win():
    global drapeau
    drapeau = 0
    can1.create_text(canX/2, 200, anchor =CENTER, text ="SI SI OUAIS OUAIS",fill ="black", font="Arial 50 bold")

fen = Tk()
fen.title("casse-brique")

can1 = Canvas(fen,bg='white',height=500, width=600)
can1.pack(side=LEFT, padx =5, pady =5)

balle1 = can1.create_oval(x1, y1, x1+20, y1+20, width=1, fill='grey')
barre= can1.create_rectangle(xb-cc,470,xb+cc,480,width=0,fill="black")

fen.bind("<KeyPress-Left>",start_gauche)
fen.bind("<KeyPress-Right>",start_droite)
fen.bind("<KeyRelease-Left>",stop_gauche)
fen.bind("<KeyRelease-Right>",stop_droite)
fen.bind("<space>",start)





couleursPossibles = ["red", "blue", "blue", "blue", "blue", "red", "green"]

for i in range(10):
    for j in range(10):
        rand = random.randint(1,100)
        if rand < 8:
            Brique(i*30+10, "gold2")
        else:
            Brique(i*30+10, random.choice(couleursPossibles))
    banane = 0


bouge_balle()
bord_barre()
les_briques_qui_se_cassent_lol()
print(listeBriques)



txtscore = can1.create_text(550, 450, anchor =E, text ="Score: "+str(score),fill ="black", font="Arial 10 bold")

fen.mainloop()
