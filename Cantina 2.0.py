from datetime import datetime
now = datetime.now()
print(now.hour, ":", now.minute)
print(now.day, "/", now.month, "/", now.year)

class administrador:

    def __init__(self, cadastAluno, cadastSala, cadastTurma, cadastHorario):
        self.__aluno = cadastAluno
        self.__sala = cadastSala
        self.__turma = cadastTurma
        self.__horario = cadastHorario

    