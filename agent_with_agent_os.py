# Arquivo: agent_with_agent_os.py
# Objetivo: expor o agente de pesquisa via uma aplicação FastAPI
# utilizando o `AgentOS`, permitindo servir o agente como API/web app.
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.valyu import ValyuTools
from agno.os import AgentOS

# Carrega variáveis de ambiente do arquivo `.env`
from dotenv import load_dotenv

load_dotenv()

# Definição do agente de pesquisa (mesma ideia do `default_agent.py`):
# inclui identidade, papel, instruções, modelo Gemini e ferramentas.
agent = Agent(
    id="Agente de pesquisa",
    name="Pesquisador DDG",
    role="Responda perguntas baseadas em contextos buscados na internet e em artigos científicos",
    instructions=[
        "Busque as principais fontes confiáveis sobre o tema.",
        "Entregue uma saída concisa com: 5-10 fatos em bullets e um quadro de fontes com título + URL.",
        "Não invente links. Priorize sites oficiais, artigos e referências robustas.",
        "Use a ValyuTools para busca em artigos e DuckDuckGoTools para buscas na internet."
    ],
    model=Gemini(
        id="gemini-2.5-flash-lite",
    ),
    tools=[
        DuckDuckGoTools(),
        ValyuTools(),
    ]
)
# Inicializa o `AgentOS` com a lista de agentes disponíveis.
agent_os = AgentOS(
    agents=[agent]
)
# Obtém a aplicação FastAPI para servir o agente.
app = agent_os.get_app()
if __name__ == "__main__":
    import uvicorn
    # Executa o servidor local: acesse `http://127.0.0.1:8000`
    uvicorn.run(app, host="127.0.0.1", port=8000)
