create database if not exists cantina;
use cantina;

#create schema DBPython;

create table if not exists turma (
idTurma int auto_increment not null,
horario time,
nomeTurma varchar (30),
primary key (idTurma)
);


 create table if not exists aluno (
idAluno int auto_increment not null,
idTurma int,
nome varchar (30),
turma varchar (20),
primary key (idAluno),
foreign key (idTurma) references turma(idTurma)
);
 
 create table if not exists pedido (
idPedido int auto_increment not null,
horario time,
numPedido varchar (15),
#peca varchar (25),
#casadinha varchar (25),
#suco varchar (25),
primary key (idPedido)
);
        
create table if not exists produto (
idProduto int auto_increment not null,
idPedido int,
preco varchar (15),
nomeProduto varchar (25),
primary key (idProduto),
foreign key (idPedido) references pedido(idPedido)
);

create table if not exists lucro (
IdLucro int auto_increment not null,
idPedido int,
valLucro varchar (25),
primary key (idLucro),
foreign key (idPedido) references pedido(idPedido)	
);

create table if not exists dados (
idBanco int auto_increment,
idPedido int,
primary key (idBanco),
foreign key (idPedido) references pedido(idPedido)
); 

select sum(preco) from produto; 