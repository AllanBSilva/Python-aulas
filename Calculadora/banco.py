import sqlite3

# Conectar-se ao banco de dados (ele será criado se não existir)
conn = sqlite3.connect('meu_banco.db')

# Criar um cursor para executar consultas SQL
cursor = conn.cursor()

# Exemplo de criação de uma tabela
cursor.execute('''CREATE TABLE IF NOT EXISTS calculos (
                    numero1 FLOAT NOT NULL,
                    numero2 FLOAT NOT NULL,
                    expressao TEXT,
                    resultado REAL, 
                    PRIMARY KEY (resultado)
                )''')


# Exemplo de inserção de dados

numero1 = 5.5
numero2 = 3.2
expressao = '5.5 + 3.2'
resultado = numero1 + numero2

cursor.execute('''INSERT INTO calculos (numero1, numero2, expressao, resultado)
                  VALUES (?, ?, ?, ?)''', (numero1, numero2, expressao, resultado))

# Commit para salvar as alterações
conn.commit()

# Fechar o cursor e a conexão com o banco de dados
cursor.close()
conn.close()
