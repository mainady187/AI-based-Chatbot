import re
import streamlit as st

chat = {
    
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! What's on your mind?",
    "hey": "Hey! Great to see you here. What can I do for you?",
    "greetings": "Greetings, human! How can I assist you today?",

   
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "your name": "I am a smart Rule-Based Chatbot.",
    "who are you": "I am an AI assistant built to respond to specific rules and keywords.",
    "what are you": "I'm a computer program designed to chat with you based on predefined logic.",
    "who created you": "I was created by a talented AI developer using Python!",

    "help": "Sure! You can ask me how I'm doing, my name, or what I can do. Type 'bye' to exit.",
    "what can you do": "I can answer your greetings, tell you about myself, or just have a basic conversation!",
    "commands": "Try typing: 'hi', 'how are you', 'your name', 'who created you', or 'joke'.",

    "thank you": "You're very welcome! Glad I could help.",
    "thanks": "Anytime! Let me know if you need anything else.",
    "joke": "Why do programmers wear glasses? Because they can't C#! 😂",
    "awesome": "I know, right? AI is pretty cool!",
    "cool": "Standard robot response: *Beep boop* dynamic level unlocked! 😎",

    "bye": "Goodbye! Have a wonderful day!",
    "exit": "Goodbye! Have a wonderful day!",
    "quit": "See you later! Terminal session closed."
}

def clean_input(user_text: str) -> str:
    """Clean the input text by converting to lowercase and stripping whitespace."""
    return re.sub(r'\s+', ' ', user_text).strip().lower()

def get_bot_response(user_message: str) -> str:
    """Get the bot response based on the user message."""
    return chat.get(user_message, "I'm sorry, I didn't understand that. Can you rephrase?")

st.set_page_config(page_title="Rule-Based Chatbot", page_icon="🤖")
st.title("Rule-Based AI Chatbot")
st.write("Welcome to the Rule-Based AI Chatbot! Type your message below and see how I respond based on predefined rules.")


if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! How can I help you today?"}]


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


if user_input := st.chat_input("Say something..."):
   
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    
    cleaned_input = clean_input(user_input)
    
    if cleaned_input in ['bye', 'exit']:
        bot_response = chat[cleaned_input]
    else:
        bot_response = get_bot_response(cleaned_input)
        
  
    with st.chat_message("assistant"):
        st.write(bot_response)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})