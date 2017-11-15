import time, datetime
import MySQLdb

con = MySQLdb.connect('localhost', 'root', '')
con.select_db('cantina')

cursor = con.cursor()
res = int

print("######################### Sistema para cantina do SENAI #########################\n \n")

from datetime import datetime

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
    if now.hour < 20:
        print("espere a hora de seu intervalo")
    elif (now.hour == 20 and now.minute >= 30) and (now.hour == 20 and now.minute <= 59):

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
            lan = int(input("Opcao: "))
            if lan == 1:
                print("Pegue sua coxinha. R$2,50")
            elif lan == 2:
                print("Pegue seu pastel. R$2,50")
            elif lan == 3:
                print("Pegue seu enroladinho. R$2,50")
        if res == 2:
            print("[1] - Goiaba")
            print("[2] - Manga")
            suc = int(input("Opcao: "))
            if suc == 1:
                print("Pegue seu suco de goiaba. R$1,50")
            elif suc == 2:
                print("Pegue seu suco de manga. R$1,50")


        elif res == 3:
            while 2:
                print("Pegue o lanche e o suco de sua preferencia na cantina. R$4,00")
                break

    elif now.hour >= 23:  # and now.minute > 15:
        print("Já acabou o horário.")

elif tur == 12345:

    if (now.hour < 21):

        print("espere a hora de seu intervalo")
    elif (now.hour == 21 and now.minute >= 0) and (now.hour == 21 and now.minute < 16):
        print("Nome do aluno: ", a)
        print("Turma do aluno: ", tur, "\n")
        print("Numero do aluno: ", a, "\n")
        print("========================")
        print("     Cantina    ")
        print("========================")
        print("[1] - lanche R$ 3,00")
        print("[2] - suco R$ 1,50")
        print("[3] - casadinha R$ 4,00")
        print(" ")
        res = int(input("Opcao: "))

        if res == 1:
            print("[1] - coxinha")
            print("[2] - pastel")
            print("[3] - enrroladinho")
            lan = int(input("Opcao: "))
            if lan == 1:
                print("Pegue sua coxinha")
            elif lan == 2:
                print("Pegue seu pastel")
            elif lan == 3:
                print("Pegue seu enroladinho")
        if res == 2:
            print("[1] - Goiaba")
            print("[2] - Manga")
            suc = int(input("Opcao: "))
            if suc == 1:
                print("Pegue seu suco a goiaba")
            elif suc == 2:
                print("Pegue seu suco de manga")


        elif res == 3:
            while 2:
                print("[1] - Pegue o lanche e o suco de sua preferencia na cantina.")
                break
    if now.hour > 21 and now.minute > 16:
        print("Já acabou o horário.")

# INTEGRAÇÃO COM MYSQL ABAIXO

################################### TURMA ###################################

date = time.strftime("%H:%M:%S")
cursor.execute('select idTurma from turma where nomeTurma = %s' % (tur))
selecao = cursor.fetchone()
cursor.execute('insert into turma (horario, nomeTurma) values ("%s", "%s")' % (date, (tur)))
con.commit()
#############################################################################

################################### ALUNO ###################################

cursor.execute('select idTurma from turma where nomeTurma = %s' % (tur))
selecao = cursor.fetchone()
id = int(selecao[0])
cursor.execute('insert into aluno (nome, turma,idTurma) values ("%s", "%d","%d")' % (a, tur, id))
con.commit()

##############################################################################

################################### PEDIDO ###################################

peca = (lan)
casadinha = (lan)
suco = (suc)

cursor.execute('insert into pedido (horario, peca, suco, casadinha) values ("%s", "%s", "%s", "%s")' % (
date, peca, suco, casadinha))
con.commit()

#############################################################################

################################### PRODUTO ###################################

cursor.execute('select idPedido from pedido where nomePedido = %s' % (res))
selecao = cursor.fetchone()
id = int(selecao[0])
cursor.execute('insert into produto (preco, nomeProduto) values (%s, %s)' % (res, lan or suc))
con.commit()