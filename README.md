# Agent-With-Tools-Using-Agno-Framework

Projeto de exemplo usando o Agno Framework para criar um agente de pesquisa que:
- Consulta a web via `DuckDuckGoTools` e artigos científicos via `ValyuTools`.
- Usa o modelo `Gemini` para gerar respostas concisas com fontes confiáveis.
- Pode ser executado como script (`default_agent.py`) ou exposto como API FastAPI via `AgentOS` (`agent_with_agent_os.py`).

## Estrutura
- `default_agent.py`: instancia o agente e imprime uma resposta para uma pergunta exemplo.
- `agent_with_agent_os.py`: expõe o agente como uma aplicação FastAPI usando `AgentOS`.
- `.env.example`: variáveis necessárias (chaves das APIs Google e Valyu).

## Pré-requisitos
- Python 3.10+
- Chave `GOOGLE_API_KEY` (Google Gemini)
- Chave `VALYU_API_KEY` (Valyu)

## Instalação e Execução
1. Crie e ative um ambiente virtual (opcional, recomendado):
   - Windows: `python -m venv .venv` e `.\.venv\Scripts\activate`
2. Instale as dependências:
   - `pip install -r requirements.txt`
3. Configure suas variáveis de ambiente:
   - Copie `.env.example` para `.env`
   - Preencha `GOOGLE_API_KEY` e `VALYU_API_KEY`
4. Execute como script (resposta direta no terminal):
   - `python default_agent.py`
5. Execute como API (FastAPI + Uvicorn):
   - `python agent_with_agent_os.py`
   - Acesse `http://127.0.0.1:8000` (docs interativas em `http://127.0.0.1:8000/docs`)
