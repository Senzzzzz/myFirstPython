import random
import time
import json
import datetime
import requests
import ollama

conversation_history = ""


def get_ai_response(user_input):
    global conversation_history
    client = ollama.Client()

    conversation_history += f"\nMe: {user_input}\nElena: "
    model = "llama3"
    prompt = conversation_history

    response = client.generate(model=model, prompt=prompt)
    return response.response


current_date = datetime.datetime.now().strftime("%y/%m/%d")
with open("chatbot/chatlogs.txt", "a") as file:
    file.write(f"---------New Chat({current_date})--------\n")
while True:
    user = input("Enter a message: ").lower()

    response = get_ai_response(user)
    print(f"Elena: {response}")

    with open("chatbot/chatlogs.txt", "a") as file:
        file.write(f"{current_date} Me: {user}\n")
        file.write(f"{current_date} Elena: {response}\n")
