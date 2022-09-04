from tkinter import * #Importar biblioteca tkinter

#Definicoes de cores baseadas no color picker
cor1 = '#09090a' #preto

janela  = Tk() #funcoes janela tkinter

janela.title('Voltando aos estudos') #titulo da janela
janela.geometry('400x350') #tamanho da janela
janela.resizable(width=False,height=False) #Bloqueio de janela redimensionavel
janela.config(bg = cor1) #cor de fundo, bg = background

janela.iconphoto(False,PhotoImage(file='logo.png')) #Trocar icone da janela
janela.mainloop() #"travar" a execu��o da janela atual usando um event loop