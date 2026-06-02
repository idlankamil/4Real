# -*- coding: utf-8 -*-
"""
4Real - Advanced AI Plagiarism Detection System
================================================

Description:
    Main application file for 4Real plagiarism detector.
    Uses a hybrid approach combining TF-IDF and BERT algorithms
    to detect both exact copying and sophisticated paraphrasing.

Algorithm:
    - TF-IDF (40% weight): Detects exact word matches
    - BERT AI (60% weight): Detects semantic similarity and paraphrasing
    - Final Score = (TF-IDF × 0.4) + (BERT × 0.6)

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
from chatbot import show_floating_chatbot
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

# Configure Streamlit page settings
st.set_page_config(
    page_title="4Real - AI Plagiarism Detector",  # Browser tab title
    page_icon="🔍",                                # Browser tab icon
    layout="wide",                                 # Use full width of screen
    initial_sidebar_state="collapsed"              # Hide sidebar by default
)

# ============================================================================
# CUSTOM CSS STYLING
# ============================================================================

# Apply custom CSS for purple gradient design and better buttons
st.markdown("""
<style>
    .main { padding: 2rem; }
    
    /* Better Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-size: 1.5rem;
        font-weight: bold;
        padding: 1rem 2rem;
        border-radius: 10px;
        border: none;
        transition: all 0.3s;
        box-shadow: 0 4px 15px rgba(102,126,234,0.3);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102,126,234,0.4);
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
        background-color: transparent;
        padding: 1rem 0;
    }
    
    .stTabs [data-baseweb="tab"] {
        font-size: 1.2rem;
        font-weight: 600;
        padding: 1rem 2rem;
        border-radius: 8px;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# MODEL LOADING
# ============================================================================

@st.cache_resource
def load_model():
    """
    Load the BERT model for semantic similarity detection.
    
    Uses Streamlit's cache to load the model only once (not every time).
    This makes the app much faster after the first load.
    
    Model: all-MiniLM-L6-v2 (Sentence-BERT)
    - Size: ~80MB (lightweight and fast)
    - Purpose: Convert text to semantic embeddings
    - Output: 384-dimensional vector representing text meaning
    
    Returns:
        SentenceTransformer: Pre-trained BERT model
    """
    return SentenceTransformer('all-MiniLM-L6-v2')

# Load model once at startup
model = load_model()

# ============================================================================
# MAIN APPLICATION INTERFACE
# ============================================================================

# Display main title
st.markdown("# 🔍 4Real - Advanced AI Plagiarism Detection")
st.markdown("---")

# Create navigation tabs
tab1, tab2, tab3 = st.tabs(["🔍 Check Plagiarism", "📚 About", "❓ Help & FAQ"])

# Display floating chatbot (available on all tabs)
show_floating_chatbot()

# ============================================================================
# TAB 1: CHECK PLAGIARISM (Main Functionality)
# ============================================================================

with tab1:
    """
    Main plagiarism detection interface.
    Users paste two documents and get instant similarity analysis.
    """
    
    st.markdown("### Paste your documents below to check for similarity")
    
    # Create two columns for side-by-side document input
    col1, col2 = st.columns(2)
    
    # LEFT COLUMN: Document 1
    with col1:
        st.markdown("#### 📄 Document 1")
        text1 = st.text_area(
            "Paste first document", 
            height=300, 
            key="text1", 
            label_visibility="collapsed"
        )
        # Show word count
        st.caption(f"Words: {len(text1.split())}")
    
    # RIGHT COLUMN: Document 2
    with col2:
        st.markdown("#### 📄 Document 2")
        text2 = st.text_area(
            "Paste second document", 
            height=300, 
            key="text2", 
            label_visibility="collapsed"
        )
        # Show word count
        st.caption(f"Words: {len(text2.split())}")
    
    st.markdown("---")
    
    # ========================================================================
    # CHECK PLAGIARISM BUTTON
    # ========================================================================
    
    if st.button("🔍 CHECK PLAGIARISM", use_container_width=True, type="primary"):
        
        # Validate input - both documents must have text
        if text1 and text2:
            
            # Show loading spinner during analysis (7-10 seconds)
            with st.spinner("🤖 Analyzing with AI..."):
                
                # ============================================================
                # STEP 1: TF-IDF ANALYSIS (40% weight)
                # ============================================================
                
                # Create TF-IDF vectorizer and transform documents
                vectorizer = TfidfVectorizer()
                tfidf_vectors = vectorizer.fit_transform([text1, text2])
                
                # Calculate cosine similarity between TF-IDF vectors
                tfidf_similarity = cosine_similarity(tfidf_vectors[0], tfidf_vectors[1])[0][0]
                
                # ============================================================
                # STEP 2: BERT SEMANTIC ANALYSIS (60% weight)
                # ============================================================
                
                # Encode both documents using BERT model
                embeddings = model.encode([text1, text2])
                
                # Calculate cosine similarity between BERT embeddings
                bert_similarity = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
                
                # ============================================================
                # STEP 3: HYBRID COMBINATION
                # ============================================================
                
                # Calculate weighted final score
                final_score = (tfidf_similarity * 0.4) + (bert_similarity * 0.6)
                final_percentage = round(final_score * 100, 2)
                
                # ============================================================
                # STEP 4: DISPLAY RESULTS
                # ============================================================
                
                st.markdown("---")
                st.markdown("## 📊 Analysis Results")
                
                # Display verdict with color based on similarity level
                # Use OLD style: direct text in verdict
                if final_percentage >= 80:
                    st.error(f"### 🚨 HIGH SIMILARITY: {final_percentage}%")
                    recommendation = "This document appears to be heavily copied. Manual review strongly recommended."
                elif final_percentage >= 50:
                    st.warning(f"### ⚠️ MODERATE SIMILARITY: {final_percentage}%")
                    recommendation = "Significant overlap detected. Manual review recommended to verify originality."
                elif final_percentage >= 20:
                    st.info(f"### ⚡ LOW SIMILARITY: {final_percentage}%")
                    recommendation = "Some common phrases found. This is likely acceptable overlap."
                else:
                    st.success(f"### ✅ ORIGINAL WORK: {final_percentage}%")
                    recommendation = "No significant plagiarism detected. Document appears original."
                
                st.markdown("---")
                
                # ============================================================
                # STEP 5: DETAILED BREAKDOWN
                # ============================================================
                
                st.markdown("### 🔬 Detailed Breakdown")
                
                # Display individual scores in three columns
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric(
                        "📊 TF-IDF Score", 
                        f"{round(tfidf_similarity * 100, 2):.2f}%", 
                        help="Exact word matching"
                    )
                
                with col2:
                    st.metric(
                        "🧠 BERT AI Score", 
                        f"{round(bert_similarity * 100, 2):.2f}%", 
                        help="Semantic analysis"
                    )
                
                with col3:
                    st.metric(
                        "🎯 Final Score", 
                        f"{final_percentage:.2f}%", 
                        help="Combined hybrid score"
                    )
                
                # Display dynamic recommendation based on score
                st.info(f"💡 **Recommendation:** {recommendation}")
                
                # Display visual progress bar
                st.markdown("### 📈 Similarity Level")
                st.progress(final_score)
                
        else:
            # Show error if documents are empty
            st.error("⚠️ Please enter text in both documents!")

# ============================================================================
# TAB 2: ABOUT (System Information)
# ============================================================================

with tab2:
    """
    Information about the 4Real system.
    Explains how it works and the technology behind it.
    """
    
    st.markdown("## 📚 About 4Real")
    
    # What is 4Real?
    st.markdown("### 🎯 What is 4Real?")
    st.write(
        "4Real is an advanced AI-powered plagiarism detection system that uses "
        "cutting-edge NLP techniques to identify document similarities."
    )
    
    # How It Works
    st.markdown("### ⚙️ How It Works")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **📊 TF-IDF Analysis (40%)**
        - Analyzes word frequency
        - Detects exact matches
        - Identifies direct copying
        """)
    
    with col2:
        st.info("""
        **🧠 BERT AI (60%)**
        - Understands context
        - Detects paraphrasing
        - Semantic analysis
        """)
    
    # Technology Stack
    st.markdown("### 💻 Technology Stack")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("**🤖 AI Model**\n\nSentence-BERT")
    with col2:
        st.markdown("**🎨 Framework**\n\nStreamlit")
    with col3:
        st.markdown("**📊 Libraries**\n\nscikit-learn")
    with col4:
        st.markdown("**💬 Chatbot**\n\nChatGPT AI")
    
    # Development Team
    st.markdown("### 👥 Development Team")
    st.success("""
    **📚 BAXI3413 Natural Language Processing Project**
    
    **🚀 Developed by Group 4Real**
    
    *Universiti Teknikal Malaysia Melaka (UTeM)*
    
    **Team Members:**
    - MUHAMMAD IDLAN AZHAD BIN KAMIL RIADZ - B032310389
    - IMAN MUZAKKIR BIN AHMAD ZAKI - B032310689
    - AMMAR ZAIM BIN SAZILI - B032310346
    - MUHAMMAD HAFIZUDDIN BIN KAMARUL HATTA - B032310676
    """)

# ============================================================================
# TAB 3: HELP & FAQ (User Assistance)
# ============================================================================

with tab3:
    """
    Help documentation and answers to common questions.
    Uses expandable sections for easy navigation.
    """
    
    st.markdown("## ❓ Help & FAQ")
    
    # FAQ 1: How to use
    with st.expander("📖 How do I use 4Real?", expanded=True):
        st.write("1. Go to Check Plagiarism tab")
        st.write("2. Paste two documents")
        st.write("3. Click CHECK PLAGIARISM")
        st.write("4. View results!")
    
    # FAQ 2: Score meanings
    with st.expander("🤔 What do the scores mean?"):
        st.write("**80-100%:** High similarity")
        st.write("**50-80%:** Moderate similarity")
        st.write("**20-50%:** Low similarity")
        st.write("**0-20%:** Original work")
    
    # FAQ 3: TF-IDF explanation
    with st.expander("🧠 What is TF-IDF?"):
        st.write(
            "TF-IDF measures word importance. Excellent for exact matching. "
            "Contributes 40% to final score."
        )
    
    # FAQ 4: BERT explanation
    with st.expander("🤖 What is BERT?"):
        st.write(
            "BERT is Google AI that understands meaning. Detects paraphrasing. "
            "Contributes 60% to score."
        )
    
    # FAQ 5: File upload
    with st.expander("📁 Can I upload files?"):
        st.write("File upload coming soon! Currently copy-paste text into boxes.")
    
    # FAQ 6: Accuracy
    with st.expander("💬 How accurate is 4Real?"):
        st.write(
            "Highly accurate! Hybrid AI (TF-IDF + BERT) catches both exact "
            "copying and paraphrasing."
        )

# ============================================================================
# END OF FILE
# ============================================================================