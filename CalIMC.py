## Calculadora de imc com tkinter

## Bibliotecas
import tkinter
import customtkinter
from tkinter import *
from customtkinter import *



## Janela
window1 = Tk()
window1.title("IMC")
window1.configure(background="Gray")
window1.geometry("400x400")


## Function
def cal1():
    p = float(peso.get())
    a = int(altu.get())
    a = a/100
    imc = p/(a**2)
    if imc < 16.9:
        resultxt1.set_text(f"{imc:.2f}\n Muito abaixo do peso")
    elif 17 >= imc <= 18.4:
        resultxt1.set_text(f"{imc:.2f}\n Abaixo do peso")
    elif 18.5 >= imc <= 24.9:
        resultxt1.set_text(f"{imc:.2f}\n Peso normal")
    elif 25 >= imc < 30:
        resultxt1.set_text(f"{imc:.2f}\n Acima do peso")
    elif 30 >= imc < 40:
        resultxt1.set_text(f"{imc:.2f}\n Obeso")
    else:
        resultxt1.set_text(f"{imc:.2f}\n Muito Obeso")


## Layout
null1 = Label(window1,text=" ",bg="Gray",width=28)
null1.grid(column=1,row=0)

balanca = PhotoImage(file="imagens\oois2.png")
balanca = balanca.subsample(4,4)
imagem = Label(window1,image=balanca,height=125,width=125,bg="Gray")
imagem.grid(column=2,row=1)

peos = CTkLabel(master=window1,
                text="Insira seu peso em kg",
                text_color="Black",
                width=175,
                text_font=("Franklin Gothic Demi",10))
peos.grid(column=2,row=2)
peso = CTkEntry(master=window1,
                text_color="Black",
                corner_radius=100,
                height=65,
                width=175,
                fg_color="White",
                font=("Franklin Gothic Demi",25))
peso.grid(column=2,row=3)



alut = CTkLabel(master=window1,
                text="Insira sua altura em cm",
                text_color="Black",
                width=175,
                text_font=("Franklin Gothic Demi",10))
alut.grid(column=2,row=4)
altu = CTkEntry(master=window1,
                text_color="Black",
                corner_radius=100,
                height=65,
                width=175,
                fg_color="White",
                font=("Franklin Gothic Demi",25))
altu.grid(column=2,row=5)


cal = CTkButton(master= window1,
                text="Calcular o IMC",
                text_color="Black",
                text_font=("Franklin Gothic Demi",15),
                fg_color="White",
                width=140,
                height=55,
                command=cal1)
cal.grid(column=1,row=3)

resultxt = CTkLabel(master=window1,
                    text="Resultado: ",
                    text_color="Black",
                    text_font=("Franklin Gothic Demi",15))
resultxt.grid(column=1,row=4)

resultxt1 = CTkLabel(master=window1,
                     text="                     ",
                     text_color="Black",
                     text_font=("Franklin Gothic Demi",10),
                     width=125,
                     height=65)
resultxt1.grid(column=1,row=5)

## Looooop Janela
window1.mainloop()