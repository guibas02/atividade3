# -*- coding utf-8 -*-
import sqlite3

con = sqlite3.connect('bancoImc.db')
cur = con.cursor()
cur.execute('''
    create table pacientes(
        id integer primary key autoincrement,
        nome text,
        endereco text,
        altura real,
        peso real,
        resultado text
    )
''')
con.close()

print ("banco de dados gerado com sucesso")