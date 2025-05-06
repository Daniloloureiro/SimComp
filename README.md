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
