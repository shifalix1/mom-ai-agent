import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

# Configure Gemini with your API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load the gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# This function takes a message and returns AI's reply
def get_ai_reply(message):
    response = model.generate_content(message)
    return response.text