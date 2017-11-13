import time, datetime
import MySQLdb
con = MySQLdb.connect('localhost', 'root', '')
con.select_db('cantina')

cursor = con.cursor()
date = time.strftime("%H")
cursor.execute('insert into turma (horario, nomeTurma) values ("%s", "%s")' % (date, "1010"))

print("######################### Sistema para cantina do SENAI #########################\n \n")
from datetime import datetime

aluno = []
now = datetime.now()
print(now.hour, ":", now.minute)
print(now.day, "/", now.month, "/", now.year)
turma = []
print("\n\nInforme a sua turma: ")
print("[54125] - informatica")
print("[12345] - redes")
tur = int(input("Opcao: "))
if tur == 54125:
    if now.hour <= 20:
        print("espere a hora de seu intervalo")
    elif (now.hour >= 20 and now.minute >= 1) and (now.hour >= 20 and now.minute <=16):

        a = input("\nInforme o seu nome: ")
        aluno.append(a)
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
    if now.hour >= 21:
        print("Já acabou o horário.")

elif tur == 12345:

    if (now.hour <= 19 and now.minute <= 45):
        print("espere a hora de seu intervalo")
    elif (now.hour >= 19 and now.minute >= 46) and now.hour < 20:
        a = input("\nInforme o seu nome: ")
        aluno.append(a)
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
    if now.hour >= 22:
        print("Já acabou o horário.")