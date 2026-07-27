import os

from dotenv import load_dotenv

from langchain_community.vectorstores import FAISS
from langchain_cohere import CohereEmbeddings, ChatCohere
from langchain_core.prompts import PromptTemplate


load_dotenv()


def cargar_vectorstore():

    embeddings = CohereEmbeddings(
        model="embed-multilingual-v3.0",
        cohere_api_key=os.getenv("COHERE_API_KEY")
    )

    base_vectorial = FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return base_vectorial



def preguntar_documento(pregunta):

    base_vectorial = cargar_vectorstore()


    documentos_encontrados = base_vectorial.similarity_search_with_score(
        pregunta,
        k=5
    )


    fragmentos = [
        documento
        for documento, score in documentos_encontrados
    ]


    contexto = "\n\n".join(
        fragmento.page_content
        for fragmento in fragmentos
    )


    prompt = PromptTemplate(
        template="""

Eres DocuMind AI, un asistente especializado en análisis documental.

Instrucciones:
- Utiliza solamente la información encontrada en el contexto.
- Explica las respuestas de manera clara.
- No agregues información externa.
- Si el documento no contiene la respuesta indica:
"No encuentro esa información en el documento."

CONTEXTO:
{contexto}

CONSULTA:
{pregunta}

RESPUESTA:
""",
        input_variables=[
            "contexto",
            "pregunta"
        ]
    )


    modelo = ChatCohere(
        model="command-r-plus-08-2024",
        cohere_api_key=os.getenv("COHERE_API_KEY")
    )


    respuesta = modelo.invoke(
        prompt.format(
            contexto=contexto,
            pregunta=pregunta
        )
    )


    return respuesta.content