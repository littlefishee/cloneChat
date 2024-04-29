import streamlit as st
from langchain.memory import ConversationBufferMemory

from utils import get_chat_response

st.header("克隆Chat_GPT")

with st.sidebar:
    openai_api_key = st.text_input("请输入OpenAI的API Key", type="password")
    st.markdown("[点击此处获取openai的api key](https://platform.openai.com/api-keys)")

if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages = True)
    st.session_state["messages"] = [{"role":"ai", "content":"从提问开始吧"}]
for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()
if prompt:
    if not openai_api_key:
        st.info("请输入你的OpenAI API Key")
        st.stop()
    st.session_state["messages"].append({"role":"human", "content":prompt})
    st.chat_message("human").write(prompt)

    with st.spinner("AI正在思考中"):
        response = get_chat_response(prompt,st.session_state["memory"],openai_api_key)
    st.session_state["messages"].append({"role":"ai","content":response})
    st.chat_message("ai").write(response)