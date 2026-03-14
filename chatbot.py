import os
from openai import OpenAI

client = OpenAI(api_key="your-api-key-here")

def chat(user_message, business_context):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are a helpful customer service assistant for {business_context}"},
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content

business = "a local pizza restaurant called Mario's Pizza"
while True:
    user_input = input("Customer: ")
    print("Bot:", chat(user_input, business))


