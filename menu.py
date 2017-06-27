#coding: utf-8
from equipe import equipe
instancia = equipe('DLEI')

while True:
    print '1- Adicionar aluno'
    print '2- Remover aluno'
    print '3- mostar '
    print '4- Sair'

    op = int(raw_input("\nDigite a opçao desejada: "))

    if op == 1:
        while True:
            aluno1 = raw_input('\nDigite o nome do aluno: ')
            cpf = int(raw_input('Digite o CPF do aluno'))
            instancia.cadastrar(aluno1,cpf)
            o = raw_input("\nDeseja cadastrar outro aluno? ")
            if o.upper() == "SIM":
                continue
            else:
                break

    elif op == 2:
        while True:
            remover = int(raw_input("\nDigite o CPF do aluno que você deseja remover: "))
            instancia.remover(remover)
            o2 = raw_input("\nDeseja remover outro aluno? ")
            if o2.upper() == "SIM":
                continue
            else:
                break
    elif op == 3:
        while True:
            instancia.mostrar()
            o3 = raw_input("\nDeseja verificar novamente? ")
            if o.upper() == "SIM":
                continue
            else:
                break
    elif op == 4:
        print "Obrigado!!!"
        print "\nTCHAU"
        break