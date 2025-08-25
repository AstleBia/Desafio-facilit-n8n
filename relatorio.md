# **Relatório Técnico: Orquestração de IA com n8n para Análise de Dados**

## **1. Objetivo**

O objetivo deste projeto foi construir um sistema completo de IA
conversacional, utilizando o n8n como orquestrador principal. A solução
permite que um usuário envie uma pergunta em linguagem natural para um
workflow do n8n e receba uma resposta precisa, consultada diretamente de
um banco de dados populado com informações de planilhas.

## **2. Arquitetura da Solução**

A arquitetura do sistema foi projetada para ser modular e escalável,
utilizando containers Docker para orquestrar os diferentes serviços. A
solução é composta por:

-   **Banco de Dados PostgreSQL:** Um container Docker rodando uma
    instância do PostgreSQL para armazenar os dados dos eventos.

-   **API (Backend):** Uma API desenvolvida em Python com o framework
    FastAPI, que serve como uma camada de acesso para o banco de dados,
    executando operações de CRUD.
    Esta API também roda em seu próprio container Docker.

-   **n8n (Workflows):** Dois containers Docker, cada um rodando uma
    instância do n8n para separar as responsabilidades:

    1.  **Workflow de ETL:** Responsável pela migração de dados das
        planilhas Google Sheets para o banco de dados através da API.
    2.  **Workflow de Consulta com IA:** Atua como um agente de IA
        conversacional, recebendo perguntas via webhook e utilizando a
        API para consultar o banco de dados e gerar respostas6.

Essa arquitetura é gerenciada por um único arquivo\
docker-compose.yml, simplificando a configuração e a execução de todos
os serviços.

## **3. Detalhes da Implementação**

### **Etapa 1: Infraestrutura (Banco de Dados e API)**

A base do projeto foi a criação da infraestrutura para armazenamento e
acesso aos dados.

-   **Banco de Dados:** Foi configurado um serviço PostgreSQL em um
    container Docker. No momento da inicialização, um script (db-config.sql) é executado para criar as três tabelas necessárias:
    agenda_rh, agenda_marketing e agenda_ia, conforme especificado nas
    planilhas.

-   **API em Python (FastAPI):** Para interagir com o banco de dados,
    foi desenvolvida uma API RESTful utilizando FastAPI.

    -   **Models:** Foram definidos os modelos de dados (EventoRh,
        EventoMarketing, EventoIA) utilizando SQLModel, que mapeiam as
        tabelas do banco.
    -   **Routers:** Para cada tabela, foi criado um conjunto de
        endpoints que permitem as operações básicas de CRUD.
    -   **Conexão:** A conexão com o banco de dados PostgreSQL é
        gerenciada pelo database.py, que utiliza as variáveis de
        ambiente para configurar a URL de conexão.

### **Etapa 2: Workflow de Migração de Dados (ETL)**

O primeiro workflow do n8n (Workflow API.json) foi criado para
automatizar a extração de dados das planilhas e o carregamento no banco
de dados.

1.  **Gatilho Manual:** O workflow é iniciado manualmente, através de um
    botão na interface do n8n.

2.  **Leitura do Google Sheets:** Três nós do tipo "Google Sheets" foram
    configurados para ler os dados das planilhas "Agenda IA", "Agenda
    RH" e "Agenda Marketing".

3.  **Requisições HTTP:** Para cada linha lida das planilhas, o workflow
    faz uma requisição POST para a API correspondente (/eventos-ia,
    /eventos-rh, /eventos-marketing), enviando os dados para serem
    inseridos no banco.

### **Etapa 3: Workflow de Consulta com IA**

Este é o cérebro do projeto, um segundo workflow (workflow
consulta.json) que funciona como um agente de IA conversacional.

1.  **Webhook:** O workflow é acionado por um webhook, que aguarda
    requisições POST contendo uma pergunta em linguagem natural no
    formato {"pergunta": "Qual a data do evento X?"}.

2.  **Agente de IA:** O nó principal é um "AI Agent" conectado a um
    modelo de linguagem, especificamente o gpt-4.1-mini (escolhido pelo
    bom custo-benefício em comparação com outros modelos como o
    3.5-turbo).

3.  **Prompt e Ferramentas:** O agente foi instruído com um prompt
    detalhado para atuar como um assistente especializado em consultar
    eventos corporativos. Foram disponibilizadas três ferramentas para o
    agente:

    -   consultar_eventos_rh: Faz uma requisição GET para o endpoint
        /eventos-rh.
    -   consultar_eventos_marketing: Faz uma requisição GET para
        /eventos-marketing.
    -   consultar_eventos_ia: Faz uma requisição GET para /eventos-ia.

4.  **Lógica de Decisão:** O prompt instrui o agente a analisar a
    pergunta do usuário e decidir qual ferramenta usar. Se a pergunta
    for específica ("eventos de RH"), ele usa a ferramenta
    correspondente. Se for uma pergunta genérica, ele busca em todas as
    três categorias até encontrar o evento.

5.  **Formatação da Resposta:** O prompt também contém regras e exemplos
    para garantir que a resposta final seja em linguagem natural, direta
    e sem formatação de código, melhorando a experiência do
    usuário.

## **4. Como Configurar e Rodar o Projeto**

Siga os passos abaixo para executar a solução completa localmente.\
**Pré-requisitos:**

-   Docker e Docker Compose instalados.
-   Git instalado.

**Passos:**

1.  **Clonar o Repositório:**
    ```
    git clone https://github.com/AstleBia/Desafio-facilit-n8n.git
    cd Desafio-facilit-n8n
    ```

2.  Configurar Variáveis de Ambiente:\
    Crie um arquivo chamado .env na raiz do projeto. Este arquivo deve conter as credenciais do banco
    de dados. Adicione o seguinte conteúdo a ele, substituindo pelos
    valores desejados:\
    POSTGRES_USER=seu_usuario\
    POSTGRES_PASSWORD=sua_senha

3.  Iniciar os Serviços:\
    Execute o comando abaixo na raiz do projeto para construir as
    imagens e iniciar todos os containers (API, Banco de Dados e os
    dois n8n).\
    `
    docker-compose up --build
    `
4.  **Acessar os Serviços:**

    -   **API:** A documentação interativa da API estará disponível em
        http://localhost:8000/docs.
    -   **n8n (Workflow ETL):** Acesse em http://localhost:5678.
    -   **n8n (Workflow de Consulta):** Acesse em
        http://localhost:5679.

5.  **Executar os Workflows:**

    -   **Workflow ETL:** Abra a interface do n8n em
        http://localhost:5678, importe o arquivo Workflow API.json,
        configure suas credenciais do Google Sheets e execute-o
        manualmente para popular o banco de dados.
    -   **Workflow de Consulta:** Abra http://localhost:5679, importe o
        arquivo workflow consulta.json, configure suas credenciais da
        OpenAI e ative o workflow. Agora você pode enviar perguntas para
        o URL do webhook para interagir com o agente de IA.

## **5. Dificuldades Encontradas**

A maior dificuldade encontrada durante o desenvolvimento foi a
implementação dos workflows no n8n. Por ser o primeiro contato com a
ferramenta, foi necessário um tempo de aprendizado e pesquisa em
diversos recursos para entender seu funcionamento e aplicar a lógica
desejada de forma eficaz, especialmente na configuração do agente de IA
e suas ferramentas.

## **6. IAs Utilizadas como Auxílio**

Foram utilizadas ferramentas de IA para auxiliar no desenvolvimento, principalmente na
implementação dos workflows n8n. Os modelos utilizados foram:

-   **Claude Opus 4.1**
-   **Qwen 3-coder** 17
