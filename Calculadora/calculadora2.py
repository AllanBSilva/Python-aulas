import tkinter as tk
import sqlite3

def press_btn(value):
    entry.insert(tk.END, value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)

        # Salvar o cálculo no banco de dados
        conn = sqlite3.connect('calculadora.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO calculos (expressao, resultado) VALUES (?, ?)", (expression, result))
        conn.commit()
        conn.close()
    except Exception as e:
        clear_entry()
        entry.insert(tk.END, "Erro")

# Criar o banco de dados SQLite e a tabela
conn = sqlite3.connect('calculadora.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS calculos (
                    id INTEGER PRIMARY KEY,
                    expressao TEXT,
                    resultado REAL
                )''')
conn.commit()
conn.close()

# Criando a janela
window = tk.Tk()
window.title("Calculadora")

# Criando a entrada
entry = tk.Entry(window, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Criando os botões
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_num = 1
col_num = 0

for btn_text in buttons:
    btn = tk.Button(window, text=btn_text, padx=10, pady=10, command=lambda btn_text=btn_text: press_btn(btn_text))
    btn.grid(row=row_num, column=col_num)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

# Botão de limpar
clear_btn = tk.Button(window, text='C', padx=10, pady=10, command=clear_entry)
clear_btn.grid(row=row_num, column=0, columnspan=2)

# Botão de calcular
equal_btn = tk.Button(window, text='=', padx=10, pady=10, command=calculate)
equal_btn.grid(row=row_num, column=2, columnspan=2)

# Rodando o loop principal
window.mainloop()
