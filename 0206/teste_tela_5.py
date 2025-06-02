import tkinter as tk

def mudar_cor():
    # Alterna entre duas cores
    if frame_direito.cget("bg") == "lightblue":
        frame_direito.config(bg="lightgreen")
        botao.config(text="Azul")
    else:
        frame_direito.config(bg="lightblue")
        botao.config(text="Verde")

# Cria janela principal
janela = tk.Tk()
janela.title("Dois Frames com Pack")
janela.geometry("300x200")

# Frame esquerdo (contendo o botão)
frame_esquerdo = tk.Frame(janela, bg="#f0f0f0", width=100)
frame_esquerdo.pack(side="left", fill="both", expand=False)

# Frame direito (área que muda de cor)
frame_direito = tk.Frame(janela, bg="lightblue", width=200)
frame_direito.pack(side="right", fill="both", expand=True)

# Botão que faz a ação
botao = tk.Button(
    frame_esquerdo, 
    text="Verde", 
    command=mudar_cor,
    bg="white",
    width=10
)
botao.pack(pady=50, padx=20)

# Label no frame direito
label = tk.Label(
    frame_direito, 
    text="Clique no botão!", 
    bg="lightblue",
    font=("Arial", 12)
)
label.pack(pady=70)

janela.mainloop()