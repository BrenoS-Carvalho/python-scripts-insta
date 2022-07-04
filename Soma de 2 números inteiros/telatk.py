from cProfile import label
import tkinter as tk
janela = tk.Tk()
janela.title('Calculadora de 2 números inteiros')
titulo = tk.Label(text='Calculadora')
titulo.pack()

valor = tk.Entry()
valor.pack()

janela.mainloop()