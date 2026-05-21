# Rule-Based AI Chatbot (Streamlit Web App)

A sleek, responsive, and interactive rule-based AI chatbot built using **Python** and **Streamlit**. This project demonstrates the fundamental concepts of text preprocessing, control flow, decision-making logic, and building interactive AI user interfaces.

---

## Features

- **Text Preprocessing Pipeline:** Uses Regular Expressions (`re`) to clean inputs by removing extra whitespaces, stripping trailing/leading spaces, and converting text to lowercase for reliable matching.
- **Flexible Pattern Matching:** Implements smart lookup logic using custom rule sets to handle user queries efficiently.
- **Interactive UI/UX:** A modern chat interface powered by Streamlit components (`st.chat_input` and `st.chat_message`) that mimics a real-world chat application.
- **Session Persistence:** Maintains full conversation history across web page re-renders using Streamlit's `session_state`.
- **Predefined Rule Domains:** Handles greetings, identity questions, capabilities, casual chat/jokes, and standard session exit commands seamlessly.

---

## Key Skills Demonstrated

- **Control Flow & Decision-Making:** Structured handling of continuous application loops and logical branching for response matching and graceful shutdowns.
- **Natural Language Processing (NLP) Basics:** Implementing a foundational text cleaning and tokenization/normalization strategy.
- **Full-Stack AI Prototyping:** Designing a modular and clean frontend script linked directly to the backend logic.
- **Clean Code Practices (PEP 8):** Properly written type hints, modular functional design, explicit docstrings, and a readable architecture.

---

## Project Structure

```text
├── app.py              # Main application source code containing UI and Chatbot logic
├── README.md           # Project documentation and setup guide
└── requirements.txt    # Required dependencies (Streamlit)
