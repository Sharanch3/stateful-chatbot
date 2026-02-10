# 🧠 LangGraph-Based Conversational Chatbot

An interactive AI chatbot built using **LangGraph** that supports **real-time streaming, persistent memory, tool calling, resumable multi-threaded conversations, and full observability via LangSmith** — all wrapped in a clean **Streamlit UI**.

This project demonstrates how to build a **production-style conversational agent** with explicit state management, database-backed memory, **execution tracing**, and user-friendly interaction.

---

## 🌐 Live Demo

**LINK** -> 

---

## 🚀 Features

### 🔄 Real-Time Streaming
- Token-by-token streaming responses  
- Smooth, ChatGPT-like conversational experience  
- Tool execution status shown live in the UI  

### 🧠 Short-Term Memory
- Maintains conversation context within a chat session  
- Uses LangGraph state management for message flow  

### 💾 Persistent Chat Threads (SQLite)
- Each conversation is stored as a **thread**  
- Backed by **SQLite** for durability  
- Conversations survive page reloads and app restarts  

### ▶️ Resume Chat Feature
- Users can resume any previous chat thread  
- Reloading the app does **not** reset conversations  
- Sidebar thread selection for easy navigation  

### 🛠 Tool Calling Support
- Integrated external tools (search, utilities, etc.)  
- Automatic tool routing via LangGraph  
- Tool execution is streamed and visible to users  

### 🔍 Observability & Tracing (LangSmith)
- End-to-end tracing of LLM calls, tool invocations, and graph execution  
- Visibility into conversation flow and decision paths  
- Enables debugging, performance monitoring, and evaluation  
- Bridges the gap between demo chatbots and production-ready systems  

### 🖥 Streamlit UI
- Clean, interactive chat interface  
- Sidebar for chat thread management  
- Real-time response rendering  

---

### Key Components:
- **LangGraph** → Orchestrates conversation flow
- **SQLite Checkpointer** → Stores chat history per thread
- **Streamlit** → Frontend UI
- **Tool Nodes** → External capabilities
- **Streaming** → Real-time token output
- **Langsmith**  → End-to-end observability

---

## 🧰 Tech Stack

- **Python**
- **LangGraph**
- **LangChain**
- **Langsmith**
- **Streamlit**
- **SQLite**
- **LLM Provider** (OpenAI / Groq / others)

---

Built with ❤️ using LangGraph and Streamlit



