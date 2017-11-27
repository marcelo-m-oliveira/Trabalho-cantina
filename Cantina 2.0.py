class administrador:

    def __init__(self, cadastAluno, cadastSala, cadastTurma, cadastHorario):
        self.__aluno = cadastAluno
        self.__sala = cadastSala
        self.__turma = cadastTurma
        self.__horario = cadastHorario

    def horario(self):
        from datetime import datetime
        now = datetime.now()
        print(now.hour, ":", now.minute)
        print(now.day, "/", now.month, "/", now.year),

    def cadastroA(self, aluno):
        self.__aluno = aluno

    def cadastroS(self, sala):
        self.__sala = sala

    def cadastroT(self, turma):
        self.__turma = turma

    def cadastroH(self, horario):
        self.__horario = horario