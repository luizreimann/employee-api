# Employee API

Esta é uma API de gerenciamento de funcionários construída com **FastAPI**, **PostgreSQL** e **Docker**.

## 📂 Estrutura do Projeto

```
employee_api/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── schemas.py
│   ├── main.py
│   ├── crud.py
│   ├── database.py
│   └── tests/
│       ├── __init__.py
│       ├── test_main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .env
```

## 🚀 Tecnologias Utilizadas
- **FastAPI**: Framework para construção da API
- **SQLAlchemy**: ORM para interação com o banco de dados
- **Pydantic**: Validação de dados
- **Uvicorn**: Servidor ASGI
- **pytest**: Testes unitários
- **PostgreSQL**: Banco de dados relacional
- **Docker**: Containerização

## 🔥 Como Executar o Projeto

### Pré-requisitos
- **Docker** instalado
- **Docker Compose** instalado

### Passo a Passo
1. **Clone o Repositório**
```bash
git clone https://github.com/seu-usuario/employee-api.git
cd employee-api
```

2. **Configure o Ambiente**
```bash
cp .env.example .env
```
Preencha o arquivo `.env` com as credenciais do banco de dados:
```env
DATABASE_URL=postgresql://user:password@db:5432/employee_db
```

3. **Suba os Containers**
```bash
docker-compose up --build
```

4. **Acesse a API**
- Documentação: [http://localhost:8000/docs](http://localhost:8000/docs)
- API Base: [http://localhost:8000](http://localhost:8000)

## 🧪 Executando Testes

Para rodar os testes unitários, execute o comando dentro do container:
```bash
docker exec -it employee_api pytest
```

## 🛠️ Rotas Disponíveis

- **Criar Funcionário**: `POST /employees/`
- **Listar Funcionários**: `GET /employees/`
- **Obter Funcionário por ID**: `GET /employees/{employee_id}`
- **Deletar Funcionário**: `DELETE /employees/{employee_id}`

## 🧑‍💻 Contribuição
Sinta-se à vontade para abrir **Issues** e **Pull Requests**.

## 📝 Licença
Este projeto está sob a licença **MIT**.