from langchain_classic.chains.summarize import load_summarize_chain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.documents import Document as LCDocument
from app.core.config import settings


def summarize_text(text: str) -> str:
    # Initialize the Gemini LLM (using gemini-1.5-flash for fast, free tier performance)
    llm = ChatGoogleGenerativeAI(
        temperature=0,
        google_api_key=settings.GOOGLE_API_KEY,
        model="gemini-3.5-flash"
    )

    # Langchain expects a list of Document objects
    docs = [LCDocument(page_content=text)]

    # Load the summarization chain (map_reduce is good for longer texts)
    chain = load_summarize_chain(llm, chain_type="stuff")    # Execute summarization
    summary = chain.invoke(docs)
    return summary["output_text"]