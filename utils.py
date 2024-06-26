from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI
# from langchain.memory import ConversationBufferMemory

def get_chat_response(prompt, memory, openai_api_key):
    model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key)
    chain = ConversationChain(llm=model,memory=memory)

    response = chain.invoke({"input":prompt})
    return response["response"]

# memory = ConversationBufferMemory(return_messages = True)
# print(get_chat_response("牛顿提出过哪些知名的定律",memory,"sk-proj-DfnTHxCrhvJ8x8YXwQKZT3BlbkFJI16sdvUHM2tzIwlzXDc1"))
# print(get_chat_response("上一个问题是？",memory,"sk-proj-DfnTHxCrhvJ8x8YXwQKZT3BlbkFJI16sdvUHM2tzIwlzXDc1"))