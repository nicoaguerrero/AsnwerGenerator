from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace


def build_llm():
    llm = HuggingFaceEndpoint(
        repo_id="microsoft/Phi-3-mini-4k-instruct",
        task="text-generation",
        max_new_tokens=512,
        do_sample=False,
        repetition_penalty=1.03,
        huggingface_api_token=True,
    )

    return ChatHuggingFace(llm=llm, verbose=True)