# Arquivo: default_agent.py
# Objetivo: criar um agente de pesquisa que usa DuckDuckGo e Valyu para
# buscar contextos na web e em artigos científicos, respondendo de forma
# concisa com fontes confiáveis. Requer variáveis no `.env`.
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.valyu import ValyuTools

# Carrega variáveis de ambiente do arquivo `.env` (ex.: GOOGLE_API_KEY, VALYU_API_KEY)
from dotenv import load_dotenv

load_dotenv()

# Configuração do agente:
# - `id` e `name`: identificação e nome amigável
# - `role`: descreve o objetivo do agente
# - `instructions`: diretrizes para buscar e apresentar informações
# - `model`: modelo Gemini a ser utilizado
# - `tools`: ferramentas de busca (internet e artigos científicos)
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
# Exemplo de uso: imprime uma resposta do agente para a pergunta informada
print(agent.print_response("Quais os principais artigos sobre redes neurais?"))
