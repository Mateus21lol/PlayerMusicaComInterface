

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 22:56:57 2020

@author: Mateus Nobre Silva Almeida
"""


import numpy as np
from tkinter import *
import tkinter
from functools import partial
from PIL import ImageTk,Image
import pygame
import time

print("(☞ﾟヮﾟ)☞")


# Funções
def bt_click(botao):
    pygame.init()
    if(botao == bt1):
        print("Playing Unknown Brain - Superhero")
        pygame.mixer.music.load("Musicas/UnknownBrainSuperhero.mp3")
        pygame.mixer.music.play()
    if(botao == bt2):
        print("Playing OK KID Am Ende")
        pygame.mixer.music.load("Musicas/AmEnde.mp3")
        pygame.mixer.music.play()
    if(botao == bt3):
        print("Playing Grimes Oblivion")
        pygame.mixer.music.load("Musicas/GrimesOblivion.mp3")
        pygame.mixer.music.play()
    if(botao == bt4):
        print("Playing Lolo Zouaï - Moi")
        pygame.mixer.music.load("Musicas/LoloZouaiMoi.mp3")
        pygame.mixer.music.play()
    if(botao == bt5):
        print("Playing I Follow Rivers - Lykke Li")
        pygame.mixer.music.load("Musicas/IFollowRiversLykkeLiLaViedAdele.mp3")
        pygame.mixer.music.play()
    if(botao == bt6):
        print("Playing Tove Lo - Habits (Stay High)")
        pygame.mixer.music.load("Musicas/ToveLoHabitsStayHigh.mp3")
        pygame.mixer.music.play()
    if(botao == bt8):
        print("Playing Lolo Zouaï - Brooklyn Love")
        pygame.mixer.music.load("Musicas/LoloZouaiBrooklynLove.mp3")
        pygame.mixer.music.play()


def comandos(botao):
    control = botao
    if control == "pause":
        print("Pausado")
        pygame.mixer.music.pause()
    elif control == "play":
        print("Tocando")
        pygame.mixer.music.unpause()



# main do programa
janela = tkinter.Tk()
janela.title("Janela Principal")
lb = Label(janela, text=" (☞ﾟヮﾟ)☞  Ç'est un test  ☜(ﾟヮﾟ☜) ")
lb.place(x=100, y=60)

#botões inicio
bt1 = Button(janela, width=20, text="Unknown Brain - Superhero")
bt1["command"] = partial(bt_click, bt1)
bt1.place(x=100, y=101)

bt2 = Button(janela, width=20, text="OK KID Am Ende")
bt2["command"] = partial(bt_click, bt2)
bt2.place(x=100, y=130)

bt3 = Button(janela, width=20, text="Grimes Oblivion")
bt3["command"] = partial(bt_click, bt3)
bt3.place(x=100, y=160)

bt4 = Button(janela, width=20, text="Lolo Zouaï - Moi")
bt4["command"] = partial(bt_click, bt4)
bt4.place(x=100, y=190)

bt5 = Button(janela, width=20, text="I Follow Rivers - Lykke Li")
bt5["command"] = partial(bt_click, bt5)
bt5.place(x=100, y=220)

bt6 = Button(janela, width=20, text="Tove Lo - Habits (Stay High)")
bt6["command"] = partial(bt_click, bt6)
bt6.place(x=100, y=250)

bt7 = Button(janela, width=20, text="Lolo Zouaï - For the Crowd")
bt7["command"] = partial(bt_click, bt7)
bt7.place(x=100, y=280)

bt8 = Button(janela, width=20, text="Lolo Zouaï - Brooklyn Love")
bt8["command"] = partial(bt_click, bt8)
bt8.place(x=100, y=280)

bt9 = Button(janela, width=20, text="PAUSE")
bt9["command"] = partial(comandos, "pause")
bt9.place(x=300, y=101)

bt10 = Button(janela, width=20, text="PLAY")
bt10["command"] = partial(comandos, "play")
bt10.place(x=300, y=130)
#botões fim





#padrão é pixels
#LarguraxAltura+Estancia+Topo
#300x300+100+100
janela["background"] = "gray"
janela.geometry("800x600+100+100")

janela.mainloop()
