# -----GROQ-----
from groq import Groq
from dotenv import load_dotenv
from prompt import get_system_prompt
from memory import load_memory, add_to_memory
from datetime import datetime
import os

client = None

load_dotenv()

# Groq (active) removed since jenkins was crashing added beneath

def get_ai_reply(message):
    from groq import Groq
    import os
    from datetime import datetime

    add_to_memory("user", message)
    history = load_memory()

    # detect time question
    is_time_query = any(word in message.lower() for word in ["time", "baje", "kitne baje"])

    # clear memory for time questions
    if is_time_query:
        history = []

    api_key = os.getenv("GROQ_API_KEY")

    # Jenkins fallback (no API key)
    if not api_key:
        reply = "haanji mumma 😊"
        add_to_memory("assistant", reply)
        return reply

    client = Groq(api_key=api_key)

    current_time = datetime.now().strftime("%H:%M")

    # build messages properly
    messages = [
        {"role": "system", "content": get_system_prompt()}
    ]

    if is_time_query:
        messages.append({
            "role": "system",
            "content": f"Current time is {current_time}. Answer time questions correctly."
        })

    messages += history

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0.7,
        messages=messages
    )

    reply = response.choices[0].message.content
    add_to_memory("assistant", reply)

    return reply

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