# 🚀 4Real Setup Guide - Complete Beginner's Tutorial

**Project:** 4Real AI Plagiarism Detector  
**Course:** BAXI3413 Natural Language Processing  
**Institution:** Universiti Teknikal Malaysia Melaka (UTeM)

---

## 📋 What You Need

Before starting, make sure you have:

- ✅ Google Account (Gmail)
- ✅ Internet connection
- ✅ 15-20 minutes of time
- ✅ Project files (4real_app.py, chatbot.py, config.py)

---

## 🎯 Overview

This guide will help you:
1. Get required API keys (OpenAI & Ngrok)
2. Configure the project files
3. Run 4Real on Google Colab
4. Share it with others via public URL

**Total time:** 15-20 minutes (first time)

---

# Part 1: Get API Keys (10 minutes)

## Step 1: Get OpenAI API Key

**What is this?** The key that lets the chatbot AI work.

### Instructions:

1. Go to: https://platform.openai.com/signup
2. Sign up with your email or Google account
3. Verify your email if needed
4. After login, go to: https://platform.openai.com/api-keys
5. Click "**+ Create new secret key**"
6. Name it: `4Real_Project`
7. Click "Create secret key"
8. **COPY THE KEY** - it starts with `sk-proj-...`
9. Save it in Notepad temporarily

⚠️ **IMPORTANT:** You can only see this key once! Copy it immediately!

---

## Step 2: Get Ngrok Auth Token

**What is this?** The key that creates a public URL for your app.

### Instructions:

1. Go to: https://ngrok.com
2. Click "**Sign up**" (or use Google account)
3. After signup, click "**Your Authtoken**" in the left menu
4. Or go directly to: https://dashboard.ngrok.com/get-started/your-authtoken
5. Click "**Copy**" button
6. Save it in Notepad with your OpenAI key

Your Notepad should look like:
```
OpenAI Key: sk-proj-abc123xyz789...
Ngrok Token: 2abc123XYZ456def789...
```

✅ **Done! You have both keys!**

---

# Part 2: Upload Files to Google Drive (5 minutes)

## Step 1: Create Project Folder

1. Go to: https://drive.google.com
2. Click "**+ New**" → "**New folder**"
3. Name it: `4Real_Project`
4. Double-click to open the folder

## Step 2: Upload Files

1. Click "**+ New**" → "**File upload**"
2. Select these files:
   - `4real_app.py`
   - `chatbot.py`
   - `config.py`
3. Wait for upload to complete (green checkmarks)

✅ **Files uploaded!**

---

# Part 3: Configure API Keys (3 minutes)

## Step 1: Edit config.py

1. In Google Drive, **right-click** on `config.py`
2. Click "**Open with**" → "**Google Colaboratory**"
   - If you don't see it, click "Connect more apps" and search for "Colaboratory"
   - **Alternative:** You can also use other editing tools such as "Anyfile Notepad" or download the file and edit with any text editor
3. Find line with `OPENAI_API_KEY = "YOUR_OPENAI_API_KEY_HERE"`
4. Replace `YOUR_OPENAI_API_KEY_HERE` with your actual OpenAI key
5. Find line with `NGROK_AUTH_TOKEN = "YOUR_NGROK_TOKEN_HERE"`
6. Replace `YOUR_NGROK_TOKEN_HERE` with your actual Ngrok token
7. Press `Ctrl+S` (or `Cmd+S` on Mac) to **SAVE**
8. Close the tab

**Example:**
```python
# Before:
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY_HERE"

# After:
OPENAI_API_KEY = "sk-proj-abc123xyz789..."
```

✅ **Config file ready!**

---

# Part 4: Run on Google Colab (Main Part!)

## Step 1: Create New Notebook

1. Go to: https://colab.research.google.com
2. Click "**+ New notebook**"

## Step 2: Mount Google Drive

Copy and paste this in the first cell:

```python
from google.colab import drive
drive.mount('/content/drive')
```

Click the ▶️ Play button (or press `Shift+Enter`)

- Click "Connect to Google Drive"
- Choose your account
- Click "Allow"
- Wait for: `Mounted at /content/drive` ✅

## Step 3: Navigate to Project Folder

Add new cell (click "+ Code"), then paste:

```python
%cd /content/drive/MyDrive/4Real_Project
```

Run it. You should see: `/content/drive/MyDrive/4Real_Project`

## Step 4: Install Packages

Add new cell and paste:

```python
!pip install streamlit sentence-transformers scikit-learn openai pyngrok -q
print("✅ All packages installed!")
```

Run it and **WAIT 2-3 MINUTES** ⏳

## Step 5: Configure Ngrok

Add new cell and paste:

