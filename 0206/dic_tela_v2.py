from tkinter import *

def adiciona():
    entrada = input.get()
    list.insert(END, entrada)
    input.delete(0, 'end')

# Criamos a janela e adicionamos titulo e tamanho
janela = Tk()
janela.title("Adicionador de nomes")
janela.geometry("500x200")

#Vamos criar 2 frames lado a lado
esquerdo = Frame(janela)
esquerdo.pack(side="left", padx=5, pady=5)

direito = Frame(janela)
direito.pack(side="right", padx=5, pady=5)

#Adicionamos campos no frame esquerdo
lbl = Label(esquerdo, text="Digite o nome: ") #Label
lbl.pack(padx=5, pady=5)
input = Entry(esquerdo, width=30) #Input
input.pack(padx=5, pady=5)
bt = Button(esquerdo, command=adiciona, text="Adicionar") #Button
bt.pack(padx=5, pady=5)

#Adicionamos uma lista do lado direito
list = Listbox(direito)
list.pack(padx=5, pady=5)

#criamos o looping de eventos
janela.mainloop()