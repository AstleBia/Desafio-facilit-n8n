# Orquestração de IA com n8n para Análise de Dados

## Visão Geral
Este projeto é uma **Prova de Conceito (PoC)** que demonstra como o **n8n** pode orquestrar fluxos de dados e servir como motor de uma aplicação de **IA conversacional**.  

O sistema permite que o usuário faça perguntas em linguagem natural via um **webhook no n8n**, que por sua vez consulta um **banco de dados PostgreSQL** (alimentado a partir de planilhas do Google Sheets) e retorna uma resposta processada por IA.

---

## Arquitetura
A solução foi projetada para ser **modular e escalável**, utilizando **Docker** para orquestrar os serviços:

- **PostgreSQL (DB):** Contêiner para armazenar os dados migrados das planilhas.  
- **API (FastAPI):** Backend em Python para expor operações de CRUD no banco.  
- **n8n (Workflows):**
  - **ETL Workflow:** Lê dados de planilhas no Google Sheets e popula o banco via API.  
  - **IA Workflow:** Recebe perguntas em linguagem natural via webhook, consulta os dados e retorna respostas processadas por IA.  

---

## Como Rodar o Projeto

### 1. Clonar o Repositório
```bash
git clone https://github.com/AstleBia/Desafio-facilit-n8n.git
cd Desafio-facilit-n8n
```

### 2. Subir os Contêineres
É necessário ter **Docker** e **Docker Compose** instalados.
```bash
docker-compose up -d --build
```

### 3. Configurar o n8n
- Importe o workflow `workflow api.json` (responsável pela migração dos dados).  
- Importe o workflow `workflow consulta.json` (responsável pela consulta com IA).  

---

## Exemplos de Uso
- Enviar uma pergunta para o webhook:
```json
{"pergunta": "Qual o período do evento X?"}
```

- Resposta esperada:
```json
{"resposta": "O período é de Y a Z"}
```

---

## 📝 Relatório Técnico
O relatório completo com **arquitetura, decisões técnicas e dificuldades enfrentadas** está disponível em [`relatorio.md`](./relatorio.md).

---
