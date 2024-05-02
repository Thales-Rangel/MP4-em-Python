#para o console
from tkinter import*
import customtkinter as janela
import tkinter.ttk as ttk
from tkinter import messagebox as tkMessageBox

#para as imagens
from PIL import Image, ImageTk

#para tocar musica
import pygame
from pygame import mixer_music, mixer

import os
import random

from mutagen.mp3 import MP3

import time

co0 = "#f0f3f5" # cinza
co1 = '#080808' # preto
co2 = '#fafafa' # branco
co3 = '#d43833' # vermelho
co4 = '#35c232' # verde 
co5 = '#3281c2' # azul
co6 = '#cfaf25' # amarelo
co7 = '#8b39ad' # roxo
co8 = '#ad3990' # rosa
co9 = '#ad7539' # laranja

# Tela/ Console

janela = janela.CTk()
janela.title('SPOTIFYCRACKEAD*')
janela.geometry('432x405')
janela.configure(background=co1)
janela.resizable(width=False,height=False)

# Setting icon of master window
janela.iconbitmap('logo.ico')

# inicializando
pygame.mixer.init()

# Frames/ Cubos

frame_esquerda = Frame(janela,width=120,height=180,bg=co1,borderwidth=0,highlightthickness=0)
frame_esquerda.grid(row=0,column=0,pady=1,padx=1,sticky=NSEW)

frame_direita = Frame(janela,width=370,height=280,bg=co1,borderwidth=0,highlightthickness=0)
frame_direita.grid(row=0,column=1,pady=1,padx=0,sticky=NSEW)

frame_baixo = Frame(janela,width=504,height=230,bg=co1,borderwidth=0,highlightthickness=0)
frame_baixo.grid(row=1,column=0,columnspan=3,pady=1,padx=0,sticky=NSEW)

# frame esquerdo  
img_1 = Image.open('spotify.png')
img_1 = img_1.resize((175,180))
img_1 = ImageTk.PhotoImage(img_1)

l_logo = Label(frame_esquerda, height=140,image=img_1,compound=LEFT,padx=10,anchor='nw',font='ivy 16 bold',bg=co1,fg=co1,borderwidth=0,highlightthickness=0)
l_logo.place(x=-8,y=12)

#

def play_musica():
    empty_tuple = ()
    if listbox.curselection() == empty_tuple:
        tkMessageBox.showinfo(message="Selecione uma música!")
    else:
        musica_posicao.set(1)
        mixer.music.set_volume(0.55)
                
        rodando = listbox.get(ACTIVE)
        l_tocando['text']=rodando
        mixer.music.load(rodando)
        mixer.music.play(loops=0)

        audio = MP3(rodando)
        tamanho = audio.info.length
        minutos = str(int(tamanho/60))
        segundos = str(int(tamanho%60))
        musica_tamanho.config(text=f'{minutos}:{segundos.rjust(2,"0")}')
            
        musica_posicao.config(to=tamanho)
            
        play_tocando()
    
def play_tocando():
    #tempo da musica enquanto esta tocando
    #tempo_musica_atual = 0
    #minutos = 0
    #segundos = 0
    
    """
    if not posicao_mudada:
        tempo_musica_atual = musica_posicao.get()
        minutos = str(int(tempo_musica_atual/60))
        segundos = str(int(tempo_musica_atual%60))
    else:
        tempo_musica_atual = pygame.mixer.music.get_pos()
        minutos = str(int((tempo_musica_atual/1000)/60))
        segundos = str(int((tempo_musica_atual/1000)%60))
    """
    
    tempo_musica_atual = pygame.mixer.music.get_pos()
    
    minutos = str(int((tempo_musica_atual/1000)/60))
    segundos = str(int((tempo_musica_atual/1000)%60))
    
    #tempo da musica selecionada (fixo)
    rodando = listbox.get(ACTIVE)
    audio = MP3(rodando)
    tamanho = audio.info.length
    min = str(int(tamanho/60))
    seg = str(int(tamanho%60))
    
    if tempo_musica_atual==tamanho:
        proxima_musica()
        
    musica_tocando.config(text=f'{minutos}:{segundos.rjust(2,"0")}')    
    musica_posicao.config(value= tempo_musica_atual/1000 )

    
    musica_tocando.after(1000,play_tocando)
    
    # reproduzir a próxima música quando a música atual terminar
    if not pygame.mixer.music.get_busy() and not musica_pausada:
        if not aleatorio_selecionado:
            proxima_musica()
        else: 
            musica_aleatoria()
    
                  
