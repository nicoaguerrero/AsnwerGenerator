from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import ChatPromptTemplate
from src.prompts import autoreply_prompt

def setup_vectorstore():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    vector_store = Chroma(embedding_function=embeddings)
    return vector_store

def add_qa_pair(vector_store, question, answer):
    document = Document(page_content=question, metadata={"answer": answer})
    vector_store.add_documents([document])

def search_question(vector_store, question):
    results = vector_store.similarity_search(question)
    print(results)
    return [(result.page_content, result.metadata["answer"]) for result in results]

def search_and_respond(model, vector_store, question):
    results = vector_store.similarity_search(question)
    relevant_answers = "\n".join([result.metadata["answer"] for result in results])
    prompt = ChatPromptTemplate.from_template(autoreply_prompt)
    prompt_value = prompt.invoke({"question": question, "relevant_answers": relevant_answers})
    response = model.invoke(prompt_value)
    return response.content