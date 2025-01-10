import streamlit as st
import requests
from datetime import datetime

#while loop that runs inf using cuny ID that connects to DB for degreework sample

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What's on your mind?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Create echo response
    response = f"Echo ({datetime.now().strftime('%H:%M:%S')}): {prompt}"
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Add a clear button
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Display chat info in sidebar
with st.sidebar:
    st.title("Chat Info")
    st.write(f"Total messages: {len(st.session_state.messages)}")
    if st.session_state.messages:
        st.write(f"Last message time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