def mudar_posicao(x):
    global posicao_mudada
    rodando = listbox.get(ACTIVE)
    pygame.mixer.music.load(rodando)
    
    pygame.mixer.music.stop()
    
    pygame.mixer.music.play(loops=0, start=int(musica_posicao.get()))
    
    tempo_musica_mudanca = musica_posicao.get()
    
    minutos = str(int(tempo_musica_mudanca/60))
    segundos = str(int(tempo_musica_mudanca%60))

    musica_tocando.config(text=f'{minutos}:{segundos.rjust(2,"0")}')
    posicao_mudada = True
       
def pausar_musica():
    empty_tuple = ()
    if listbox.curselection() == empty_tuple:
        tkMessageBox.showinfo(message="Selecione uma música!")
    else:
        global musica_pausada
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            musica_pausada = True
        else:
            pygame.mixer.music.unpause()
            musica_pausada = False
    
def proxima_musica():  
    pygame.mixer_music.set_pos=0
    tocando = l_tocando['text']
    novo_index = musicas.index(tocando) + 1
    
    if novo_index >= len(musicas):
        novo_index = 0
        
    tocando = musicas[novo_index]
    
    pygame.mixer.music.load(tocando)
    pygame.mixer.music.play()
    
    listbox.delete(0,END)
    
    mostrar()
    
    listbox.select_set(novo_index)
    listbox.config(selectmode=SINGLE)
    
    l_tocando['text']=tocando
    
    # alterando tempo msc fixo
    audio = MP3(listbox.get(novo_index))
    tamanho = audio.info.length
    minutos = str(int(tamanho/60))
    segundos = str(int(tamanho%60))
    musica_tamanho.config(text=f'{minutos}:{segundos.rjust(2,"0")}')
   
    musica_posicao.config(to=tamanho)
    
    play_tocando()

def voltar_musica():
    pygame.mixer_music.set_pos=0
    tocando = l_tocando['text']
    novo_index = musicas.index(tocando) - 1
    
    if novo_index < 0:
        novo_index = 0
        
    tocando = musicas[novo_index]
    
    mixer.music.load(tocando)
    mixer.music.play()
    
    listbox.delete(0,END)
    
    mostrar()
    
    listbox.select_set(novo_index)
    listbox.config(selectmode=SINGLE)
    
    l_tocando['text']=tocando
    
    # alterando tempo msc fixo
    audio = MP3(listbox.get(novo_index))
    tamanho = audio.info.length
    minutos = str(int(tamanho/60))
    segundos = str(int(tamanho%60))
    musica_tamanho.config(text=f'{minutos}:{segundos.rjust(2,"0")}')
   
    musica_posicao.config(to=tamanho)
    
    play_tocando()
    
def musica_aleatoria():
    global aleatorio_selecionado
    pygame.mixer_music.set_pos=0
    novo_index = random.randrange(0,len(musicas))
    
    tocando = musicas[novo_index]
    
    mixer.music.load(tocando)
    mixer.music.play()
    
    listbox.delete(0,END)
    
    mostrar()
    
    listbox.select_set(novo_index)
    listbox.config(selectmode=SINGLE)
    
    l_tocando['text']=tocando
    
    # alterando tempo msc fixo
    audio = MP3(listbox.get(novo_index))
    tamanho = audio.info.length
    minutos = str(int(tamanho/60))
    segundos = str(int(tamanho%60))
    musica_tamanho.config(text=f'{minutos}:{segundos.rjust(2,"0")}')
   
    musica_posicao.config(to=tamanho)
    
    play_tocando()
    aleatorio_selecionado = True

def alterar_volume(x):
    mixer.music.set_volume(volume.get())
    

# frame direito

listbox = Listbox(frame_direita,width=43,height=13,selectmode=SINGLE,font=('calibri 9'),bg=co1,fg=co2,borderwidth=0,highlightthickness=0)
listbox.grid(row=0,column=0)

