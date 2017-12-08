from datetime import datetime

import MySQLdb

con = MySQLdb.connect('localhost', 'root', '')
con.select_db('cantina')

cursor = con.cursor()


class time:
    #pra que essa classe? o horário só é necessário na classe principal para limitar o horário e
    #cadastrar o pedido
    def imprimeTime(self):

        now = datetime.now()
        print(now.hour, ":", now.minute)
        print(now.day, "/", now.month, "/", now.year)

    #def barrarhorario(self):



class Pessoa:

    def __init__(self, nome, cpf, datanasc, rg):

        self.__Nome = nome
        self.__CPF = cpf
        self.__Datanasc = datanasc
        self.__RG = rg

    def inserir(self):

        nome = input("Insira seu nome:\n")
        turma = input("\nInsira sua turma: \n")
        date = time


        cursor.execute('select idTurma from turma where nomeTurma = %s' % (turma))
        selecao = cursor.fetchone()
        cursor.execute('insert into turma (horario, nomeTurma) values ("%s", "%s")' % (date, (turma)))
        con.commit()

class Administrador(Pessoa):

    def __init__(self, nome, cpf, datanasc, rg, car, numma):

        super().__init__(nome, cpf, datanasc, rg)
        self.__Cargo = car
        self.__nAdmin = numma

    def cadastraAluno(self):
        #SQL de cadastro
    def cadastraTurma(self):
        #SQL de cadastro de turma
        #aqui talvez na Tabela turma tenha a sala
    def cadastraSala(self):
        #SQL de cadastro de sala
        #Aqui talvez na tabela sala tenha o horário de intervalo


class pedido:

    def __init__(self, numpedido, valorpedido, produto):

        self.__numero = numpedido
        self.__valor = valorpedido
        self.__produto = produto

class Produto:

    def __init__(self, produto, valor, nome, codigo):

        self.__produto = produto
        self.__valor = valor
        self.__nomeProd = nome
        self.__codigo = codigo

    def cadasProduto (self, produto, valor, nome, codigo):

        self.__produto = produto
        self.__valor = valor
        self.__nomeProd = nome
        self.__codigo = codigo

    def produto(self, produto):

        self.__produto = produto

    def valor(self, valor):

        self.__valor = valor

    def nome(self, nome):

        self.__nome = nome

    def codigo(self, codigo):

        self.__codigo = codigo

    def mostrarProduto (self):

         print("Código do produto: " +str (self.__produto)
            + "O valor do produto é: " +str (self.__valor)
            + "O nome do produto é: " +str (self.__nomeProd)
            + "O seu produto é : " +str (self.__codigo))

class Atendente (Pessoa):

    def __init__(self, nome, cpf, datanasc, rg):

        super().__init__(nome, cpf, datanasc, rg)


    def cadasProduto (self, cadasProduto, produto):

        produto.Produto(cadasProduto)

    def cadasProd (self, prod):

        self.__prod = prod

    def verLucro(self, lucro):

        self.__lucro = lucro


class Aluno(Pessoa):

    def __init__(self, nome, cpf, datanasc,rg):

        super().__init__(nome, cpf, datanasc, rg)

    def __init__(self, numma, tur, sala):

        self.__nAluno = numma
        self.__turma = tur
        self.__sala = sala

    def pedido(self, pedido):

        self.__pedido = pedido

    def verCardapio(self, cardapio):

        self.__cardapio = cardapio


class sala:

   def __init__(self, nome, horaintervalo, turma):

       self.__nome = nome
       self.__horaint = horaintervalo
       self.__turma = turma

   def criarsala(self, numero, horaintervalo):

        self.__numsala = numero
        self.__horaint = horaintervalo




"""" class administrador:

  def __init__(self, cadastAluno, cadastSala, cadastTurma, cadastHorario):
      self.__aluno = cadastAluno
      self.__sala = cadastSala
      self.__turma = cadastTurma
      self.__horario = cadastHorario

  def horario(self):
      from datetime import datetime
      now = datetime.now()
      print(now.hour, ":", now.minute)

  def cadastroA(self, aluno):
      self.__aluno = aluno

  def cadastroS(self, sala):
      self.__sala = sala
      print(now.day, "/", now.month, "/", now.year),

  def cadastroT(self, turma):
      self.__turma = turma

  def cadastroH(self, horario):
      self.__horario = horario """


