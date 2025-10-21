FROM python:3.12-slim

WORKDIR /app

# Copiar arquivos de dependências primeiro (para cache)
COPY pyproject.toml uv.lock requirements.txt ./

# Instalar dependências com UV
RUN pip install uv && uv pip install --system -r pyproject.toml

# Copiar TODO o conteúdo, incluindo a pasta src
COPY . .

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

