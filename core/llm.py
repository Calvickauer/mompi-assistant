# core/llm.py
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

conversation_history = []

def ask_openai(prompt: str) -> str:
    global conversation_history
    conversation_history.append({"role": "user", "content": prompt})
    if len(conversation_history) > 6:
        conversation_history = conversation_history[-6:]

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=conversation_history,
            max_tokens=1024,
            temperature=0.7
        )
        reply = response.choices[0].message.content.strip()
        conversation_history.append({"role": "assistant", "content": reply})
        return reply
    except Exception as e:
        return f"[Error calling GPT API: {e}]"
