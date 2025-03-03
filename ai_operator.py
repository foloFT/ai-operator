# ai_operator.py
import os
from dotenv import load_dotenv
from openai import OpenAI
from anthropic import Anthropic

# Carica le variabili d'ambiente 
load_dotenv()

# Inizializza i client con le API keys ottenute dalle variabili d'ambiente
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def get_chatgpt_response(prompt):
    """Ottieni risposta da ChatGPT"""
    try:
        response = openai_client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Errore con ChatGPT: {str(e)}"

def get_claude_response(prompt):
    """Ottieni risposta da Claude"""
    try:
        response = anthropic_client.messages.create(
            model="claude-3-7-sonnet-20250219",
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text
    except Exception as e:
        return f"Errore con Claude: {str(e)}"

def process_query(user_prompt):
    """Funzione principale che interroga entrambe le AI"""
    # Ottieni risposte da entrambi i modelli
    chatgpt_response = get_chatgpt_response(user_prompt)
    claude_response = get_claude_response(user_prompt)
    
    # Restituisci entrambe le risposte
    return {
        "chatgpt": chatgpt_response,
        "claude": claude_response
    }
