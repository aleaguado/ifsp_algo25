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

# Através do método pack() anexamos os componentes na tela!
rotulo_instrucao.pack(pady=10) #anexamos o rótulo com margem de 10
entrada_nome.pack(pady=5) #anexamos o campo de digitação com margem de 5
bt.pack(pady=10) #anexamos o botão com margem de 10
rotulo_resultado.pack(pady=10) #anexamos o último rótulo com margem de 10

# Iniciar o loop principal da interface
janela.mainloop() #Muito Importante! Cria o looping de eventos, que aguarda ação do 
#usuário nos botões! Sem ele, abriria e fecharia no mesmo momento!