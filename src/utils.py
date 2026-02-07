import uuid
import streamlit as st
from src.backend import chatbot
from langchain_core.messages import HumanMessage


def generate_new_thread():
    """Generate a unique thread ID"""

    thread_id = str(uuid.uuid4())

    return thread_id



def reset_chat():
    """Reset the current chat and create a new thread"""

    thread_id = generate_new_thread()

    st.session_state["thread_id"] = thread_id

    add_thread(thread_id)

    st.session_state["chat_history"] = []




def add_thread(thread_id):

    if thread_id not in st.session_state["chat_threads"]:
        st.session_state["chat_threads"].append(thread_id)




def load_chat(thread_id):
    """Load conversation history from a specific thread"""

    state = chatbot.get_state(
        config= {'configurable': {'thread_id': thread_id}}
    )

    return state.values.get("messages", [])




def get_thread_display_name(thread_id):
    """Get a display name for a thread based on the first human message"""
    messages = load_chat(thread_id)
    
    # Find the first human message
    for message in messages:
        is_human = isinstance(message, HumanMessage) or (hasattr(message, 'type') and message.type == 'human')
        
        if is_human and message.content:
            # Get first 20 characters and add ellipsis
            content = message.content.strip()
            if len(content) > 10:
                return content[:20] + "..."
            else:
                return content
    
    # Fallback if no human message found
    return f"Chat- {thread_id[0]}..."


