################################################ LIGAÇÃO COM O MYSQL ###################################################

import time, datetime

import MySQLdb

con = MySQLdb.connect('localhost', 'root', '')
con.select_db('cantina')

cursor = con.cursor()
#res = int

########################################################################################################################

################################################ PARTE LOGICA DO CÓDIGO ################################################

print("######################### Sistema para cantina do SENAI #########################\n \n")
from datetime import datetime
#lucropec = 2.50
#lucrosuc = 1.50
#lucrocas = 4.00
#lucrotot = float
now = datetime.now()
print(now.hour, ":", now.minute)
print(now.day, "/", now.month, "/", now.year)
aluno = str
a = input("\nInforme o seu nome: ")
print("\n\nInforme a sua turma: ")
print("[54125] - informatica")
print("[12345] - redes")
tur = int(input("Opcao: "))



if tur == 54125:

    if now.hour > 0:
        print("espere a hora de seu intervalo")
    elif (now.hour >= 0 and now.minute >= 0) and (now.hour >= 0 and now.minute <= 59):

        print("Nome do aluno: ", a)
        print("Turma do aluno: ", tur, "\n")
        print("========================")
        print("     Cantina    ")
        print("========================")
        print("[1] - lanche R$ 2,50")
        print("[2] - suco R$ 1,50")
        print("[3] - casadinha R$ 4,00")
        print(" ")
        lan1 = str("Coxinha")
        lan2 = str("Pastel")
        lan3 = str("Enroladinho")
        suc1 = str("Suco de Goiaba")
        suc2 = str("Suco de Manga")
        cas = str("Peça + suco")
        preço1 = float(2.50)
        preço2 = float(1.50)
        preço3 = float(4.00)
        res = int(input("Opcao: "))

        if res == 1:
            print("[1] - coxinha")
            print("[2] - pastel")
            print("[3] - enrroladinho")
            lan = int(input("Opção: "))
            if lan == 1:
                print("Pegue sua ", lan1, ". R$2,50")

               #lucro1 = 2.50
               #lucrototpeça = []
               #lucrototpeça.append(lucro1)
               #print("o lucro total é: R$", lucrototpeça)

            elif lan == 2:
                print("Pegue seu ", lan2, ". R$2,50")
               #lucro1 = 2.50
               #lucrototpeça = []
               #lucrototpeça.append(lucro1)
               #print("o lucro total é: R$", lucrototpeça)

            elif lan == 3:
                print("Pegue seu ", lan3, ". R$2,50")
               #lucro1 = 2.50
               #lucrototpeça = []
               #lucrototpeça.append(lucro1)
               #print("o lucro total é: R$", lucrototpeça)



        if res == 2:
            print("[1] - Goiaba")
            print("[2] - Manga")
            suc = int(input("Opcao: "))
            if suc == 1:
                print("Pegue seu", suc1, ". R$1,50")
               #lucro2 = 1.50
               #lucrototsuco = []
               #lucrototsuco.append(lucro2)
               #print("o lucro total é: R$", lucrototsuco)

            elif suc == 2:
                print("Pegue seu", suc2, ". R$1,50")
               #lucro2 = 1.50
               #lucrototsuco = []
               #lucrototsuco.append(lucro2)
               #print("o lucro total é: R$", lucrototsuco)


        elif res == 3:
            while 2:
                print("Pegue o lanche e o suco de sua preferencia na cantina. R$4,00")
               #lucro3 = 4.00
               #lucrototcasadinha = []
               #lucrototcasadinha.append(lucro3)
               #print("o lucro total é: R$", lucrototcasadinha)
                break

    elif now.hour >= 3:# and now.minute > 15:
        print("Já acabou o horário.")


