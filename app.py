import streamlit as st
from src.backend import chatbot





if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []





st.set_page_config(
    page_title= "Stateful Chatbot",
    page_icon= "🤖",
    layout="centered"
)
st.title("🤖 Stateful Chatbot")


for messages in st.session_state["chat_history"]:
    with st.chat_message(messages['role']):
        st.markdown(messages['content'])





user_input = st.chat_input("Ask me anything...")

if user_input:
    st.session_state["chat_history"].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)

    
    

    with st.chat_message('assistant'):

        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                input={'messages': user_input},
                config= {'configurable': {'thread_id': 'thread-1'}},
                stream_mode="messages"  
            )    
        )

    st.session_state["chat_history"].append({'role': 'assistant', 'content': ai_message})

        