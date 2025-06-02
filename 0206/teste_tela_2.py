#Aqui importamos a biblioteca tkinter com o nome tk
import tkinter as tk
#Para facilitar a chamada importamos messagebox da própria tkinter
from tkinter import messagebox

#função que será executada ao clicarmos no botão
def cumprimentar():
    nome = entrada_nome.get()
    if nome:
        mensagem = f"Olá, {nome}! Bem-vindo(a) à minha primeira interface!"
        rotulo_resultado.config(text=mensagem)
        messagebox.showinfo("Saudação", mensagem)
    else:
        messagebox.showerror("Erro", "Por favor, digite seu nome!")

#execução começa aqui!
# Criar a janela principal
janela = tk.Tk() #método que cria a janela
janela.title("Minha primeira interface!") #método que anexa um título a janela
janela.geometry("400x200") #método que especifica tamanho da janela

# Aqui criamos os componentes que queremos colocar na tela!
rotulo_instrucao = tk.Label(janela, text="Digite seu nome:", font=("Arial", 12))
entrada_nome = tk.Entry(janela, width=30, font=("Arial", 12))
bt = tk.Button(janela, text="Rodar!", command=cumprimentar, bg="lightblue", font=("Arial", 10))
rotulo_resultado = tk.Label(janela, text="", font=("Arial", 12))

# Através do método place() anexamos os componentes na tela por coordenadas
rotulo_instrucao.place(x=50, y=50) #anexamos o rótul
entrada_nome.place(x=50, y=100) #anexamos o campo de digitação
bt.place(x=50, y=150) #anexamos o botão
rotulo_resultado.place(x=50, y=200) #anexamos o último rótulo

# Iniciar o loop principal da interface
janela.mainloop() #Muito Importante! Cria o looping de eventos, que aguarda ação do 
#usuário nos botões! Sem ele, abriria e fecharia no mesmo momento!