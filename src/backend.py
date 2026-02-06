import os
from langgraph.checkpoint.memory import InMemorySaver
from typing import TypedDict, Annotated, List
from langgraph.graph import StateGraph, START
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph.message import add_messages
from langchain_groq import ChatGroq
from .tools import search_tool, calculator, get_stock_price
from dotenv import load_dotenv
load_dotenv()




MODEL = "openai/gpt-oss-120b"
TEMPERATURE = 0.3
MAX_TOKEN = 2000
API_KEY = os.getenv("GROQ_API_KEY")




#STATE-
class ChatState(TypedDict):

    messages: Annotated[List[BaseMessage], add_messages]



#LLM
def llm_init():
    
    llm = ChatGroq(
        model= MODEL,
        temperature= TEMPERATURE,
        max_tokens= MAX_TOKEN,
        api_key= API_KEY
        
    )

    return llm



#GRAPH
def build_graph():

    llm = llm_init()

    tools = [search_tool, calculator, get_stock_price]
    
    llm_with_tools = llm.bind_tools(tools= tools)

    #CHATNODE-
    def chatnode(state: ChatState) ->ChatState:

        messages = state['messages']

        response = llm_with_tools.invoke(messages)

        return {'messages': [response]}
    

    #TOOLNODE-
    toolnode = ToolNode(tools= tools)


    #GRAPH-
    builder = StateGraph(ChatState)
    checkpointer = InMemorySaver()

    builder.add_node('chatnode', chatnode)
    builder.add_node('tools', toolnode)

    builder.add_edge(START, 'chatnode')
    builder.add_conditional_edges('chatnode', tools_condition)
    builder.add_edge('tools', 'chatnode')

    chatbot = builder.compile(checkpointer= checkpointer)

    
    return chatbot



chatbot = build_graph()




if __name__ == "__main__":

    CONFIG = {'configurable': {'thread_id': 'thread-1'}}

    chatbot = build_graph()

    # initial_state = {'messages': HumanMessage(content="What is the current stock of apple?")}
    
    # response = chatbot.invoke(initial_state, config=CONFIG)
    
    # print(response['messages'][-1].content)

    #=========================STREAMING FEATURE===================================
    stream_generator = chatbot.stream(
        input= {'messages': 'Write a recipe to make pizza'},
        config= CONFIG,
        stream_mode="messages"
    )

    for chunk_message, metadata in stream_generator:
        print(chunk_message.content, sep=' ', end= ' ', flush= True)


