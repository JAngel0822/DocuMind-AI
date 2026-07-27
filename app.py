import streamlit as st

from src.loader import PDFLoader
from src.embeddings import crear_vectorstore
from src.chatbot import preguntar_documento


st.set_page_config(
    page_title="DocuMind AI",
    page_icon="🧠",
    layout="centered"
)


st.title("🧠 DocuMind AI")

st.markdown(
    """
    ### Asistente inteligente de documentos

    Carga un documento PDF y realiza preguntas.
    El agente analizará la información usando inteligencia artificial.
    """
)


st.divider()


archivo = st.file_uploader(
    "📄 Selecciona un documento PDF",
    type="pdf"
)


if archivo:

    with open(
        "data/documento.pdf",
        "wb"
    ) as f:
        f.write(
            archivo.getbuffer()
        )


    with st.spinner(
        "Analizando documento..."
    ):

        loader = PDFLoader(
            "data/documento.pdf"
        )

        texto = loader.extraer_texto()


        crear_vectorstore(
            texto
        )


    st.success(
        "✅ Documento listo para consultas"
    )


    st.subheader(
        "💬 Consulta el documento"
    )


    pregunta = st.text_input(
        "Escribe tu pregunta:"
    )


    if st.button(
        "🔎 Analizar"
    ):

        if pregunta:

            with st.spinner(
                "Generando respuesta..."
            ):

                respuesta = preguntar_documento(
                    pregunta
                )


            st.info(
                respuesta
            )