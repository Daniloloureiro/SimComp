# SimROEL - Simulador de Redes Ópticas Elásticas

![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

Simulador de redes ópticas elásticas desenvolvido em Python para análise e alocação de espectro.

## 📋 Pré-requisitos

- Python 3.12 (exigido)
- pip (gerenciador de pacotes)
- Git (para clonar o repositório)

## 🛠️ Configuração do Ambiente

### 1. Clonar o repositório
```bash
git clone https://github.com/Daniloloureiro/SimComp.git
cd SimComp
```

### 2. Criar ambiente virtual
Linux/macOS
```bash
python3.12 -m venv venv
source venv/bin/activate
```

Windows
```powershell
python -m venv venv
.\venv\Scripts\activate
```

### 3. Instalar dependências
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. 🚀 Execução
```bash
python simroel.py
```

### 5. Configuração com pyenv (Recomendado)

Se você estiver usando pyenv para gerenciar versões do Python, siga estas instruções:

1. Instalar Python 3.12 via pyenv:
```bash
pyenv install 3.12.10
```

2. Criar um ambiente virtual para o projeto:
```bash
pyenv virtualenv 3.12.10 simroel-env
```

3. Configurar o ambiente virtual para o projeto:
```bash
pyenv local simroel-env
```

4. Instalar as dependências:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### Como usar o ambiente:

- O ambiente será ativado automaticamente quando você entrar no diretório do projeto
- Para ativar manualmente o ambiente:
```bash
pyenv activate simroel-env
```
- Para desativar o ambiente:
```bash
pyenv deactivate
```

#### Verificando a instalação:

Para confirmar que está tudo configurado corretamente, execute:
```bash
python --version  # Deve mostrar Python 3.12.x
which python     # Deve mostrar o caminho do Python no ambiente virtual
```

## 🐛 Solução de Problemas

Erro de versão do Python:

Linux:
```bash
# Ubuntu/Debian
sudo apt install python3.12
```

Windows (via Chocolatey):
```powershell
choco install python --version=3.12.0
```

Dependências faltando:
```bash
pip install --force-reinstall -r requirements.txt
```
