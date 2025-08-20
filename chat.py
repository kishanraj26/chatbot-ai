import google.generativeai as genai


# Hardcode API key
api_key = "AIzaSyDPBuKf8J8YNy1tsgSxeMimkNrBs-GC888"
genai.configure(api_key=api_key)


# Define generation config
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}


# Initialize the Gemini model
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    generation_config=generation_config,
)


# Initialize chat history
history = []


print("Bot: Hello, how can I help you?")


# Start the chat session
chat_session = model.start_chat(history=history)


while True:
    user_input = input("You: ")
    response = chat_session.send_message(user_input)
    model_response = response.text
    print(f"Bot: {model_response}")
    print()


    # Update the history
    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [model_response]})
    chat_session = model.start_chat(history=history)
