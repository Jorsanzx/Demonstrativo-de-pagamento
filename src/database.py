import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME='db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME

class Data_base:
    def __init__(self, name = DB_NAME):

        self.name = name

    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass

    def create_table_funcionarios(self):

        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Funcionarios(
            CPF TEXT PRIMARY KEY,
            NOME TEXT,
            ENDERECO TEXT,
            TELEFONE TEXT,
            CARGO TEXT,
            DATA_ADM DATE,
            SALARIO REAL          
            )
        """)
        self.connection.commit()
        cursor.close()

    def register_funcionarios(self, cpf, nome, endereco, telefone,
                            cargo, data_adm, salario):
        valores = [cpf, nome,endereco, telefone, cargo, data_adm, salario]
        cursor = self.connection.cursor()

        try:

            cursor.execute('INSERT INTO Funcionarios'
                            '(CPF, NOME, ENDERECO, TELEFONE, CARGO, DATA_ADM, SALARIO)'
                            'VALUES' 
                            '(?, ?, ? ,? ,? ,? ,?)', valores )
                
            self.connection.commit()
            cursor.close()

            return "DADOS INSERIDOS"
        except:
            return "ERRO NA GRAVAÇÃO"

    
    def select_all_funcionarios(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Funcionarios")
            funcionarios = cursor.fetchall()
            return funcionarios
        
        except:
            pass

    def delete_funcionario(self, cpf):

        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Funcionarios WHERE CPF = '{cpf}' ")
            
            self.connection.commit()
            cursor.close()

            return "Cadastro Excluido com Sucesso!"
        
        except:
            return "Erro ao Excluir Registro"

    def uppdate_funcionario(self, valores):
        
        
  
        cursor = self.connection.cursor()
        cursor.execute(f""" UPDATE Funcionarios SET 
                        NOME = ?, 
                        ENDERECO = ?, 
                        TELEFONE = ?, 
                        CARGO = ?, 
                        DATA_ADM = ?, 
                        SALARIO = ?
                        WHERE CPF = ? """, [valores[1],valores[2], valores[3],
                                            valores[4], valores[5], valores[6], valores[0]] )
        
        self.connection.commit()
        cursor.close()
        
        
        

banco = Data_base()

