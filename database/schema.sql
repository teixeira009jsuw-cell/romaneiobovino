-- ==========================
-- BANCO DE DADOS
-- Romaneio Bovino
-- ==========================

CREATE TABLE fazenda (
    id_fazenda INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    proprietario TEXT NOT NULL,
    municipio TEXT NOT NULL
);

CREATE TABLE lote (
    id_lote INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo_lote TEXT NOT NULL UNIQUE,
    id_fazenda INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    FOREIGN KEY (id_fazenda) REFERENCES fazenda(id_fazenda)
);

CREATE TABLE animal (
    id_animal INTEGER PRIMARY KEY AUTOINCREMENT,
    brinco TEXT NOT NULL UNIQUE,
    sexo TEXT NOT NULL,
    peso REAL NOT NULL,
    raca TEXT,
    id_lote INTEGER NOT NULL,
    FOREIGN KEY (id_lote) REFERENCES lote(id_lote)
);

CREATE TABLE romaneio (
    id_romaneio INTEGER PRIMARY KEY AUTOINCREMENT,
    data_romaneio DATE NOT NULL,
    destino TEXT NOT NULL,
    motorista TEXT,
    id_lote INTEGER NOT NULL,
    FOREIGN KEY (id_lote) REFERENCES lote(id_lote)
);