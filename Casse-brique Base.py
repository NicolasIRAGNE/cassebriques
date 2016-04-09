# Créé par Geoffroy, le 24/12/2015 en Python 3.2
from tkinter import *
from math import sqrt
import random
from winsound import *
x1 ,y1=150,200
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
damage = 1
fire = 0 #
bigbonus = 0
perdu = 0

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
        if self.couleur == "b":
            self.couleur = "blue"
            self.hp = 1
        elif self.couleur == "r":
            self.hp = 2
            self.couleur = "red"
        elif self.couleur == "g":
            self.hp = 3
            self.couleur = "green"
        elif self.couleur == "2":
            self.hp = 10
            self.scorevalue = 5
            self.couleur = "gold2"
        elif self.couleur == "f":
            self.hp = 1
            self.couleur = "gray"
        self.generer(height)
    def damage(self):
        global score, damage 
        self.hp -= damage
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
            elif self.couleur == "gray":
                self.scorevalue = 15
                bonus_fire(2000)
            score += self.scorevalue
            can1.delete(self.brick)
            listeBriques.remove(self)
            PlaySound(hitSound, SND_ASYNC)
        else:
            PlaySound(breakSound, SND_ASYNC)





def fire_off():
    global damage,fire 
    can1.itemconfig(balle1, fill = "grey")
    damage = 1
    fire = 0


def bonus_fire(duration):
    global damage, fire, dx1, dy1
    can1.itemconfig(balle1, fill = "red")
    damage = 2
    fire = 1
    fen.after(duration, fire_off)

def retablir_taille():
    global bigbonus, xb, cc
    bigbonus = 0
    cc = 80
    barre= can1.create_rectangle(0,470,xb,480,width=0,fill="white")
    barre= can1.create_rectangle(xb+cc,470,600,480,width=0,fill="white")
    barre= can1.create_rectangle(xb-cc,470,xb+cc,480,width=0,fill="black")


def bonus_big(duration):
    global bigbonus
    bigbonus = 1
    barre= can1.create_rectangle(xb-cc-40,470,xb+cc+40,480,width=0,fill="black")
    fen.after(duration, retablir_taille)

def direction(x):
    global dx1, dy1
    dx1=x/10
    dy1=-5

def les_briques_qui_se_cassent_lol():
    for brick in listeBriques:
        global x1, y1,dx1, dy1, txtscore, fire
        if x1-20<=brick.coords[0]<=x1+40:
            if y1-20<=brick.coords[1]<=y1+40:
                
                brick.damage()
                print("touché brique " + brick.couleur + ", hp restants: " + str(brick.hp) + ", score+" + str(brick.scorevalue))
                if fire == 0:
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
                PlaySound(breakSound, SND_ASYNC)

            else :
                game_over()
        else :
            game_over()
    can1.coords(balle1,x1,y1,x1+20,y1+20)

    if listeBriques == []:
        win()

    if drapeau==1 and perdu != 1:
        fen.after(15,bouge_balle)


def bord_barre():
    global xb,cc, bigbonus
    if bigbonus == 1:
        cc = 120
    else:
        cc = 80
    if xb-cc< 0:
        barre= can1.create_rectangle(xb-cc,470,xb+cc,480,width=0,fill="white")
        xb=cc
        barre= can1.create_rectangle(xb-cc,470,xb+cc,480,width=0,fill="black")
        barre= can1.create_rectangle(0,470,xb,480,width=0,fill="white")
        barre= can1.create_rectangle(xb+cc-40,470,600,480,width=0,fill="white")
        barre= can1.create_rectangle(xb-cc,470,xb+cc,480,width=0,fill="black")

    if xb+cc>600:
        barre= can1.create_rectangle(xb-cc,470,xb+cc,480,width=0,fill="white")
        xb=600-cc
        barre= can1.create_rectangle(xb-cc,470,xb+cc,480,width=0,fill="black")
        barre= can1.create_rectangle(0,470,xb,480,width=0,fill="white")
        barre= can1.create_rectangle(xb+cc-40,470,600,480,width=0,fill="white")
        barre= can1.create_rectangle(xb-cc,470,xb+cc,480,width=0,fill="black")
    if bigbonus == 1:
        cc = 120
    else:
        cc = 80
    fen.after(15, bord_barre)

def barre_gauche():
    global xb,dxb, bigbonus
    if bigbonus == 1:
        cc = 120
    else:
        cc = 80
    barre= can1.create_rectangle(xb-cc,470,xb+cc,480,width=0,fill="white")
    xb=xb-dxb
    barre= can1.create_rectangle(xb-cc,470,xb+cc,480,width=0,fill="black")
    barre= can1.create_rectangle(0,470,xb,480,width=0,fill="white")
    barre= can1.create_rectangle(xb+cc-40,470,600,480,width=0,fill="white")
    barre= can1.create_rectangle(xb-cc,470,xb+cc,480,width=0,fill="black")
    if bigbonus == 1:
        cc = 120
    else:
        cc = 80
    if gauche<0:
        fen.after(15, barre_gauche)

def barre_droite():
    global xb,dxb, bigbonus
    if bigbonus == 1:
        cc = 120
    else:
        cc = 80
    barre= can1.create_rectangle(xb-cc,470,xb+cc,480,width=0,fill="white")
    xb=xb+dxb
    barre= can1.create_rectangle(xb-cc,470,xb+cc,480,width=0,fill="black")
    barre= can1.create_rectangle(0,470,xb,480,width=0,fill="white")
    barre= can1.create_rectangle(xb+cc-40,470,600,480,width=0,fill="white")
    barre= can1.create_rectangle(xb-cc,470,xb+cc,480,width=0,fill="black")
    if bigbonus == 1:
        cc = 120
    else:
        cc = 80
    if droite<0:
        fen.after(15, barre_droite)

def start_gauche(event=None):
    gauche=1
    if perdu == 0:

        barre_gauche()

def start_droite(event=None):
    droite=1
    if perdu == 0:
        barre_droite()


def stop_gauche(event=None):
    gauche=0

def stop_droite(event=None):
    droite=0

def start(event=None):
    global drapeau, perdu
    if drapeau==0 and perdu == 0:
        drapeau=1
        bouge_balle()

def game_over():
    global drapeau, perdu
    perdu = 1
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



txtscore = can1.create_text(550, 450, anchor =E, text ="Score: " + str(score),fill ="black", font="Arial 10 bold")

couleursPossibles = ["red", "blue", "blue", "blue", "blue", "red", "green", "blue", "blue"]

niveau1 = [
"b0bbbbbb0b", 
"bbb0bb0bbb", 
"b0bbbbbb0b", 
"bbb0bb0bbb"
]

"""
for i in range(4):
    for j in range(10):
        rand = random.randint(1,100)
        if rand < 2:
            Brique(i*30+10, "gold2")
        elif 2 < rand < 5:
            Brique(i*30+10, "gray")
        else:
            Brique(i*30+10, random.choice(couleursPossibles))
    banane = 0
"""
booyah = 0
for string in niveau1:
    booyah += 1 
    for letter in string:
        if letter == "0":
            banane +=1
        elif letter == "x":
            Brique(booyah*30+10, random.choice(couleursPossibles))
        else:
            Brique(booyah*30+10, letter)
    banane = 0 #



bouge_balle()
bord_barre()
les_briques_qui_se_cassent_lol()
print(listeBriques)



fen.mainloop()
