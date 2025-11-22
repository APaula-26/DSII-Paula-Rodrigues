create database Amargo;

USE Amargo;

-- Tabela Vendedores
CREATE TABLE Vendedores (
  IDVendedor INT AUTO_INCREMENT PRIMARY KEY,
  Nome VARCHAR(50)
);

-- Tabela Produtos
CREATE TABLE Produtos (
  IDProduto INT AUTO_INCREMENT PRIMARY KEY,
  Produto VARCHAR(100),
  Preco DECIMAL(10,2)
);

-- Tabela Clientes
CREATE TABLE Clientes (
  IDCliente INT AUTO_INCREMENT PRIMARY KEY,
  Cliente VARCHAR(50),
  Estado VARCHAR(2),
  Sexo CHAR(1),
  Status VARCHAR(50)
);

-- Tabela Vendas
CREATE TABLE Vendas (
  IDVenda INT AUTO_INCREMENT PRIMARY KEY,
  IDVendedor INT,
  IDCliente INT,
  Data DATE,
  Total DECIMAL(10,2),
  FOREIGN KEY (IDVendedor) REFERENCES Vendedores(IDVendedor),
  FOREIGN KEY (IDCliente) REFERENCES Clientes(IDCliente)
);

-- Tabela ItensVenda
CREATE TABLE ItensVenda (
  IDProduto INT,
  IDVenda INT,
  Quantidade INT,
  ValorUnitario DECIMAL(10,2),
  ValorTotal DECIMAL(10,2),
  Desconto DECIMAL(10,2),
  PRIMARY KEY (IDProduto, IDVenda),
  FOREIGN KEY (IDProduto) REFERENCES Produtos(IDProduto) ON DELETE RESTRICT,
  FOREIGN KEY (IDVenda) REFERENCES Vendas(IDVenda) ON DELETE CASCADE
);
