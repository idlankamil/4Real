# -*- coding: utf-8 -*-
"""
4Real Configuration File
========================
Simple configuration for API keys and settings.

IMPORTANT: Replace YOUR_API_KEY_HERE with your actual API keys!
"""

# ============================================================================
# API KEYS (REPLACE THESE!)
# ============================================================================

# OpenAI API Key (for ChatGPT chatbot)
# Get your key from: https://platform.openai.com/api-keys
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY_HERE"

# Ngrok Token (for Google Colab only)
# Get your token from: https://dashboard.ngrok.com/get-started/your-authtoken
NGROK_AUTH_TOKEN = "YOUR_NGROK_TOKEN_HERE"

# ============================================================================
# MODEL SETTINGS
# ============================================================================

# BERT Model (for semantic similarity)
BERT_MODEL = "all-MiniLM-L6-v2"

# ChatGPT Settings
CHATBOT_MODEL = "gpt-4o-mini"
CHATBOT_MAX_TOKENS = 250

# ============================================================================
# ALGORITHM SETTINGS
# ============================================================================

# Hybrid Algorithm Weights
TFIDF_WEIGHT = 0.4    # 40% weight
BERT_WEIGHT = 0.6     # 60% weight

# Plagiarism Thresholds (percentage)
THRESHOLD_HIGH = 80        # 80-100% = High similarity
THRESHOLD_MODERATE = 50    # 50-80% = Moderate similarity  
THRESHOLD_LOW = 20         # 20-50% = Low similarity
                          # 0-20% = Original work

# ============================================================================
# APP SETTINGS
# ============================================================================

APP_TITLE = "4Real - AI Plagiarism Detector"
APP_ICON = "🔍"
MAX_DOCUMENT_WORDS = 10000  # Maximum words per document

# ============================================================================
# END OF CONFIG
# ============================================================================
