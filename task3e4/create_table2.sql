CREATE TABLE operadoras_saude (
    Registro_ANS VARCHAR(10) PRIMARY KEY,
    CNPJ VARCHAR(14) NOT NULL,
    Razao_Social VARCHAR(255) NOT NULL,
    Nome_Fantasia VARCHAR(255),  -- Pode ser NULL (155 valores nulos)
    Modalidade VARCHAR(100) NOT NULL,
    Logradouro VARCHAR(255) NOT NULL,
    Numero VARCHAR(10) NOT NULL,
    Complemento VARCHAR(100),  -- Pode ser NULL (560 valores nulos)
    Bairro VARCHAR(100) NOT NULL,
    Cidade VARCHAR(100) NOT NULL,
    UF CHAR(2) NOT NULL,
    CEP CHAR(8) NOT NULL,
    DDD CHAR(2),  -- Pode ser NULL (109 valores nulos)
    Telefone VARCHAR(15),  -- Pode ser NULL (107 valores nulos)
    Fax VARCHAR(15),  -- Pode ser NULL (597 valores nulos)
    Endereco_eletronico VARCHAR(255),  -- Pode ser NULL (2 valores nulos)
    Representante VARCHAR(255) NOT NULL,
    Cargo_Representante VARCHAR(100) NOT NULL,
    Regiao_de_Comercializacao INT,  -- Pode ser NULL (128 valores nulos)
    Data_Registro_ANS DATE NOT NULL
);
