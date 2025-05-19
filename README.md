# Projeto API Restaurante

API desenvolvida em [FastAPI](https://fastapi.tiangolo.com/) para gerenciar usuários, pedidos e cardápio de um restaurante.

## Funcionalidades

- Cadastro e autenticação de usuários (JWT)
- Criação e listagem de pedidos
- Validação de endereço via OpenStreetMap
- Integração com MongoDB (async)

## Como rodar o projeto

1. **Clone o repositório**
   ```sh
   git clone <url-do-repo>
   cd app restaurante
   ```

2. **Configure o ambiente**
   - Crie um arquivo `.env` com as variáveis necessárias (veja exemplo abaixo).

3. **Instale as dependências**
   ```sh
   poetry install
   ```

4. **Execute a aplicação**
   ```sh
   poetry run uvicorn app.main:app --reload
   ```

5. **Acesse a documentação**
   - [http://localhost:8000/docs](http://localhost:8000/docs)

## Exemplo de `.env`

```
MONGO_USER=seu_usuario
MONGO_PASSWORD=sua_senha
MONGO_CLUSTER=seu_cluster
MONGO_DB_NAME=nome_do_banco
MONGO_APP_NAME=nome_app
JWT_SECRET_KEY=sua_chave_secreta
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30
USER_AGENT_NAME=SeuApp
USER_AGENT_CONTACT=seu@email.com
```

## Estrutura do Projeto

- `app/main.py`: Inicialização da API
- `app/routers/`: Rotas da API
- `app/models/`: Modelos Pydantic
- `app/crud/`: Operações com o banco de dados
- `app/utils/`: Utilitários (validação, autenticação, etc)
- `app/db/`: Conexão com o banco de dados
- `app/core/settings.py`: Configurações do projeto

---

Feito com ❤️ usando FastAPI e MongoDB.