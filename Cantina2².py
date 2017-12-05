from Cantina2 import time, Pessoa, Administrador, Produto, Atendente, Aluno

tempo = time()
tempo.imprimeTime()

cadastro = Pessoa("nome", "cpf", "datanasc", "rg")
cadastro.inserir()

