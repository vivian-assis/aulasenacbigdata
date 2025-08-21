CREATE DATABASE ClinicasNara;

USE ClinicasNara;

CREATE TABLE clientes (
id INT PRIMARY KEY,
nome VARCHAR(100)); 

CREATE TABLE pedidos (id INT PRIMARY KEY,
cliente_id INT, FOREIGN KEY (cliente_id) REFERENCES
clientes(id));

INSERT INTO clientes (id, nome) VALUES
(10, "Naruto"),
(20, "Sasuke"),
(30, "Luffy"),
(40, "Zoro");

INSERT INTO pedidos (id, cliente_id) VALUES
(01, 10),
(02, 10),
(03, 40),
(04, 20),
(05, 40);

SELECT clientes.nome, pedidos.id
FROM clientes
INNER JOIN pedidos ON clientes.id = pedidos.cliente_id;

SELECT clientes.nome, pedidos.id
FROM clientes
LEFT JOIN pedidos ON clientes.id = pedidos.cliente_id;



