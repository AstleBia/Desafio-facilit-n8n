
CREATE TABLE IF NOT EXISTS agenda_rh (
    id SERIAL PRIMARY KEY,
    data_anual VARCHAR(50) NOT NULL,
    evento VARCHAR(100) NOT NULL,
    descricao TEXT NOT NULL,
    alcance INTEGER NOT NULL,
    status VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS agenda_marketing (
    id SERIAL PRIMARY KEY,
    data_anual VARCHAR(50) NOT NULL,
    evento VARCHAR(100) NOT NULL,
    descricao TEXT NOT NULL,
    status VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS agenda_ia (
    id SERIAL PRIMARY KEY,
    data_anual VARCHAR(50) NOT NULL,
    evento VARCHAR(100) NOT NULL,
    descricao TEXT NOT NULL,
    engajamento INTEGER NOT NULL,
    status VARCHAR(50) NOT NULL
);