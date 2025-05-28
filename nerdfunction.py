import openai
import os

# Set your OpenAI API key

openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.api_key)
# Recommended: Use environment variable
# Or you can directly set it like this:
# openai.api_key = "YOUR_API_KEY_HERE"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use "gpt-3.5-turbo" if you don't have GPT-4 access
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=100,
        n=1,
        temperature=0.7,
    )
    return response.choices[0].message['content']

# Example usage
prompt = "Hello, how do I become a good programmer?"
response_text = chat_with_gpt(prompt)
print(response_text)