# 🧠 DocuMind AI

Asistente inteligente basado en inteligencia artificial capaz de analizar documentos PDF y responder preguntas utilizando la información contenida dentro del archivo.

El proyecto implementa una arquitectura **RAG (Retrieval Augmented Generation)**, combinando búsqueda semántica mediante embeddings con modelos generativos de Cohere para obtener respuestas contextualizadas.

---

# 🚀 Características

- 📄 Procesamiento automático de documentos PDF.
- 🧠 Generación de embeddings con Cohere.
- 🔎 Recuperación de información mediante búsqueda semántica.
- 🗂 Base vectorial utilizando FAISS.
- 🤖 Generación de respuestas con modelos de lenguaje.
- 🌐 Interfaz web desarrollada con Streamlit.
- 📚 Respuestas basadas únicamente en el contenido del documento.

---

# 🏗 Arquitectura de la solución

```text
Usuario
   |
   ↓
Aplicación Streamlit
   |
   ↓
Carga y procesamiento PDF
   |
   ↓
Generación de embeddings
   |
   ↓
FAISS Vector Database
   |
   ↓
Modelo Cohere
   |
   ↓
Respuesta generada
```

---

# 🛠 Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Python | Lenguaje principal |
| Streamlit | Interfaz web |
| Cohere API | Modelo de inteligencia artificial |
| LangChain | Orquestación del flujo RAG |
| FAISS | Base de datos vectorial |
| PyPDF | Lectura de documentos PDF |

---

# ⚙ Instalación

## 1. Clonar repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

Ingresar al proyecto:

```bash
cd DocuMind-AI
```

---

## 2. Crear entorno virtual

```bash
python -m venv venv
```

Activar entorno:

Windows:

```bash
venv\Scripts\activate
```

---

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 4. Configurar API Key de Cohere

Crear un archivo llamado:

```text
.env
```

Agregar:

```env
COHERE_API_KEY=tu_api_key
```

---

# ▶ Ejecutar aplicación

Ejecutar:

```bash
streamlit run app.py
```

La aplicación estará disponible en:

```text
http://localhost:8501
```

---

# 💬 Ejemplos de preguntas

### Pregunta:

```text
¿Cuál es el objetivo principal del documento?
```

### Respuesta generada:

```text
El agente analiza el contenido del documento y proporciona una respuesta basada en la información encontrada.
```

---

### Pregunta:

```text
¿Qué información importante contiene el archivo?
```

### Respuesta generada:

```text
La información relevante se recupera mediante búsqueda semántica y es utilizada para generar una respuesta contextualizada.
```

---

# 📂 Estructura del proyecto

```text
DocuMind-AI
│
├── app.py
├── README.md
├── requirements.txt
├── .env.example
│
├── data
│   └── documento.pdf
│
└── src
    ├── loader.py
    ├── embeddings.py
    └── chatbot.py
```

---

# 👨‍💻 Autor

Implementando un asistente inteligente basado en documentos PDF utilizando inteligencia artificial generativa y arquitectura RAG.