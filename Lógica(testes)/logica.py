import pandas as pd
from openpyxl import Workbook


def ler_planilha():
    excel = pd.read_excel("C:/Users/USER/Desktop/PROGRAMAÇÃO/PROGRAMAÇÕES/PYTHON/Projeto Python Senai (Planilha)/Manipulação de Planilhas Lógica/planilha_teste.xlsx")
    print(excel)

def deletar_linha():
    excel = pd.read_excel("C:/Users/USER/Desktop/PROGRAMAÇÃO/PROGRAMAÇÕES/PYTHON/Projeto Python Senai (Planilha)/Manipulação de Planilhas Lógica/planilha_teste.xlsx")
    excel = excel.drop(index=0)
    print(excel)

def deletar_coluna():
    excel = pd.read_excel("C:/Users/USER/Desktop/PROGRAMAÇÃO/PROGRAMAÇÕES/PYTHON/Projeto Python Senai (Planilha)/Manipulação de Planilhas Lógica/planilha_teste.xlsx")
    print(excel)

def add_linha():
    pass

def add_coluna():
    pass

def atualizar_planilha():
    excel = pd.read_excel("C:/Users/USER/Desktop/PROGRAMAÇÃO/PROGRAMAÇÕES/PYTHON/Projeto Python Senai (Planilha)/Manipulação de Planilhas Lógica/planilha_teste.xlsx")
    print(excel)

