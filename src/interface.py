# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import img_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(890, 429)
        MainWindow.setStyleSheet(u";\n"
"background-color: rgb(200, 200, 200);")
        self.actionFuncion_rio = QAction(MainWindow)
        self.actionFuncion_rio.setObjectName(u"actionFuncion_rio")
        self.actionFuncion_rio.setEnabled(True)
        self.actionListagem_de_Func = QAction(MainWindow)
        self.actionListagem_de_Func.setObjectName(u"actionListagem_de_Func")
        self.actionRelat_rio_de_pgto = QAction(MainWindow)
        self.actionRelat_rio_de_pgto.setObjectName(u"actionRelat_rio_de_pgto")
        self.actionVers_o = QAction(MainWindow)
        self.actionVers_o.setObjectName(u"actionVers_o")
        self.actionHome = QAction(MainWindow)
        self.actionHome.setObjectName(u"actionHome")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_8 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.horizontalLayout_4 = QHBoxLayout(self.home)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.home)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.home)
        self.cadastro = QWidget()
        self.cadastro.setObjectName(u"cadastro")
        self.verticalLayout = QVBoxLayout(self.cadastro)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.cadastro)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line_cpf = QLineEdit(self.frame)
        self.line_cpf.setObjectName(u"line_cpf")
        self.line_cpf.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.line_cpf, 2, 0, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 4)

        self.line_admissao = QLineEdit(self.frame)
        self.line_admissao.setObjectName(u"line_admissao")
        self.line_admissao.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_admissao.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.line_admissao, 5, 2, 1, 1)

        self.line_endereco = QLineEdit(self.frame)
        self.line_endereco.setObjectName(u"line_endereco")
        self.line_endereco.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.line_endereco, 4, 0, 1, 3)

        self.line_salario = QLineEdit(self.frame)
        self.line_salario.setObjectName(u"line_salario")
        self.line_salario.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.line_salario, 5, 3, 1, 1)

        self.line_nome = QLineEdit(self.frame)
        self.line_nome.setObjectName(u"line_nome")
        self.line_nome.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.line_nome, 2, 2, 1, 2)

        self.line_cargo = QLineEdit(self.frame)
        self.line_cargo.setObjectName(u"line_cargo")
        self.line_cargo.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.line_cargo, 5, 0, 1, 2)

        self.line_telefone = QLineEdit(self.frame)
        self.line_telefone.setObjectName(u"line_telefone")
        self.line_telefone.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.line_telefone, 4, 3, 1, 1)

        self.line_nome.raise_()
        self.line_cpf.raise_()
        self.label_2.raise_()
        self.line_admissao.raise_()
        self.line_endereco.raise_()
        self.line_salario.raise_()
        self.line_cargo.raise_()
        self.line_telefone.raise_()

        self.verticalLayout.addWidget(self.frame)

        self.btn_salvar = QPushButton(self.cadastro)
        self.btn_salvar.setObjectName(u"btn_salvar")
        self.btn_salvar.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.btn_salvar, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.cadastro)
        self.listagem = QWidget()
        self.listagem.setObjectName(u"listagem")
        self.verticalLayout_3 = QVBoxLayout(self.listagem)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.label_3 = QLabel(self.listagem)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.table_listagem = QTableWidget(self.listagem)
        if (self.table_listagem.columnCount() < 7):
            self.table_listagem.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_listagem.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_listagem.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_listagem.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_listagem.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_listagem.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_listagem.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_listagem.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.table_listagem.setObjectName(u"table_listagem")
        self.table_listagem.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.table_listagem)

        self.frame_2 = QFrame(self.listagem)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_listar = QPushButton(self.frame_2)
        self.btn_listar.setObjectName(u"btn_listar")

        self.verticalLayout_2.addWidget(self.btn_listar)

        self.btn_alterar = QPushButton(self.frame_2)
        self.btn_alterar.setObjectName(u"btn_alterar")

        self.verticalLayout_2.addWidget(self.btn_alterar)

        self.btn_excel = QPushButton(self.frame_2)
        self.btn_excel.setObjectName(u"btn_excel")

        self.verticalLayout_2.addWidget(self.btn_excel)

        self.btn_delete = QPushButton(self.frame_2)
        self.btn_delete.setObjectName(u"btn_delete")

        self.verticalLayout_2.addWidget(self.btn_delete)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_5.addWidget(self.frame_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.stackedWidget.addWidget(self.listagem)
        self.resultado_pgto = QWidget()
        self.resultado_pgto.setObjectName(u"resultado_pgto")
        self.verticalLayout_6 = QVBoxLayout(self.resultado_pgto)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_3 = QFrame(self.resultado_pgto)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.inss_label = QLabel(self.frame_3)
        self.inss_label.setObjectName(u"inss_label")

        self.gridLayout_2.addWidget(self.inss_label, 2, 1, 1, 1)

        self.sal_liq_label = QLabel(self.frame_3)
        self.sal_liq_label.setObjectName(u"sal_liq_label")

        self.gridLayout_2.addWidget(self.sal_liq_label, 5, 1, 1, 1)

        self.salario_label = QLabel(self.frame_3)
        self.salario_label.setObjectName(u"salario_label")

        self.gridLayout_2.addWidget(self.salario_label, 1, 1, 1, 1)

        self.func_name_label = QLabel(self.frame_3)
        self.func_name_label.setObjectName(u"func_name_label")

        self.gridLayout_2.addWidget(self.func_name_label, 0, 1, 1, 1)

        self.label_16 = QLabel(self.frame_3)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_2.addWidget(self.label_16, 5, 0, 1, 1)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.fgts_label = QLabel(self.frame_3)
        self.fgts_label.setObjectName(u"fgts_label")

        self.gridLayout_2.addWidget(self.fgts_label, 3, 1, 1, 1)

        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_14 = QLabel(self.frame_3)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 4, 0, 1, 1)

        self.irrf_label = QLabel(self.frame_3)
        self.irrf_label.setObjectName(u"irrf_label")

        self.gridLayout_2.addWidget(self.irrf_label, 4, 1, 1, 1)

        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)

        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 3, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.btn_voltar = QPushButton(self.resultado_pgto)
        self.btn_voltar.setObjectName(u"btn_voltar")

        self.verticalLayout_6.addWidget(self.btn_voltar, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.resultado_pgto)
        self.processo = QWidget()
        self.processo.setObjectName(u"processo")
        self.verticalLayout_5 = QVBoxLayout(self.processo)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.processo)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_5 = QLabel(self.processo)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.line_cpf_pagamento = QLineEdit(self.processo)
        self.line_cpf_pagamento.setObjectName(u"line_cpf_pagamento")
        self.line_cpf_pagamento.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.line_cpf_pagamento)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.btn_gerar_pagamento = QPushButton(self.processo)
        self.btn_gerar_pagamento.setObjectName(u"btn_gerar_pagamento")

        self.verticalLayout_5.addWidget(self.btn_gerar_pagamento, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.processo)
        self.sobre = QWidget()
        self.sobre.setObjectName(u"sobre")
        self.horizontalLayout_6 = QHBoxLayout(self.sobre)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_4 = QFrame(self.sobre)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_7.addWidget(self.label_7)

        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_7.addWidget(self.label_9)


        self.verticalLayout_8.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_7.addWidget(self.label_11, 0, Qt.AlignHCenter)


        self.verticalLayout_8.addWidget(self.frame_6)


        self.horizontalLayout_3.addWidget(self.frame_4)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)

        self.stackedWidget.addWidget(self.sobre)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.horizontalLayout_8.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 890, 22))
        self.menuCadastro = QMenu(self.menubar)
        self.menuCadastro.setObjectName(u"menuCadastro")
        self.menuProcessos = QMenu(self.menubar)
        self.menuProcessos.setObjectName(u"menuProcessos")
        self.menuSobre = QMenu(self.menubar)
        self.menuSobre.setObjectName(u"menuSobre")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuCadastro.menuAction())
        self.menubar.addAction(self.menuProcessos.menuAction())
        self.menubar.addAction(self.menuSobre.menuAction())
        self.menuCadastro.addAction(self.actionFuncion_rio)
        self.menuCadastro.addAction(self.actionListagem_de_Func)
        self.menuProcessos.addAction(self.actionRelat_rio_de_pgto)
        self.menuSobre.addAction(self.actionVers_o)
        self.menuSobre.addSeparator()
        self.menuSobre.addAction(self.actionHome)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionFuncion_rio.setText(QCoreApplication.translate("MainWindow", u"Funcion\u00e1rio", None))
        self.actionListagem_de_Func.setText(QCoreApplication.translate("MainWindow", u"Listagem de Func.", None))
        self.actionRelat_rio_de_pgto.setText(QCoreApplication.translate("MainWindow", u"Relat\u00f3rio de pgto.", None))
        self.actionVers_o.setText(QCoreApplication.translate("MainWindow", u"Vers\u00e3o", None))
        self.actionHome.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/img/img/logo_zxsoft.png\"/></p></body></html>", None))
        self.line_cpf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Cadastro</span></p></body></html>", None))
        self.line_admissao.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data ADM", None))
        self.line_endereco.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
        self.line_salario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Sal\u00e1rio", None))
        self.line_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.line_cargo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cargo", None))
        self.line_telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(DDD) Telefone", None))
        self.btn_salvar.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Funcion\u00e1rios</span></p></body></html>", None))
        ___qtablewidgetitem = self.table_listagem.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem1 = self.table_listagem.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem2 = self.table_listagem.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None));
        ___qtablewidgetitem3 = self.table_listagem.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Telefone", None));
        ___qtablewidgetitem4 = self.table_listagem.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Cargo", None));
        ___qtablewidgetitem5 = self.table_listagem.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Data de Adm", None));
        ___qtablewidgetitem6 = self.table_listagem.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Sal\u00e1rio", None));
        self.btn_listar.setText(QCoreApplication.translate("MainWindow", u"Listar", None))
        self.btn_alterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.inss_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">R$</span></p></body></html>", None))
        self.sal_liq_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">R$</span></p></body></html>", None))
        self.salario_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">R$</span></p></body></html>", None))
        self.func_name_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">R$</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Sal\u00e1rio L\u00edquido:</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Funcion\u00e1rio:</span></p></body></html>", None))
        self.fgts_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">R$</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Sal\u00e1rio:</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">IRRF:</span></p></body></html>", None))
        self.irrf_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">R$</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">INSS:</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">FGTS:</span></p></body></html>", None))
        self.btn_voltar.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Demonstrativo de Pagamento</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.line_cpf_pagamento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o CPF", None))
        self.btn_gerar_pagamento.setText(QCoreApplication.translate("MainWindow", u"Gerar", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Vers\u00e3o: 1.0</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Autor: ZX Softwares Solu\u00e7\u00f5es LTDA</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/img/img/logo_zxsoft_reduced.png\"/></p></body></html>", None))
        self.menuCadastro.setTitle(QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.menuProcessos.setTitle(QCoreApplication.translate("MainWindow", u"Processos", None))
        self.menuSobre.setTitle(QCoreApplication.translate("MainWindow", u"Sobre", None))
    # retranslateUi

