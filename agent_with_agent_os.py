from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.valyu import ValyuTools
from agno.os import AgentOS

from dotenv import load_dotenv

load_dotenv()


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

agent_os = AgentOS(
    agents=[agent]
)

app = agent_os.get_app()
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
