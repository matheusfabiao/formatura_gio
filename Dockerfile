# Define a imagem base Python 3.12 slim
FROM python:3.12-slim-bookworm AS base

# Cria um estágio de construção baseado na imagem base
FROM base AS builder

# Copia o gerenciador de pacotes UV para o container
COPY --from=ghcr.io/astral-sh/uv:0.4.9 /uv /bin/uv

# Define variáveis de ambiente para otimizar o UV
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

# Define o diretório de trabalho como /app
WORKDIR /app

# Copia os arquivos de dependências do projeto
COPY uv.lock pyproject.toml /app/

# Sincroniza as dependências do projeto usando cache
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev

# Copia todo o código fonte para o container
COPY . /app

# Sincroniza novamente as dependências com o código completo
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# Inicia um novo estágio a partir da imagem base
FROM base

# Copia a aplicação construída do estágio anterior
COPY --from=builder /app /app

# Adiciona o diretório do ambiente virtual ao PATH
ENV PATH="/app/.venv/bin:$PATH"

# Expõe a porta 8000 para acesso externo
EXPOSE 8000

# Dá permissão de execução ao script de inicialização
RUN chmod +x /app/scripts/entrypoint.dev.sh

# Define o comando padrão para iniciar a aplicação
CMD ["/app/scripts/entrypoint.dev.sh"]