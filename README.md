# 🔍 4Real - AI Plagiarism Detector
An AI-powered plagiarism detection web app built with Streamlit and a hybrid TF-IDF and BERT pipeline.
Paste two documents and get an instant similarity score that catches both exact copying and paraphrasing.

# ✨ Technologies
* `Python`
* `Streamlit`
* `Sentence-BERT`
* `scikit-learn`
* `OpenAI GPT-4o-mini`

# 🚀 Features
* Hybrid detection combining TF-IDF (40%) and BERT semantic analysis (60%) into a single similarity score
* Catches both direct word-for-word copying and cleverly reworded paraphrasing
* Side-by-side document input with live word count
* Color-coded verdict: Original, Low, Moderate, or High similarity
* Built-in GPT-4o-mini chatbot assistant to answer questions about the app

# 📍 The Process

Wanted to build a plagiarism checker that goes beyond simple word matching. Most basic tools
miss paraphrasing completely since the words are different even if the meaning is identical.
So the system runs two checks at once: TF-IDF catches exact word overlap while BERT reads
the actual meaning of the text. Both scores get combined into one final result, weighted
towards BERT since paraphrasing is the harder problem to catch. Wrapped everything in
Streamlit so it's easy to use without any technical knowledge.

# 🚦 Running the Project
1. Clone the repository
2. Upload `4real_app.py`, `chatbot.py`, and `config.py` to Google Drive inside a folder named `4Real_Project`
3. Get your OpenAI API key from `https://platform.openai.com/api-keys` and Ngrok token from `https://dashboard.ngrok.com`
4. Open `config.py` in Colab and replace both placeholder keys with your actual keys, then save
5. Open a new Colab notebook and mount Google Drive, then navigate to the project folder
6. Install dependencies: `!pip install streamlit sentence-transformers scikit-learn openai pyngrok -q`
7. Run the launch block to start Streamlit and create a public Ngrok URL
8. Click the generated URL, hit "Visit Site", and wait 10-20 seconds for the model to load

> Full step-by-step setup in `setup_guide.md`
