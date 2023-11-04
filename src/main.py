import sqlite3
import pandas as pd
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from interface import Ui_MainWindow
from database import Data_base, DB_NAME, ROOT_DIR
from utils import calcula_salario_liquido
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=  None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Projeto RAD")
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)


        # PAGES ######################################
        self.actionFuncion_rio.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.cadastro))
        self.actionListagem_de_Func.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.listagem))
        self.actionRelat_rio_de_pgto.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.processo))
        self.actionVers_o.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.sobre))
        self.actionHome.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.home))
        self.btn_voltar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.processo))
        ################################################

        # BUTTONS ######################################
        self.btn_salvar.clicked.connect(self.salvar_dados)
        self.btn_salvar.clicked.connect(self.limpar_campos_cadastro)
        self.btn_listar.clicked.connect(self.buscar_func)
        self.btn_alterar.clicked.connect(self.atualizar_cadastro)
        self.btn_delete.clicked.connect(self.deletar_cadatro)
        self.btn_excel.clicked.connect(self.gerar_doc)
        self.btn_gerar_pagamento.clicked.connect(self.calcula_pagamento)
        ################################################

    def salvar_dados(self):
        cpf = self.line_cpf.text()
        nome = self.line_nome.text()
        endereco = self.line_endereco.text()
        telefone = self.line_telefone.text()
        cargo = self.line_cargo.text()
        data_adm = self.line_admissao.text()
        salario = self.line_salario.text()

        try:
            int(cpf)
        except:
            alert = QMessageBox()
            alert.setIcon(QMessageBox.Information)
            alert.setWindowTitle("ERRO")
            alert.setText("CAMPO CPF: Utilize caracteres numéricos!")
            alert.exec()   
            return

        try:
            if ',' in salario:
                alert = QMessageBox()
                alert.setIcon(QMessageBox.Information)
                alert.setWindowTitle("ERRO")
                alert.setText("CAMPO SALÁRIO: substitua a ',' por '.' !")
                alert.exec()   
                return
            float(salario)
        except:
            alert = QMessageBox()
            alert.setIcon(QMessageBox.Information)
            alert.setWindowTitle("ERRO")
            alert.setText("CAMPO SALÁRIO: Utilize caracteres numéricos!")
            alert.exec()
            return   


        print(banco.register_funcionarios(cpf, nome, endereco, telefone, cargo, data_adm, salario))

        alert = QMessageBox()
        alert.setIcon(QMessageBox.Information)
        alert.setWindowTitle("Cadastro")
        alert.setText("Cadastro realizado com sucesso!")
        alert.exec() 



    def limpar_campos_cadastro(self):
        self.line_cpf.clear()
        self.line_nome.clear()
        self.line_endereco.clear()
        self.line_telefone.clear()
        self.line_cargo.clear()
        self.line_admissao.clear()
        self.line_salario.clear()

    def buscar_func(self):
        result = banco.select_all_funcionarios()

        self.table_listagem.clearContents()
        self.table_listagem.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.table_listagem.setItem(row, column, QTableWidgetItem(str(data)))

    def atualizar_cadastro(self):

        dados = []
        update_dados = []

        for row in range(self.table_listagem.rowCount()):
            for column in range(self.table_listagem.columnCount()):
                dados.append(self.table_listagem.item(row, column).text())

            update_dados.append(dados)
            dados = []

        ######
        for funcionario in update_dados:
            banco.uppdate_funcionario(tuple(funcionario))

        alert = QMessageBox()
        alert.setIcon(QMessageBox.Information)
        alert.setWindowTitle("Atualização de Cadastro")
        alert.setText("Dados atualizados com sucesso!")
        alert.exec()

        self.table_listagem.reset()
        self.buscar_func()

    def deletar_cadatro(self):
        alert = QMessageBox()
        alert.setWindowTitle("Excluir")
        alert.setText("Este colaborador será excluído.")
        alert.setInformativeText("Você tem certeza que quer excluir?")
        alert.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = alert.exec()
        
        if resp == QMessageBox.Yes:
            cpf = self.table_listagem.selectionModel().currentIndex().siblingAtColumn(0).data()
            result = banco.delete_funcionario(cpf)
            self.buscar_func()

            alert = QMessageBox()
            alert.setIcon(QMessageBox.Information)
            alert.setWindowTitle("Exclusão")
            alert.setText(result)
            alert.exec()

    def gerar_doc(self):

        cnx = sqlite3.connect(DB_NAME)

        funcionarios =pd.read_sql_query("""SELECT * FROM Funcionarios""", cnx)

        funcionarios.to_excel("Funcionarios.xlsx", sheet_name='funcionarios', index=False)

        alert = QMessageBox()
        alert.setIcon(QMessageBox.Information)
        alert.setWindowTitle("Sucesso")
        alert.setText(f"Arquivo gerado com sucesso em {ROOT_DIR.parent}!")
        alert.exec()

    def calcula_pagamento(self):

        cursor = banco.connection.cursor()
        cursor.execute("SELECT SALARIO, NOME FROM Funcionarios WHERE CPF = ? ", [self.line_cpf_pagamento.text()])
        dados = cursor.fetchall()
        try:
            print(dados[0][1], dados[0][0])
            salario, inss, irrf, fgts = calcula_salario_liquido(dados[0][0])
            self.func_name_label.setText(dados[0][1])
            self.salario_label.setText("R$ " + str(salario))
            self.inss_label.setText(f"R$ {round(inss, 2)}")
            self.fgts_label.setText(f"R$ {round(fgts, 2)}")
            self.irrf_label.setText(f"R$ {round(irrf, 2)}")
            self.sal_liq_label.setText(f'R$ {round(salario - inss - irrf, 2)}')
             
            self.stackedWidget.setCurrentWidget(self.resultado_pgto)
            self.func_name_label.setStyleSheet('font-size: 16px; font-weight: bold;')
            self.salario_label.setStyleSheet('font-size: 16px; font-weight: bold;')
            self.inss_label.setStyleSheet('font-size: 16px; font-weight: bold;')
            self.fgts_label.setStyleSheet('font-size: 16px; font-weight: bold;')
            self.irrf_label.setStyleSheet('font-size: 16px; font-weight: bold;')
            self.sal_liq_label.setStyleSheet('font-size: 16px; font-weight: bold;')
        except:
            print('ERRO')
            alert = QMessageBox()
            alert.setIcon(QMessageBox.Information)
            alert.setWindowTitle("ERRO")
            alert.setText("CPF ou salário inválidos")
            alert.exec()   
         


if __name__ == '__main__':
    # Inicializa o Banco
    banco = Data_base()
    banco.connect()
    banco.create_table_funcionarios()    


    # Interface
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    banco.close_connection()