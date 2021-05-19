from folha_pagamento import *
from colaborador import Colaborador
from movimento_folha import MovimentoFolha


def main():
    # Objeto FP:
    fp = FolhaPagamento(9, 2019)
    # Objetos CL:
    cl01 = Colaborador("100", "Manoel Claudino", "Av 13 de Maio 2081", "88671020",
                       "Benfica", "60020-060", "124543556-89", 4500.00)
    cl02 = Colaborador("200", "Carmelina da Silva", "Avenida dos Expedicionários 1200",
                       "3035-1280", "Aeroporto", "60530-020", "301789435-54",
                       2500.00)
    cl03 = Colaborador("300", "Gurmelina Castro Saraiva", "Av João Pessoa 1020",
                       "3235-1089", "Damas", "60330-090", "350245632-76", 3000.00)
    # Objetos MF:
    mf01 = MovimentoFolha(100, "Salario", 4500.00, "P")
    mf02 = MovimentoFolha(100, "Plano Saúde", 1000.00, "P")
    mf03 = MovimentoFolha(100, "Pensão", 600.00, "D")
    mf04 = MovimentoFolha(200, "Salario", 2500.00, "P")
    mf05 = MovimentoFolha(200, "Gratificação", 1000.00, "P")
    mf06 = MovimentoFolha(200, "Faltas", 600.00, "D")
    mf07 = MovimentoFolha(300, "Salario", 4500.00, "P")
    mf08 = MovimentoFolha(300, "Plano Saúde", 1000.00, "P")
    mf09 = MovimentoFolha(300, "Pensão", 600.00, "D")
    # Inserir todos os objetos do tipo MovimentoFolha na lista movimentos do objeto FP:
    fp.inserir_movimentos(mf01)
    fp.inserir_movimentos(mf02)
    fp.inserir_movimentos(mf03)
    fp.inserir_movimentos(mf04)
    fp.inserir_movimentos(mf05)
    fp.inserir_movimentos(mf06)
    fp.inserir_movimentos(mf07)
    fp.inserir_movimentos(mf08)
    fp.inserir_movimentos(mf09)

    cl01.inserir_movimentos1(mf01)
    cl01.inserir_movimentos1(mf02)
    cl01.inserir_movimentos1(mf03)
    cl02.inserir_movimentos1(mf04)
    cl02.inserir_movimentos1(mf05)
    cl02.inserir_movimentos1(mf06)
    cl03.inserir_movimentos1(mf07)
    cl03.inserir_movimentos1(mf08)
    cl03.inserir_movimentos1(mf09)

    print(cl01.calcular_salario(fp))
    print(cl02.calcular_salario(fp))
    print(cl03.calcular_salario(fp))


if __name__ == '__main__':
    main()
