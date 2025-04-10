# 🎓 Formatura Giovanna Urquisa - Sistema de Confirmação de Presença

[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![Django](https://img.shields.io/badge/django-5.2-green.svg)](https://www.djangoproject.com/)
[![Docker](https://img.shields.io/badge/docker-compose-blue.svg)](https://docs.docker.com/compose/)
[![Code style: Ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)

Sistema web desenvolvido para gerenciar confirmações de presença e apresentar informações sobre a formatura de Giovanna Urquisa.

## 📋 Requisitos

- Python 3.12 ou superior
- Docker e Docker Compose
- UV Package Manager

## 🛠️ Tecnologias Principais

- Django 5.2
- Django Vite 3.1.0
- Pillow 11.1.0
- Ruff (linting e formatação)
- Pytest (testes)

## 🚀 Instalação e Execução

### Usando Docker (Recomendado)

1. Clone o repositório
2. Copie o arquivo de ambiente:
   ```bash
   cp env_files/.env.example env_files/.env
   ```
3. Execute o projeto:
   ```bash
   task build   # Primeira execução
   # ou
   task up      # Execuções subsequentes
   ```

O sistema estará disponível em `http://localhost:8000`

### Comandos Disponíveis

- `task lint`: Executa verificação de código
- `task format`: Formata o código
- `task up`: Inicia os containers
- `task up-d`: Inicia os containers em modo daemon
- `task down`: Para e remove os containers
- `task stop`: Para os containers
- `task restart`: Reinicia os containers
- `task app nome_app`: Cria um novo app Django
- `task makemigrations`: Gera migrações do banco de dados

## 🧪 Testes

O projeto utiliza Pytest para testes. As configurações incluem:
- Arquivos de teste devem seguir o padrão: `test*.py`, `*_test.py` ou `test_*.py`
- Localização dos testes: diretório `src`

## 📝 Padrões de Código

Utilizamos Ruff para linting e formatação com as seguintes configurações:
- Comprimento máximo de linha: 79 caracteres
- Seleção de regras: I, F, E, W, PL, PT
- Estilo de aspas: simples

## 🏗️ Estrutura do Projeto

```
├── env_files/          # Arquivos de ambiente
├── scripts/            # Scripts de execução
├── src/                # Código fonte
│   ├── core/           # Configurações principais
│   ├── static/         # Arquivos estáticos
│   └── templates/      # Templates HTML
├── Dockerfile          # Configuração Docker
├── docker-compose.yml  # Configuração Docker Compose
└── pyproject.toml      # Configuração do projeto
```

## 🤝 Contribuição

1. Faça o fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Faça commit das mudanças (`git commit -m 'Adiciona nova feature'`)
4. Faça push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.