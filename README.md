# O Que Você Gostaria de Ser?

Jogo educativo em português feito com Python e Streamlit. A criança informa como gostaria de ser chamada, escolhe uma área e uma profissão e recebe uma apresentação personalizada, atividades da carreira e uma curiosidade.

## Requisitos

- Python 3.13 ou superior
- pip

## Como executar

1. Descompacte o arquivo ZIP.
2. Abra um terminal na pasta descompactada.
3. Crie e ative um ambiente virtual (opcional, mas recomendado):

   Linux/macOS:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   Windows (PowerShell):
   ```powershell
   py -3.13 -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

4. Instale o Streamlit:
   ```bash
   python -m pip install -r requirements.txt
   ```

5. Inicie o jogo:
   ```bash
   streamlit run main.py
   ```

O Streamlit abrirá o endereço local indicado no terminal.

## Arquivos

- `main.py`: código completo do jogo e catálogo de 35 profissões em sete áreas.
- `requirements.txt`: dependência necessária para instalação com pip.
- `pyproject.toml` e `uv.lock`: configuração e dependências travadas para quem usa uv.
