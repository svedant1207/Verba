from langchain_classic.chains.summarize import load_summarize_chain
from langchain_openai import ChatOpenAI
from langchain_core.documents import Document as LCDocument
from app.core.config import settings


def summarize_text(text: str) -> str:
    # Initialize the LLM
    llm = ChatOpenAI(temperature=0, openai_api_key=settings.OPENAI_API_KEY, model_name="gpt-3.5-turbo")

    # Langchain expects a list of Document objects
    docs = [LCDocument(page_content=text)]

    # Load the summarization chain (map_reduce is good for longer texts)
    chain = load_summarize_chain(llm, chain_type="map_reduce")

    # Execute summarization
    summary = chain.invoke(docs)
    return summary["output_text"]