CREATE DATABASE webstore;
 
USE webstore;
 
CREATE TABLE clientes(
	id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    telefone VARCHAR(20) NULL,
    cidade VARCHAR(80) NOT NULL,
    estado CHAR(2) NOT NULL,
    data_cadastro DATE NOT NULL
    ) 
    ENGINE = InnoDB;
CREATE TABLE categorias(
	id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(80) NOT NULL UNIQUE
)ENGINE = InnoDB;
 
 
CREATE TABLE produtos(
	id_produto INT AUTO_INCREMENT PRIMARY KEY,
    id_categoria INT NOT NULL,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2) NOT NULL CHECK(preco > 0),
    estoque INT NOT NULL CHECK(estoque >= 0),
    FOREIGN KEY (id_categoria)  REFERENCES categorias(id_categoria)
)ENGINE = InnoDB;
 
CREATE TABLE vendedores(
	id_vendedor INT AUTO_INCREMENT PRIMARY KEY,
    nome varchar(100) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE
)ENGINE InnoDB;
 
ALTER TABLE pedidos 
RENAME COLUMN id_vendedores TO id_vendedor;
 
 
CREATE TABLE pedidos(
	id_pedido INT  AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_vendedor INT NOT NULL,
    data_pedido DATETIME NOT NULL,
    status ENUM('PENDENTE', 'PAGO', 'CANCELADO') NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_vendedor) REFERENCES vendedores(id_vendedor)
)ENGINE = InnoDB;
 
CREATE TABLE itens_pedidos(
	id_item INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT NOT NULL,
    id_produto INT NOT NULL,
    quantidade INT NOT NULL CHECK(quantidade > 0),
    preco_unitario DECIMAL (10,2) NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
    FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
)ENGINE = InnoDB;

SELECT * FROM webstore