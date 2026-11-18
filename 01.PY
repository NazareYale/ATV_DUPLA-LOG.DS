import os
os.system('cls')

LOOPS = 3
loginC = 'cachorrodealexandre'
senhaC = 'woof'

def calcular_inss(salarioB):
    if salarioB <= 1621.00:
        inss = salarioB * 0.075
    elif salarioB <= 2902.84:
        inss = 121.575 + (salarioB - 1621.00) * 0.09
    elif salarioB <= 4354.27:
        inss = 236.9406 + (salarioB - 2902.84) * 0.12
    elif salarioB <= 8475.55:
        inss = 411.1122 + (salarioB - 4354.27) * 0.14
    else:
        inss = 988.10
    return inss

def calcular_irrf(salarioB, inss, dependentes):
    base = salarioB - inss - dependentes * 189.59

    if base <= 2428.80:
        imposto = 0
    elif base <= 2826.65:
        imposto = base * 0.075 - 182.16
    elif base <= 3751.05:
        imposto = base * 0.15 - 394.16
    elif base <= 4664.68:
        imposto = base * 0.225 - 675.49
    else:
        imposto = base * 0.275 - 908.73


    if imposto < 0:
        imposto = 0

    if salarioB <= 5000.00:
        imposto = 0
    elif salarioB <= 7350.00:
        reducao = 978.62 - 0.133145 * salarioB
        imposto = imposto - reducao
        if imposto < 0:
            imposto = 0

    return imposto

def calcular_vt(salarioB, valeT):
    if valeT == 's':
        return salarioB * 0.06
    else:
        return 0

def calcular_vr(valeR):
    return valeR * 0.20

def calcular_plano_saude(dependentes):
    return dependentes * 150

def mostrar_contracheque(login, salarioB, inss, irrf, valeT, valeR, dependente):
    total = inss + irrf + valeT + valeR + dependente
    liquido = salarioB - total

    print('\nCONTRACHEQUE - MATRICULA', login)
    print(f'Salário base R${salarioB:.2f}')
    print(f'(-) INSS R${inss:.2f}')
    print(f'(-) IRRF R${irrf:.2f}')
    print(f'(-) Vale-transporte R${valeT:.2f}')
    print(f'(-) Vale-refeição R${valeR:.2f}')
    print(f'(-) Plano de saúde R${dependente:.2f}')
    print('-----------------------------------')
    print(f'Total de descontos R${total:.2f}')
    print(f'SALÁRIO LIQUIDO R${liquido:.2f}')
    print("-----------------------------------")
    print(f'Beneficios: Vale Trasnporte informado = R${valeT:.2f} | Vale Refeição informado = R${valeR:.2f}')


for i in range(LOOPS):
        login = input('Digite seu login: ')
        senha = input('Digite sua senha: ')

        if login == loginC and senha == senhaC:
            print(f'\n{login} Seja bem-vindo!')
            break
        else:
            print(f'\nLogin ou senha errada. Tente de novo!')


while True:
    print()
    salarioB = float(input('Digite o seu salário base: R$'))
    if salarioB <= 0:
        print('Valor inválido!\nDigite o valor correto.')
        salarioB = float(input('Digite o seu salário base: R$'))
        
    valeT = input('Deseja receber vale-transporte(s/n): ').strip().lower()
    if valeT != 's' or valeT != 'n':
        print('Resposta errada, tente novamente.')
        valeT = input('Deseja receber vale-transporte(s/n): ').strip().lower()

    valeR = int(input('Digite o valor do vale refeição: R$'))
    if valeR < 0:
        print('Resposta errada, tente novamente.')
        valeR = int(input('Digite o valor do vale refeição: R$'))
        
    dependentes = int(input('Digite o número de dependentes do dependente de saúde: '))
    if dependentes < 0:
        print('Resposta errada, tente novamente.')
        dependentes = int(input('Digite o número de dependentes do dependente de saúde: '))

    inss = calcular_inss(salarioB)
    irrf = calcular_irrf(salarioB, inss, dependentes)
    valeT = calcular_vt(salarioB, valeT)
    valeR = calcular_vr(valeR)
    dependente = calcular_plano_saude(dependentes)

    mostrar_contracheque(login, salarioB, inss, irrf, valeT, valeR, dependente)
    break