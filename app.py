import streamlit as st
from src.backend import chatbot, fetch_all_threads
from langchain_core.messages import HumanMessage
from src.utils import (
    generate_new_thread,
    reset_chat,
    add_thread,
    load_chat,
    get_thread_display_name
)



#INITIALIZE UI MEMORY- Session state persists data across reruns of the app
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

#Each thread represents a separate conversation
if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = generate_new_thread()

#Allows users to switch between multiple chat histories
if "chat_threads" not in st.session_state:
    st.session_state["chat_threads"] = fetch_all_threads()

# Adds the current thread ID to the list of threads
add_thread(st.session_state["thread_id"])




#PAGE CONFIG-
st.set_page_config(
    page_title = "Stateful AI",
    page_icon = "🤖",
    layout= "centered"
)
st.title('🤖 Stateful Chatbot')



#SIDEBAR UI-
st.sidebar.header(body="⚙️ Setting", help="Press New Chat for new conversation", width="stretch", text_alignment="justify")
st.text(" ")


if st.sidebar.button(label="New Chat", type="primary", icon="📝", icon_position="left", use_container_width= False, width="content"):
    reset_chat()


st.sidebar.divider()
st.sidebar.subheader(body="Your Chats:", divider= True, width="content", text_alignment="center")


#show current thread-id as well as past-
for thread_id in st.session_state["chat_threads"][::-1]:
    
    # Get display name from first human message
    display_name = get_thread_display_name(thread_id)

    # User clicks a button for an old chat thread
    if st.sidebar.button(display_name, key= thread_id, use_container_width=True):
        st.session_state['thread_id'] = thread_id  # Switch to that thread

        messages = load_chat(thread_id) # Load old messages from database/storage

        temp_messages = []

        # Convert loaded messages to the right format
        for msg in messages:
            if isinstance(msg, HumanMessage):
                role = 'user'
            else:
                role = 'assistant'

            temp_messages.append({'role': role, 'content': msg.content})

        # Replace current chat with old chat
        st.session_state["chat_history"] = temp_messages



#LOAD CHAT HISTORY-
for messages in st.session_state["chat_history"]:
    with st.chat_message(messages['role']):
        st.text(messages['content'])



#MAIN UI-
CONFIG = {'configurable': {'thread_id': st.session_state["thread_id"]}}
user_input = st.chat_input(placeholder="Ask me anything...")


if user_input:

    st.session_state["chat_history"].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)



    with st.chat_message('assistant'):
        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                input=({'messages': HumanMessage(content= user_input)}),
                stream_mode="messages",
                config= CONFIG
            )
        )
    st.session_state["chat_history"].append({'role': 'assistant', 'content': ai_message})