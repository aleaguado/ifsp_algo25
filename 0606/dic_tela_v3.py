from tkinter import *
from tkinter import messagebox

def alimenta():
    entrada = input.get()
    lista_n = lista.get(0, "end")
    if (entrada in lista_n) and (op.get() == 1):
        indice = lista_n.index(entrada)
        lista.delete(indice)
    elif (op.get() == 0):
        lista.insert(END, entrada)
    else:
        messagebox.showerror("Mensagem", "Item Inexistente!")
        
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
op = IntVar()
lbl = Label(esquerdo, text="Digite o nome: ") #Label
lbl.pack(padx=5, pady=5)
input = Entry(esquerdo, width=30) #Input
op_add = Radiobutton(esquerdo, text="Adicionar", variable=op, value=0)
op_add.pack(padx=5, pady=5)
op_del = Radiobutton(esquerdo, text="Remover", variable=op, value=1)
op_del.pack(padx=5, pady=5)
input.pack(padx=5, pady=5)
bt = Button(esquerdo, command=alimenta, text="Executar") #Button
bt.pack(padx=5, pady=5)

#Adicionamos uma lista do lado direito
lista = Listbox(direito)
lista.pack(padx=5, pady=5)

#criamos o looping de eventos
janela.mainloop()