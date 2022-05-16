from turtle import bgcolor, color
import pandas as pd
from tkinter import *
from openpyxl import Workbook
from pkg_resources import WorkingSet

def funcao():
    a = 1
    b = 1
    
    print(a + b)
    
def deletar_linha():
    excel = pd.read_excel("planilha_teste.xlsx")
    excel = excel.drop(index=0)

def interface():
        
    window = Tk()

    #Config da Janela
    window.title("Somativa de Python")
    window.geometry("800x600")
    window.resizable(0, 0)
    window["bg"] = "pink"
    # window.iconbitmap(default="Logo Senai para Trabalho.ico")
    
    #Config de Texto
    label1 = Label(window, 
                   text="Manipulador de Planilhas",
                   font="Arial 30",
                   fg="purple",
                   bd=1,
                   bg="pink")
    label1.pack()
    
    label2 = Label(window, 
                   text="Menu\n",
                   font="Arial 20 bold",
                   fg="purple",
                   bg="pink")
    label2.pack()

    label3 = Label(window, 
                   text="ID:",
                   font="Arial 16 bold",
                   fg="black",
                   bg="pink")
    label3.place(x=55, y=115)
    
    label4 = Label(window, 
                   text="Nome:",
                   font="Arial 16 bold",
                   fg="black",
                   bg="pink")
    label4.place(x=55, y=215)
    
    label5 = Label(window, 
                   text="Idade:",
                   font="Arial 16 bold",
                   fg="black",
                   bg="pink")
    label5.place(x=55, y=315)
    
    label6 = Label(window, 
                   text="Peso:",
                   font="Arial 16 bold",
                   fg="black",
                   bg="pink")
    label6.place(x=55, y=415)
    
    #Config do Botão
    
    botao = Button(window, 
                   text="Criar",
                   font="Arial 16 bold", command=funcao)
    botao.place(x=60, y=530)
    
    botao2 = Button(window, 
                   text="Ler",
                   font="Arial 16 bold")
    botao2.place(x=190, y=530)
    
    botao3 = Button(window, 
                   text="Atualizar",
                   font="Arial 16 bold")
    botao3.place(x=300, y=530)
    
    botao4 = Button(window, 
                   text="Deletar",
                   font="Arial 16 bold", command=deletar_linha)
    botao4.place(x=440, y=530)
    
    #Config das Imagens
    
    img = PhotoImage(file="C:/Users/USER/Desktop/PROGRAMAÇÃO/PROGRAMAÇÕES/PYTHON/Projeto Python Senai (Planilha)/Manipulador de Planilhas Interface/Logo Senai para Trabalho.png",)
    logo = Label(window, image=img, bg="pink")
    # logo.pack()
    logo.place(x=10,y=10)
    
    #Config do Menu
    meuMenu = Menu(window,bg="pink")
    
    meuMenu.add_command(label="Opção")
    meuMenu.add_command(label="Opção")
    meuMenu.add_command(label="Opção")
    meuMenu.add_command(label="Opção")
    
    window.config(menu = meuMenu)
    
    #Config das caixas de texto
    texto = Entry(window, font=("Arial", 14), bd=2, width=45, justify="left")
    texto.place(x=55, y=150)
    
    texto = Entry(window, font=("Arial", 14), bd=2, width=45, justify="left")
    texto.place(x=55, y=250)
    
    texto = Entry(window, font=("Arial", 14), bd=2, width=45, justify="left")
    texto.place(x=55, y=350)
    
    texto = Entry(window, font=("Arial", 14), bd=2, width=45, justify="left")
    texto.place(x=55, y=450)
    # texto.pack()
    
    window.mainloop()
    
interface()
