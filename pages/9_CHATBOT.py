import streamlit as st
import google.generativeai as genai

# Configure the Gemini API (replace with your actual API key)
genai.configure(api_key='AIzaSyBJU_x6Vn3crT-lpx6-QRrNrJxsEeJTbSw')

# Set up the model
model = genai.GenerativeModel('gemini-pro')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Streamlit app
st.title("Gemini Chatbot")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate Gemini response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Stream response from the model
        for chunk in model.generate_content(prompt, stream=True):
            full_response += chunk.text  # Access the text attribute directly
            message_placeholder.markdown(full_response + "▌")
        
        message_placeholder.markdown(full_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Sidebar with information
st.sidebar.title("About")
st.sidebar.info("This is a Gemini chatbot powered by Streamlit.")
st.sidebar.warning("Please note: You need to replace the placeholder API key with your actual Gemini API key.")
