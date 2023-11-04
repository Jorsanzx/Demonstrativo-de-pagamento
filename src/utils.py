
def calcula_inss(salario):
    inss = 0
    if salario <= 1320:
        inss = salario * 0.075


    elif salario > 1320 and salario <= 2571.29:
        faixa1 = salario - 1320
        inss1 = 1320 * 0.075
        inss2 = faixa1 * 0.09
        inss = inss1 + inss2


    elif salario > 2571.29 and salario <= 3856.94:
        faixa1 = salario - 2571.29
        inss1 = 1320 * 0.075
        inss2 = 1251.29 * 0.09
        inss3 = faixa1 * 0.12
        inss = inss1 + inss2 + inss3


    elif salario > 3856.94 and salario <= 7507.49:
        faixa1 = salario - 3856.94
        inss1 = 1320 * 0.075
        inss2 = 1251.29 * 0.09
        inss3 = 1285.64 * 0.12
        inss4 = faixa1 * 0.14
        inss = inss1 + inss2 + inss3 + inss4


    elif salario > 7507.49:
        inss1 = 1320 * 0.075
        inss2 = 1251.29 * 0.09
        inss3 = 1285.64 * 0.12
        inss4 = 3650.56 * 0.14
        inss = inss1 + inss2 + inss3 + inss4

    return inss

def calcula_irrf(salario, inss):
    base = salario - inss

    if base <= 2112:
        irrf = 0

    elif base > 2112 and base <= 2826.65:
        irrf = base * 0.075 - 158.40

    elif base > 2826.65 and base <= 3751.05:
        irrf = base * 0.15 - 370.40

    elif base > 3751.05 and base <= 4664.68:
        irrf = base * 0.225 - 651.73

    elif base > 4664.68:
        irrf = base * 0.275 - 884.96

    return irrf

def calcula_salario_liquido(salario):
    fgts = salario * 0.08
    inss = calcula_inss(salario)
    irrf = calcula_irrf(salario, inss) 


    return salario, inss, irrf, fgts





        