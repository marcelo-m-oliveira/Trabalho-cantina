import time, datetime
import MySQLdb

con = MySQLdb.connect('localhost', 'root', '')
con.select_db('cantina')

cursor = con.cursor()
#res = int

print("######################### Sistema para cantina do SENAI #########################\n \n")
from datetime import datetime
lucro = 0
lucrotot = 0
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
    if now.hour > 20:
        print("espere a hora de seu intervalo")
    elif (now.hour >= 1 and now.minute >= 0) and (now.hour >= 1 and now.minute <= 59):

        print("Nome do aluno: ", a)
        print("Turma do aluno: ", tur, "\n")
        print("========================")
        print("     Cantina    ")
        print("========================")
        print("[1] - lanche R$ 2,50")
        print("[2] - suco R$ 1,50")
        print("[3] - casadinha R$ 4,00")
        print(" ")
        res = int(input("Opcao: "))

        if res == 1:
            print("[1] - coxinha")
            print("[2] - pastel")
            print("[3] - enrroladinho")
            lan = int(input("Opção: "))
            if lan == 1:
                print("Pegue sua coxinha. R$2,50")
                lucro = lucro + 2.50
                lucrotot = lucro + lucrotot
                print("o lucro total é: R$", lucrotot)

            elif lan == 2:
                print("Pegue seu pastel. R$2,50")
                lucro = lucro + 2.50
                lucrotot = lucro + lucrotot
                print("o lucro total é: R$", lucrotot)

            elif lan == 3:
                print("Pegue seu enroladinho. R$2,50")
                lucro = lucro + 2.50
                lucrotot = lucro + lucrotot
                print("o lucro total é: R$", lucrotot)

        if res == 2:
            print("[1] - Goiaba")
            print("[2] - Manga")
            suc = int(input("Opcao: "))
            if suc == 1:
                print("Pegue seu suco de goiaba. R$1,50")
                lucro = lucro + 1.50
                lucrotot = lucro + lucrotot
                print("o lucro total é: R$", lucrotot)

            elif suc == 2:
                print("Pegue seu suco de manga. R$1,50")
                lucro = lucro + 1.50
                lucrotot = lucro + lucrotot
                print("o lucro total é: R$", lucrotot)

        elif res == 3:
            while 2:
                print("Pegue o lanche e o suco de sua preferencia na cantina. R$4,00")
                lucro = lucro + 4.00
                lucrotot = lucro + lucrotot
                print("o lucro total é: R$", lucrotot)
                break

    elif now.hour >= 3:# and now.minute > 15:
        print("Já acabou o horário.")

if tur == 12345:
    if now.hour > 20:
        print("espere a hora de seu intervalo")
    elif (now.hour >= 1 and now.minute >= 0) and (now.hour >= 1 and now.minute <= 59):

        print("Nome do aluno: ", a)
        print("Turma do aluno: ", tur, "\n")
        print("========================")
        print("     Cantina    ")
        print("========================")
        print("[1] - lanche R$ 2,50")
        print("[2] - suco R$ 1,50")
        print("[3] - casadinha R$ 4,00")
        print(" ")
        res = int(input("Opcao: "))

        if res == 1:
            print("[1] - coxinha")
            print("[2] - pastel")
            print("[3] - enrroladinho")
            lan = int(input("Opção: "))
            if lan == 1:
                print("Pegue sua coxinha. R$2,50")
                lucro = lucro + 2.50
                lucrotot = lucro + lucrotot
                print("o lucro total é: R$", lucrotot)

            elif lan == 2:
                print("Pegue seu pastel. R$2,50")
                lucro = lucro + 2.50
                lucrotot = lucro + lucrotot
                print("o lucro total é: R$", lucrotot)

            elif lan == 3:
                print("Pegue seu enroladinho. R$2,50")
                lucro = lucro + 2.50
                lucrotot = lucro + lucrotot
                print("o lucro total é: R$", lucrotot)

        if res == 2:
            print("[1] - Goiaba")
            print("[2] - Manga")
            suc = int(input("Opcao: "))
            if suc == 1:
                print("Pegue seu suco de goiaba. R$1,50")
                lucro = lucro + 1.50
                lucrotot = lucro + lucrotot
                print("o lucro total é: R$", lucrotot)

            elif suc == 2:
                print("Pegue seu suco de manga. R$1,50")
                lucro = lucro + 1.50
                lucrotot = lucro + lucrotot
                print("o lucro total é: R$", lucrotot)

        elif res == 3:
            while 2:
                print("Pegue o lanche e o suco de sua preferencia na cantina. R$4,00")
                lucro = lucro + 4.00
                lucrotot = lucro + lucrotot
                print("o lucro total é: R$", lucrotot)
                break

    elif now.hour >= 3:# and now.minute > 15:
        print("Já acabou o horário.")

# INTEGRAÇÃO COM MYSQL ABAIXO ################################################

##############################################################################

################################### TURMA ###################################

date = time.strftime("%H:%M:%S")
#cursor.execute('insert into turma (horario, nomeTurma) values ("%s", "%s")' % (date, "54125"))
#cursor.execute('insert into turma (horario, nomeTurma) values ("%s", "%s")' % (date, "12345"))
cursor.execute('select idTurma from turma where nomeTurma = %s' % (tur))
selecao = cursor.fetchone()
#id = int(selecao[0])
cursor.execute('insert into turma (horario, nomeTurma) values ("%s", "%s")' % (date, (tur)))
con.commit()

##############################################################################

################################### ALUNO ###################################

cursor.execute('select idTurma from turma where nomeTurma = %s' % (tur))
selecao = cursor.fetchone()
id = int(selecao[0])
cursor.execute('insert into aluno (nome, turma,idTurma) values ("%s", "%d","%d")' % (a, tur, id))
con.commit()

##############################################################################

################################### PEDIDO ###################################

#peca = (res)
#casadinha = (res)
#suco = (res)
#pedido = (res)
date = time.strftime("%H:%M:%S")
pedido = res

cursor.execute('insert into pedido (horario, numPedido) values ("%s", %s)' % (date, pedido))
con.commit()


#############################################################################

################################### PRODUTO ###################################

#cursor.execute('select idPedido from pedido where numPedido = %s' % (res))
#selecao = cursor.fetchone()
#id = int(selecao[0])
#cursor.execute('insert into produto (preco, nomeProduto) values (%s, %s)' % (res, lan))
#con.commit()