if tur == 12345:

    if now.hour == 3:
        print("espere a hora de seu intervalo")
    elif (now.hour >= 0 and now.minute >= 0) and (now.hour >= 0 and now.minute <= 59):

        print("Nome do aluno: ", a)
        print("Turma do aluno: ", tur, "\n")
        print("========================")
        print("     Cantina    ")
        print("========================")
        print("[1] - lanche R$ 2,50")
        print("[2] - suco R$ 1,50")
        print("[3] - casadinha R$ 4,00")
        print(" ")
        lan1 = str("Coxinha")
        lan2 = str("Pastel")
        lan3 = str("Enroladinho")
        suc1 = str("Suco de Goiaba")
        suc2 = str("Suco de Manga")
        cas = str("Peça + suco")
        preço1 = float(2.50)
        preço2 = float(1.50)
        preço3 = float(4.00)
        res = int(input("Opcao: "))

        if res == 1:
            print("[1] - coxinha")
            print("[2] - pastel")
            print("[3] - enrroladinho")
            lan = int(input("Opção: "))
            if lan == 1:
                print("Pegue sua ", lan1, ". R$2,50")

               #lucro1 = 2.50
               #lucrototpeça = []
               #lucrototpeça.append(lucro1)
               #print("o lucro total é: R$", lucrototpeça)

            elif lan == 2:
                print("Pegue seu ", lan2, ". R$2,50")
               #lucro1 = 2.50
               #lucrototpeça = []
               #lucrototpeça.append(lucro1)
               #print("o lucro total é: R$", lucrototpeça)

            elif lan == 3:
                print("Pegue seu ", lan3, ". R$2,50")
               #lucro1 = 2.50
               #lucrototpeça = []
               #lucrototpeça.append(lucro1)
               #print("o lucro total é: R$", lucrototpeça)



        if res == 2:
            print("[1] - Goiaba")
            print("[2] - Manga")
            suc = int(input("Opcao: "))
            if suc == 1:
                print("Pegue seu", suc1, ". R$1,50")
               #lucro2 = 1.50
               #lucrototsuco = []
               #lucrototsuco.append(lucro2)
               #print("o lucro total é: R$", lucrototsuco)

            elif suc == 2:
                print("Pegue seu", suc2, ". R$1,50")
               #lucro2 = 1.50
               #lucrototsuco = []
               #lucrototsuco.append(lucro2)
               #print("o lucro total é: R$", lucrototsuco)


        elif res == 3:
            while 2:
                print("Pegue o lanche e o suco de sua preferencia na cantina. R$4,00")
               #lucro3 = 4.00
               #lucrototcasadinha = []
               #lucrototcasadinha.append(lucro3)
               #print("o lucro total é: R$", lucrototcasadinha)
                break

    elif now.hour == 3:# and now.minute > 15:
        print("Já acabou o horário.")



################################################ INTEGRAÇÃO COM MYSQL ABAIXO ###########################################

######################################################### TURMA ########################################################

date = time.strftime("%H:%M:%S")
#cursor.execute('insert into turma (horario, nomeTurma) values ("%s", "%s")' % (date, "54125"))
#cursor.execute('insert into turma (horario, nomeTurma) values ("%s", "%s")' % (date, "12345"))
cursor.execute('select idTurma from turma where nomeTurma = %s' % (tur))
selecao = cursor.fetchone()
#id = int(selecao[0])
cursor.execute('insert into turma (horario, nomeTurma) values ("%s", "%s")' % (date, (tur)))
con.commit()

########################################################################################################################

######################################################### ALUNO ########################################################

cursor.execute('select idTurma from turma where nomeTurma = %s' % (tur))
selecao = cursor.fetchone()
id = int(selecao[0])
cursor.execute('insert into aluno (nome, turma,idTurma) values ("%s", "%d","%d")' % (a, tur, id))
con.commit()

########################################################################################################################

######################################################### PEDIDO #######################################################

#peca = (res)
#casadinha = (res)
#suco = (res)
#pedido = (res)
date = time.strftime("%H:%M:%S")
pedido = res

cursor.execute('insert into pedido (horario, numPedido) values ("%s", %s)' % (date, pedido))
con.commit()


########################################################################################################################

######################################################### PRODUTO ######################################################

cursor.execute('select idPedido from pedido where numPedido = %s' % (pedido))
selecao = cursor.fetchone()
id = int(selecao[0])

########################################################################################################################
############################################## LANCHES #################################################################

if res == 1:
    if lan == 1:
        cursor.execute('insert into produto (preco, nomeProduto) values ("%.2f", "%s")' % (preço1, lan1))
        con.commit()

    elif lan == 2:
        cursor.execute('insert into produto (preco, nomeProduto) values ("%.2f", "%s")' % (preço1, lan2))
        con.commit()

    elif lan == 3:
        cursor.execute('insert into produto (preco, nomeProduto) values ("%.2f", "%s")' % (preço1, lan3))
        con.commit()

########################################################################################################################
################################################ SUCOS #################################################################

if res == 2:
    if suc == 1:
        cursor.execute('insert into produto (preco, nomeProduto) values ("%.2f", "%s")' % (preço2, suc1))
        con.commit()

    elif suc == 2:
        cursor.execute('insert into produto (preco, nomeProduto) values ("%.2f", "%s")' % (preço2, suc2))
        con.commit()

########################################################################################################################
###################################################### CASADINHA #######################################################

if res == 3:
    cursor.execute('insert into produto (preco, nomeProduto) values ("%.2f", "%s")' % (preço3, cas))
    con.commit()

########################################################################################################################

######################################################## LUCRO #########################################################
cursor.execute('select sum(preco) from cantina.produto')
lista = []
#str(lista).strip('[]')

for luc in cursor.fetchall():
    lista.append(luc)
    print("Lucro total:", lista)
lucro = str(lista).strip('[]').strip('()')

cursor.execute('insert into lucro (valLucro) values ("%s")' % (lucro))
con.commit()


