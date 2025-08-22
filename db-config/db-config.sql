CREATE TYPE status as ENUM (
    "Não iniciado",
    "Em andamento",
    "Concluído"
)

CREATE TABLE IF NOT EXISTS agenda_rh (
    id SERIAL PRIMARY KEY,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    evento VARCHAR(100) NOT NULL,
    descricao TEXT NOT NULL,
    alcance INTEGER NOT NULL,
    status status NOT NULL
)

CREATE TABLE IF NOT EXISTS agenda_marketing (
    id SERIAL PRIMARY KEY,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    evento VARCHAR(100) NOT NULL,
    descricao TEXT NOT NULL,
    status status NOT NULL
)

CREATE TABLE IF NOT EXISTS agenda_rh (
    id SERIAL PRIMARY KEY,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    evento VARCHAR(100) NOT NULL,
    descricao TEXT NOT NULL,
    engajamento INTEGER NOT NULL,
    status status NOT NULL
)