```python
!ngrok config add-authtoken YOUR_NGROK_TOKEN_HERE
```

⚠️ **REPLACE** `YOUR_NGROK_TOKEN_HERE` with your actual token!

Run it.

## Step 6: Launch 4Real

Add new cell and paste this complete block:

```python
import subprocess
import time
from pyngrok import ngrok

# Start Streamlit
print("🚀 Starting 4Real application...")
subprocess.Popen(['streamlit', 'run', '4real_app.py', '--server.port', '8501'])

# Wait for initialization
print("⏳ Waiting 15 seconds...")
time.sleep(15)

# Create public URL
print("🌐 Creating public URL...")
public_url = ngrok.connect(8501)

# Display results
print("\n" + "="*70)
print("🎉 4REAL IS NOW LIVE!")
print("="*70)
print(f"\n🌐 PUBLIC URL: {public_url}")
print("\n📝 INSTRUCTIONS:")
print("1. Click the URL above")
print("2. Wait 10-20 seconds for first load")
print("3. You'll see the 4Real homepage!")
print("\n⚠️ Keep this tab open! If you close it, app stops.")
print("="*70)
```

Run it and **WAIT 15-20 SECONDS**

## Step 7: Open Your App

You'll see output like:

```
🎉 4REAL IS NOW LIVE!
====================================================================
🌐 PUBLIC URL: https://abc123.ngrok-free.app
====================================================================
```

1. **Click the URL**
2. Click "**Visit Site**" on ngrok warning page
3. **Wait 10-20 seconds** (downloading AI model)
4. 🎉 **4Real homepage appears!**

✅ **SUCCESS! It's running!**

---

# Part 5: Test Your App

## Test 1: Check Plagiarism

1. Click "**🔍 Check Plagiarism**" tab
2. Paste this in LEFT box:
   ```
   The quick brown fox jumps over the lazy dog. Artificial intelligence is transforming the way we detect copied content.
   ```
3. Paste same text in RIGHT box
4. Click "**🔍 CHECK PLAGIARISM**"
5. Wait 10 seconds
6. You should see: **🚨 HIGH SIMILARITY: 98-100%**

✅ **Works!**

## Test 2: Chatbot

1. Click **💬** button (top-right corner)
2. Type: `How does 4Real work?`
3. Click "**Send 🚀**"
4. Wait 2-3 seconds
5. AI responds!

✅ **Chatbot works!**

---

# 🎉 You're Done!

You have successfully:
- ✅ Set up API keys
- ✅ Configured the project
- ✅ Launched 4Real on Colab
- ✅ Created a public URL
- ✅ Tested plagiarism detection
- ✅ Tested chatbot

**You can now:**
- Share the public URL with anyone
- Use it for demos/presentations
- Test with any documents

---

# ⚠️ Important Notes

## Keep Colab Tab Open
- Don't close the Colab tab with the running code
- If you close it, the app stops
- The public URL becomes inactive

## Session Time Limit
- Google Colab sessions last ~12 hours
- After that, re-run all cells (takes 5 minutes)
- You'll get a NEW public URL

## Running It Again
Next time you want to use 4Real:
1. Open your saved Colab notebook
2. Click "Runtime" → "Run all"
3. Wait 3-4 minutes
4. Copy the new public URL
5. Done!

---

# 🔧 Troubleshooting

## Problem: "API key not configured"
**Solution:** Check config.py - make sure you saved it with your real keys

## Problem: "Model download failed"
**Solution:** Check internet connection, wait 1 minute, run the last cell again

## Problem: "URL doesn't open"
**Solution:** Click "Visit Site" on the ngrok warning page

## Problem: "Nothing happens when clicking CHECK PLAGIARISM"
**Solution:** Wait longer (first run takes 20-30 seconds to download model)

## Problem: "Packages won't install"
**Solution:** 
1. Restart runtime: "Runtime" → "Restart runtime"
2. Run all cells again from Step 2

---

# 📞 Need Help?

If you're stuck:
1. Check which step failed
2. Read the error message carefully
3. Try running that cell again
4. Make sure API keys are correct in config.py

---

# 🎯 Quick Reference Card

**To run 4Real:**
```
1. Go to Colab notebook
2. Runtime → Run all
3. Wait 3-4 minutes
4. Copy public URL
5. Share & use!
```

**Files needed:**
- 4real_app.py (main app)
- chatbot.py (chatbot functionality)
- config.py (API keys)

**Keys needed:**
- OpenAI API Key (for chatbot)
- Ngrok Auth Token (for public URL)

---

**Project by Group 4Real**  
BAXI3413 Natural Language Processing  
Universiti Teknikal Malaysia Melaka (UTeM)