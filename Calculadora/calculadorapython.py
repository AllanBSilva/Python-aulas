import sqlite3
from tkinter import *
from tkinter import ttk
from math import sqrt

class Calculadora:
    def __init__(self, root):
        # Initialize tkinter window
        root.title('Calculadora')
        root.geometry("900x450")
        
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
        self.msg = Label(self.frame5, relief= 'ridge', height=2, width=16, font=('Verdana', '12'))
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

        # Treeview para exibir histórico de cálculos
        self.frame8 = Frame(root)
        self.frame8.pack(pady=10)
        self.tree = ttk.Treeview(self.frame8, columns=("Número1", "Número2", "Operação", "Resultado"), show="headings", height=5)
        
        # Treeview configuração cabeçalho
        self.tree.heading('#0', text='ID')
        self.tree.heading('Número1', text='Número1')
        self.tree.heading('Número2', text='Número2')
        self.tree.heading('Operação', text='Operação')
        self.tree.heading('Resultado', text='Resultado')

        # Treeview configuração coluna
        self.tree.column('Número1', anchor=CENTER)
        self.tree.column('Número2', anchor=CENTER)
        self.tree.column('Operação', anchor=CENTER)
        self.tree.column('Resultado', anchor=CENTER)
        self.tree.pack()

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
        self.tree.delete(*self.tree.get_children())  # Clear current items in Treeview
        self.cursor.execute('SELECT id, numero1, numero2, operation, result FROM calculations ORDER BY id DESC')
        past_calculations = self.cursor.fetchall()
        for row in past_calculations:
            #self.calculation_listbox.insert(END, f'{row[1]:.2f} {row[3]} {row[2]:.2f} = {row[4]:.2f}')
            self.tree.insert("", END, text=row[0], values=(f'{row[1]:.2f}', f'{row[2]:.2f}', row[3], f'{row[4]:.2f}'))

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
        self.clear()

    def subtrair(self):
        valor1 = float(self.valor1.get())
        valor2 = float(self.valor2.get())
        result = valor1 - valor2
        self.msg.config(text=f'{result:.2f}')
        self.store_calculation(valor1, valor2, '-', result)
        self.clear()

    def multiplicar(self):
        valor1 = float(self.valor1.get())
        valor2 = float(self.valor2.get())
        result = valor1 * valor2
        self.msg.config(text=f'{result:.2f}')
        self.store_calculation(valor1, valor2, '*', result)
        self.clear()

    def dividir(self):
        valor1 = float(self.valor1.get())
        valor2 = float(self.valor2.get())
        if valor2 != 0:
            result = valor1 / valor2
            self.msg.config(text=f'{result:.2f}')
            self.store_calculation(valor1, valor2, '/', result)
        else:
            self.msg.config(text='Erro:Divisão por 0')
        self.clear()

    def sqrt(self):
        valor1 = float(self.valor1.get())
        result = sqrt(valor1)
        self.msg.config(text=f'{result:.2f}')
        self.store_calculation(valor1, 2, 'sqrt', result)
        self.clear()

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
    
