import mysql.connector
import pandas as pd
from mysql.connector import Error

try:
    #Estabelece a conexão
    conexao = mysql.connector.connect(
        host='localhost',       # ou o IP do servidor
        user='root',
        password='',
        database='escola'
    )

    if conexao.is_connected():
        print("Conectado com sucesso!")
        
        #Cria um cursor (objeto que permite executar comandos)
        cursor = conexao.cursor()
        
        sql = "Insert INTO alunos (nome, cpf, nascimento, matricula, id_curso) VALUES (%s, %s, %s, %s, %s)"
        
        # Valores que serão substituídos nos placeholders, na mesma ordem 
        valores = ('Eduarda', '15014842123', '2000-04-22', '12343', '2')
        
        # Executa o INSERT no banco, substituindo os %s pelos valores em "valores"
        # O conector trata automaticamente aspas, datas e acentos
        cursor.execute(sql, valores)
        
        # sem commit o INSERT fica so na memória e não é gravado no banco. É necessário confirmar a transação.
        conexao.commit()
        
        # Mostra o ID (AUTO_INCREMENT) gerado na última inserção
        print(f"Linha inserida. ID gerado: {cursor.lastrowid}")
        
        cursor.execute("SELECT * FROM alunos LIMIT 5")
        
        #Busca os resultados
        resultados = cursor.fetchall()
        for linha in resultados:
            print(linha)
                    
        
except Error as e:
    print(f"Erro ao conectar ou executar: {e}")
        
finally:
    #Fecha o cursor (se foi criado)
    if 'cursor' in locals():
        try:
            cursor.close()
        except Exception:
            pass  #Se já estiver fechado ou ocorrer erro, ignora
            
            #Fecha a conexão (se foi criada e ainda está conectada)
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print("Conexão encerrada.")