s =Scrollbar(frame_direita)
s.grid(row=0,column=1,sticky=NSEW)

listbox.config(yscrollcommand=s.set)
s.config(command=listbox.yview)

#frame baixo

l_tocando = Label(frame_baixo,text='Escolha música na lista',width=64,justify=LEFT,anchor='nw',font='calibri 10',bg=co2,fg=co1,borderwidth=0,highlightthickness=0)
l_tocando.place(x=0,y=1)

# mudar posicao/duracao musica

musica_tocando = Label(janela,text='0')
musica_tocando.place(x=38,y=255)

musica_tamanho = Label(janela, text="0")
musica_tamanho.place(x=258,y=255)

# musica posicao enquanto toca

musica_posicao = ttk.Scale(janela, from_=0, to=100, orient=HORIZONTAL, value=0, command=mudar_posicao, length=247)
musica_posicao.grid(row=2, column=0, pady=10)
musica_posicao.place(x=38,y=275)

# label_volume

volume_frame = LabelFrame(janela, text="Volume",font='calibri 9',background=co1,foreground=co2,borderwidth=0,highlightthickness=0)
volume_frame.grid(row=0, column=1, padx=30)
volume_frame.place(x=338,y=230)

# botao volume

volume = ttk.Scale(volume_frame, orient=VERTICAL,from_=0, to=1,value=1,command=alterar_volume,length=105)
volume.pack(pady=10)    
# 

img_voltarmusica = Image.open('voltarmusica.png')
img_voltarmusica = img_voltarmusica.resize((30,30))
img_voltarmusica = ImageTk.PhotoImage(img_voltarmusica)

# botao voltar musica

b_anterior = Button(frame_baixo,command=voltar_musica,width=40,height=40,image=img_voltarmusica,font='ivy 10 bold',relief=RAISED,overrelief=RIDGE,bg=co1,fg=co1,borderwidth=0,highlightthickness=0)
b_anterior.place(x=38,y=108)

# botao tocar musica

img_tocar = Image.open('tocar.png')
img_tocar = img_tocar.resize((30,40))
img_tocar = ImageTk.PhotoImage(img_tocar)

b_play = Button(frame_baixo,command=play_musica,width=40,height=40,image=img_tocar,font='ivy 10 bold',relief=RAISED,overrelief=RIDGE,bg=co1,fg=co1,borderwidth=0,highlightthickness=0)
b_play.place(x=84,y=108)

# botao avançar musica

img_avancarmusica = Image.open('avancarmusica.png')
img_avancarmusica = img_avancarmusica.resize((30,30))
img_avancarmusica = ImageTk.PhotoImage(img_avancarmusica)

b_proxima = Button(frame_baixo,command=proxima_musica,width=40,height=40,image=img_avancarmusica,font='ivy 10 bold',relief=RAISED,overrelief=RIDGE,bg=co1,fg=co1,borderwidth=0,highlightthickness=0)
b_proxima.place(x=130,y=108)

# botao pausar

img_pausa = Image.open('pausa.png')
img_pausa = img_pausa.resize((30,30))
img_pausa = ImageTk.PhotoImage(img_pausa)

b_pausa = Button(frame_baixo,command=pausar_musica,width=40,height=40,image=img_pausa,font='ivy 10 bold',relief=RAISED,overrelief=RIDGE,bg=co1,fg=co1,borderwidth=0,highlightthickness=0)
b_pausa.place(x=176,y=108)

# botao aleatorio

img_aleatorio = Image.open('aleatorio.png')
img_aleatorio = img_aleatorio.resize((30,30))
img_aleatorio = ImageTk.PhotoImage(img_aleatorio)

b_aleatorio = Button(frame_baixo,command=musica_aleatoria,width=40,height=40,image=img_aleatorio,font='ivy 10 bold',relief=RAISED,overrelief=RIDGE,bg=co1,fg=co1,borderwidth=0,highlightthickness=0)
b_aleatorio.place(x=242,y=108)

os.chdir(r'C:\Users\pedrolmbs\spotifycrackeado\musicas')
musicas = os.listdir()
        
def mostrar():
    for i in musicas:
        listbox.insert(END,i)

mostrar()
musica_pausada = False
posicao_mudada = False
aleatorio_selecionado = False
janela.mainloop()