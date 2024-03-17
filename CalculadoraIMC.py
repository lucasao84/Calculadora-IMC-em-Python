from tkinter import * 
from tkinter import ttk
import tkinter as tk

# cores

cor0 = 'white'
cor1 = '#38989B' # ezul claro
cor2 = '#225F61' # azul escuro

# configurando a janela

janela = Tk()
janela.title('')
janela.geometry('295x230')
janela.configure(bg='white')

def calcular():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc = peso / (altura ** 2) 
        caixa['text'] = "{:.2f}".format(imc)
    except ValueError:
        # Tratamento de erro se os valores inseridos não forem números válidos
        caixa['text'] = "Por favor, insira valores numéricos para peso e altura"
    except ZeroDivisionError:
        # Tratamento de erro se a altura for zero
        caixa['text'] = "A altura não pode ser zero"
    
    # Converta o texto de caixa para um número antes de comparar
    imc = float(caixa['text'])

    if imc <= 18.5:
        imc1 = 'Abaixo do peso'
    elif 18.5 < imc <= 24.9:
        imc1 = 'Peso normal'
    elif 25.0 <= imc <= 29.9:
        imc1 = 'Sobrepeso'
    else:
        imc1 = 'Obeso'

    label_obesidade['text'] = imc1



# dividindo a janela em dois

#frame cima

frame_cima = Frame(janela, width=295, height=60, bg=cor0)
frame_cima.place(x=0, y=0)

# frame baixo

frame_baixo = Frame(janela, width=295, height=230 , bg=cor0)
frame_baixo.place(x=0, y=60)

# linha

linha_label = Label(frame_cima, width=295, height=3,bg=cor2)
linha_label.place(x=0, y=50)

# label titulo

titulo_label = Label(frame_cima, width=25, text='Calculadora de IMC', anchor='center', font=('Ivy 15 bold'), fg=cor2, bg=cor0)
titulo_label.place(x=0, y=25)

# config label e entry peso

label_peso = Label(frame_baixo, width=13, text='Insirir seu peso', font=('Ivy 11 bold'), fg=cor2, bg=cor0, anchor='w', )
label_peso.grid(row=0, column=0, stick=NSEW, padx=5, pady=15)

entry_peso = Entry(frame_baixo, width=6, relief=SOLID, font=("Arial 10 bold"))
entry_peso.grid(row=0, column=1, stick=NSEW, padx=5, pady=15)

# config label e entry altura

label_altura = Label(frame_baixo, width=13, text='Insirir sua altura', font=('Ivy 11 bold'), fg=cor2, bg=cor0, anchor='w', )
label_altura.grid(row=1, column=0, stick=NSEW, padx=5, pady=0)

entry_altura = Entry(frame_baixo, width=6 ,relief=SOLID, font=("Arial 10 bold"))
entry_altura.grid(row=1, column=1, stick=NSEW, padx=5, pady=0)


caixa = Label(janela, text='587', width=6, height=1, bg=cor1, anchor='center',relief='groove' ,font=('Ivy 15 bold'), padx=6, pady=18)
caixa.place(x=195, y=75)

label_obesidade = Label(janela, width=13, text='Seu IMC é:', font=('Ivy 11 bold'), fg=cor2, bg=cor0, anchor='w', )
label_obesidade.place(x=60, y=150)

label_obesidade = Label(janela, width=13, text='Obesidade', font=('Ivy 11 bold'), fg=cor2, bg=cor0, anchor='w', )
label_obesidade.place(x=140, y=150)

# config botão 

botao = Button(janela, width=33 , text='Calcular', height=1, font=("Ivy 10 bold"),relief='raised', anchor='center', bg=cor2, fg=cor0, command=calcular)
botao.place(x=10 , y=190)

janela.mainloop()