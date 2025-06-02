import tkinter as tk

janela = tk.Tk()

# Widgets
label1 = tk.Label(janela, text="Nome:", bg="lightblue")
label2 = tk.Label(janela, text="E-mail:", bg="lightgreen")
entrada1 = tk.Entry(janela)
entrada2 = tk.Entry(janela)
botao = tk.Button(janela, text="Enviar")

# Layout com grid
label1.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entrada1.grid(row=0, column=1, padx=5, pady=5)
label2.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entrada2.grid(row=1, column=1, padx=5, pady=5)
botao.grid(row=2, column=0, columnspan=2, pady=10)  # Ocupa 2 colunas

janela.mainloop()