class Pessoa:

    def __init__(self, nome, cpf, datanasc, rg):

        self.__Nome = nome
        self.__CPF = cpf
        self.__Datanasc = datanasc
        self.__RG = rg


class Administrador(Pessoa):

    def __init__(self, nome, cpf, datanasc, rg):

        super().__init__(nome, cpf, datanasc, rg)

    def __init__(self, car, numma):

        self.__Cargo = car
        self.__nAdmin = numma


class Atendente (Pessoa):

    def __init__(self, nome, cpf, datanasc, rg):

        super().__init__(nome, cpf, datanasc, rg)

    def __init__ (self, )

class Aluno(Pessoa):

    def __init__(self, nome, cpf, datanasc,rg):

        super().__init__(nome, cpf, datanasc, rg)

    def __init__(self, numma, tur, sala):

        self.__nAluno = numma
        self.__turma = tur
        self.__sala = sala




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



class produto:
    def __init__(self, produto, valor, nome, codigo):

        self.__produto = produto
        self.__valor = valor
        self.__nome = nome
        self.__codigo = codigo

    def getproduto(self, produto):
        self.__produto = produto

    def valor(self, valor):
        self.__valor = valor

    def nome(self, nome):
        self.__nome = nome

    def codigo(self, codigo):
        self.__codigo = codigo