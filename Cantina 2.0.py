class Pessoa:

    def __init__(self, nome, cpf, datanasc):

        self.__Nome = nome
        self.__CPF = cpf
        self.__Datanasc = datanasc


class Administrador(Pessoa):

    def __init__(self, nome, cpf, datanasc):

        super().__init__(nome, cpf, datanasc)

    def __init__(self, car, numma):

        self.__Cargo = car
        self.__nAdmin = numma


class Atendente (Pessoa):

    def __init__(self, nome, cpf, datanasc):

        super().__init__(nome, cpf, datanasc)

    def __init__ ()

class Aluno(Pessoa):

    def __init__(self, nome, cpf, datanasc):

        super().__init__(nome, cpf, datanasc)

    def __init__(self, numma, tur, sala):

        self.__nAluno = numma
        self.__turma = tur
        self.__sala = sala




""" class administrador:

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
      self.__horario = horario """
