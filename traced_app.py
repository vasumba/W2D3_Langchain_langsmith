from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o-mini")
prompts = [
    "What is artificial intelligence? Explain in two sentences.",
    "What is LangChain? Explain in simple words.",
    "Give three practical applications of AI in manufacturing."
]
for p in prompts:
    reply = llm.invoke(p)
    print(reply.content)