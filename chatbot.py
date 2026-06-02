# -*- coding: utf-8 -*-
"""
4Real Chatbot Module - AI Assistant Integration
================================================

Description:
    Floating chatbot interface powered by OpenAI's GPT-4o-mini model.
    Helps users understand how 4Real works and answers questions about
    plagiarism detection.

Features:
    - Floating chatbot button (accessible from any tab)
    - Real-time AI responses using ChatGPT
    - Chat history management
    - Context-aware conversations

Model Details:
    - Model: gpt-4o-mini
    - Max Tokens: 250 per response
    - Temperature: 0.7 (balanced creativity/accuracy)

Course: BAXI3413 Natural Language Processing
Project: 4Real Plagiarism Detector
Institution: Universiti Teknikal Malaysia Melaka (UTeM)

Authors: Group 4Real
    - MUHAMMAD IDLAN AZHAD BIN KAMIL RIADZ - B032310389
    - IMAN MUZAKKIR BIN AHMAD ZAKI - B032310689
    - AMMAR ZAIM BIN SAZILI - B032310346
    - MUHAMMAD HAFIZUDDIN BIN KAMARUL HATTA - B032310676
"""

# ============================================================================
# IMPORTS
# ============================================================================

import streamlit as st
from openai import OpenAI
import config

# ============================================================================
# API CONFIGURATION
# ============================================================================

# Initialize OpenAI client
# Note: Replace with your actual API key in config.py before running
client = OpenAI(
    api_key=config.OPENAI_API_KEY  
)

# ============================================================================
# CHATBOT INTERFACE FUNCTION
# ============================================================================

def show_floating_chatbot():
    """
    Display floating chatbot button with ChatGPT (gpt-4o-mini).
    
    Creates an interactive AI assistant that:
    - Opens/closes on button click
    - Maintains conversation history
    - Provides context-aware responses about 4Real system
    
    The chatbot uses GPT-4o-mini for natural language understanding
    and keeps the last 6 messages for context.
    """
    
    # ========================================================================
    # SESSION STATE INITIALIZATION
    # ========================================================================
    # Streamlit session state persists data across page reruns
    # Essential for maintaining chat history between interactions
    
    # Initialize chat window visibility (closed by default)
    if "chat_open" not in st.session_state:
        st.session_state.chat_open = False
    
    # Initialize chat history (empty at start)
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    # ========================================================================
    # CHAT TOGGLE BUTTON
    # ========================================================================
    # Create button in top-right corner using column layout
    
    col1, col2, col3 = st.columns([6, 1, 1])
    with col3:
        if st.button("💬", key="chat_toggle", help="Chat with 4Real Assistant (Powered by GPT-4o-mini)"):
            # Toggle chat window open/closed
            st.session_state.chat_open = not st.session_state.chat_open
    
    # ========================================================================
    # CHAT WINDOW DISPLAY
    # ========================================================================
    # Show chat interface if window is open
    
    if st.session_state.chat_open:
        with st.container():
            st.markdown("---")
            st.markdown("### 💬 Ask 4Real Assistant")
            st.caption("*Powered by GPT-4o-mini - Fast & Smart AI*")
            
            # Display chat history
            # User messages shown in blue, assistant messages in green
            for msg in st.session_state.chat_history:
                if msg["role"] == "user":
                    st.info(f"**You:** {msg['content']}")
                else:
                    st.success(f"**🤖 4Real:** {msg['content']}")
            
            # User input field
            user_input = st.text_input(
                "Ask anything about 4Real:", 
                placeholder="e.g., How does plagiarism detection work?", 
                key="floating_chat_input"
            )
            
            # Action buttons (Send, Clear, Close)
            col1, col2, col3 = st.columns([2, 1, 1])
            with col1:
                send_btn = st.button("Send 🚀", key="floating_send", use_container_width=True)
            with col2:
                clear_btn = st.button("Clear 🗑️", key="clear_chat", use_container_width=True)
            with col3:
                close_btn = st.button("Close ❌", key="floating_close", use_container_width=True)
            
            # ================================================================
            # BUTTON ACTIONS
            # ================================================================
            
            # Close button: hide chat window
            if close_btn:
                st.session_state.chat_open = False
                st.rerun()
            
            # Clear button: reset conversation history
            if clear_btn:
                st.session_state.chat_history = []
                st.rerun()
            
            # Send button: process user message
            if send_btn and user_input:
                with st.spinner("🤖 Thinking..."):
                    try:
                        # ====================================================
                        # BUILD CONVERSATION CONTEXT
                        # ====================================================
                        # Prepare messages for OpenAI API
                        # Format: system prompt + chat history + current question
                        
                        messages = [
                            {
                                "role": "system", 
                                "content": """You are a helpful AI assistant for 4Real plagiarism detector app. 
                            Answer questions about:
                            - How 4Real works (TF-IDF and BERT algorithms)
                            - Plagiarism detection methods
                            - How to use the app
                            - What the similarity scores mean
                            - Difference between TF-IDF and BERT
                            Keep answers clear, concise (2-3 sentences), and friendly."""
                            },
                        ]
                        
                        # Add recent chat history (last 6 messages for context)
                        # This helps the AI understand the conversation flow
                        recent_history = st.session_state.chat_history[-6:] if len(st.session_state.chat_history) > 6 else st.session_state.chat_history
                        for msg in recent_history:
                            messages.append(msg)
                        
                        # Add current user question
                        messages.append({"role": "user", "content": user_input})
                        
                        # ====================================================
                        # CALL OPENAI API
                        # ====================================================
                        # Send messages to GPT-4o-mini and get response
                        
                        response = client.chat.completions.create(
                            model="gpt-4o-mini",      # Cost-effective model
                            messages=messages,         # Full conversation context
                            max_tokens=250,           # Limit response length
                            temperature=0.7           # Balance between creative and focused
                        )
                        
                        # Extract AI's response
                        assistant_message = response.choices[0].message.content
                        
                        # ====================================================
                        # SAVE TO CHAT HISTORY
                        # ====================================================
                        # Store both user question and AI response
                        
                        st.session_state.chat_history.append({"role": "user", "content": user_input})
                        st.session_state.chat_history.append({"role": "assistant", "content": assistant_message})
                        
                        # Refresh page to display new messages
                        st.rerun()
                        
                    except Exception as e:
                        # Handle errors gracefully (API issues, network problems, etc.)
                        st.error(f"⚠️ Error: {str(e)}")
                        st.info("💡 Tip: Check your API key or internet connection")

# ============================================================================
# END OF FILE
# ============================================================================