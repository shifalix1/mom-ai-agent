# -----GROQ-----
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

# Groq (active)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_ai_reply(message):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": message}]
    )
    return response.choices[0].message.content

# -----CLAUDE-----

#import anthropic
# from google import genai  ← swap this back if switching to Gemini later
#from dotenv import load_dotenv
#import os

#load_dotenv()

# Claude Active
#client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

#def get_ai_reply(message):
#    response = client.messages.create(
#        model="claude-haiku-4-5-20251001",
#        max_tokens=1024,
#        messages=[{"role": "user", "content": message}]
#    )
#    return response.content[0].text


# -----GEMINI-----

#import google.generativeai as genai
#from google import genai
#from dotenv import load_dotenv
#import os

#load_dotenv()

# Configure client with API key
#client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# This function takes a message and returns AI's reply
#def get_ai_reply(message):
#    response = client.models.generate_content(
#        model="gemini-2.0-flash",
#        contents=message
#    )
#    return response.text

# Configure Gemini with your API key
#genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load the gemini model
#model = genai.GenerativeModel("gemini-1.5-flash")

# This function takes a message and returns AI's reply
#def get_ai_reply(message):
#    response = model.generate_content(message)
#    return response.text'''