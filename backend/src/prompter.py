from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from langchain_postgres import PGVector
from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate
from langgraph.graph import START, StateGraph
from langgraph.graph.state import CompiledStateGraph
from typing_extensions import List, TypedDict
from dotenv import load_dotenv
import os


# Define state for application
class State(TypedDict):
    code: str
    language: str
    context: List[Document]
    answer: str


# Build state
def build_state_graph() -> CompiledStateGraph:
    load_dotenv()

    # Configure Azure OpenAI Completion
    llm = AzureChatOpenAI(
        azure_deployment=os.getenv("COMPLETION_AZURE_DEPLOYMENT"),
        temperature=0,
        max_tokens=500,
        timeout=30,
        max_retries=2,
    )
    # Configure Azure OpenAI Embedding
    embeddings = AzureOpenAIEmbeddings(
        azure_deployment=os.getenv("EMBEDDING_AZURE_DEPLOYMENT"),
    )
    # Configure PGVector
    vector_store = PGVector(
        connection=os.getenv("DATABASE_URL"),
        embeddings=embeddings,
    )

    # Define prompt
    template = """Use the following pieces of context to give feedback on the code snippet at the end.
    Answer as a senior software developer. Be precise, ensure clarity, you must only use a list of issues. Do not give more than 5 issues. If there are none, say so, if you don't know, say you don't know and don't make up an answer.

    {context}

    Code ({language}): 
    {code}

    Helpful Answer:"""
    prompt = PromptTemplate.from_template(template)

    # Define retrieve step
    def retrieve(state: State):
        retrieved_docs = vector_store.similarity_search(state["code"])
        return {"context": retrieved_docs}

    # Define generate step
    def generate(state: State):
        docs_content = "\n\n".join(doc.page_content for doc in state["context"])
        messages = prompt.invoke(
            {
                "code": state["code"],
                "language": state["language"],
                "context": docs_content,
            }
        )
        response = llm.invoke(messages)
        return {"answer": response.content}

    graph_builder = StateGraph(State).add_sequence([retrieve, generate])
    graph_builder.add_edge(START, "retrieve")
    return graph_builder.compile()
