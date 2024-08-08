import sqlite3
from tkinter import *
from math import sqrt

class Calculadora:
    def __init__(self, root):
        # Initialize tkinter window
        root.title('Calculadora')
        root.geometry("300x400")

        # Entrada de dados
        self.frame2 = Frame(root)
        self.frame2.pack()
        Label(self.frame2, text='Número1:', highlightthickness=10, height=2, bg="lightgrey", font=('Verdana', '12')).pack(side=LEFT)
        self.valor1 = Entry(self.frame2, width=5, font=('Verdana', '12'))
        self.valor1.pack(side=LEFT)

        self.frame3 = Frame(root)
        self.frame3.pack()
        Label(self.frame3, text='Número2:', highlightthickness=10, height=2, bg="lightgrey", font=('Verdana', '12')).pack(side=LEFT)
        self.valor2 = Entry(self.frame3, width=5, font=('Verdana', '12'))
        self.valor2.pack(side=LEFT)

        # Display com o resultado
        self.frame5 = Frame(root)
        self.frame5.pack()
        Label(self.frame5, text='Resultado:', highlightthickness=10, bg="lightgrey", height=2, font=('Verdana', '12')).pack(side=LEFT)
        self.msg = Label(self.frame5, relief= 'ridge', height=2, width=8, font=('Verdana', '12'))
        self.msg.pack(side=RIGHT)

        # Botões de operações
        self.frame4 = Frame(root)
        self.frame4.pack()
        Button(self.frame4, text='+', command=self.somar, padx= 3, width=2, borderwidth=5).pack(side=LEFT, padx=3)
        Button(self.frame4, text='-', command=self.subtrair, padx= 3, width=2, borderwidth=5).pack(side=LEFT, padx=3)
        Button(self.frame4, text='*', command=self.multiplicar, padx= 3, width=2, borderwidth=5).pack(side=LEFT, padx=3)
        Button(self.frame4, text='/', command=self.dividir, padx= 3, width=2, borderwidth=5).pack(side=LEFT, padx=3)
        
        self.frame7 = Frame(root)
        self.frame7.pack(ipady=5)
        Button(self.frame7, text='Sqrt', command=self.sqrt, padx= 3, width=3, borderwidth=5).pack(side=LEFT, padx=8)
        Button(self.frame7, text='C', command=self.clear, padx= 3, width=10, borderwidth=5).pack(side=LEFT, padx=8)
        Button(self.frame7, text='⟳', command=self.user_result, padx= 3, width=3, borderwidth=5).pack(side=LEFT, padx=8)

        # Histórico de operações
        self.frame6 = Frame(root)
        self.frame6.pack()
        self.calculation_listbox = Listbox(self.frame6, width=30, height=5, font=('Verdana', '12'))
        self.calculation_listbox.pack(pady=10)

        # Inicializando conexão do database e carregar histórico
        self.conn = sqlite3.connect('my_calculator.db')
        self.cursor = self.conn.cursor()
        self.create_table()
        self.load_past_calculations()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS calculations (
                id INTEGER PRIMARY KEY,
                numero1 REAL,
                numero2 REAL,
                operation TEXT,
                result REAL
            )
        ''')
        self.conn.commit()

    def load_past_calculations(self):
        self.calculation_listbox.delete(0, END)  # Clear current items in listbox
        self.cursor.execute('SELECT numero1, numero2, operation, result FROM calculations ORDER BY id DESC')
        past_calculations = self.cursor.fetchall()
        for numero1, numero2, operation, result in past_calculations:
            self.calculation_listbox.insert(END, f'{numero1:.2f} {operation} {numero2:.2f} = {result:.2f}')

    def clear(self):
        self.valor1.delete(0, END)
        self.valor2.delete(0, END)
    
    def user_result(self):
        self.cursor.execute('SELECT result FROM calculations ORDER BY id DESC LIMIT 1')
        result = self.cursor.fetchone()
        if result:
            result_float = float(result[0])
        else:
            result_float = 0
        self.valor1.insert(0, f'{result_float:.2f}')

    def somar(self):
        valor1 = float(self.valor1.get())
        valor2 = float(self.valor2.get())
        result = valor1 + valor2
        self.msg.config(text=f'{result:.2f}')
        self.store_calculation(valor1, valor2, '+', result)

    def subtrair(self):
        valor1 = float(self.valor1.get())
        valor2 = float(self.valor2.get())
        result = valor1 - valor2
        self.msg.config(text=f'{result:.2f}')
        self.store_calculation(valor1, valor2, '-', result)

    def multiplicar(self):
        valor1 = float(self.valor1.get())
        valor2 = float(self.valor2.get())
        result = valor1 * valor2
        self.msg.config(text=f'{result:.2f}')
        self.store_calculation(valor1, valor2, '*', result)

    def dividir(self):
        valor1 = float(self.valor1.get())
        valor2 = float(self.valor2.get())
        if valor2 != 0:
            result = valor1 / valor2
            self.msg.config(text=f'{result:.2f}')
            self.store_calculation(valor1, valor2, '/', result)
        else:
            self.msg.config(text='Erro: Divisão por zero')

    def sqrt(self):
        valor1 = float(self.valor1.get())
        result = sqrt(valor1)
        self.msg.config(text=f'{result:.2f}')
        self.store_calculation(valor1, 2, 'sqrt', result)

    def store_calculation(self, numero1, numero2, operation, result):
        self.cursor.execute('INSERT INTO calculations (numero1, numero2, operation, result) VALUES (?, ?, ?, ?)', (numero1, numero2, operation, result))
        self.conn.commit()
        self.load_past_calculations()  # Update history after storing new calculation

    def __del__(self):
        self.conn.close()

# Main aplicação
if __name__ == "__main__":
    app = Tk()
    calculadora = Calculadora(app)
    app.mainloop()
    
