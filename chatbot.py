from google import genai

# Create client
client = genai.Client(api_key="API")

# Create chat session

chat = client.chats.create(
    model="gemini-2.5-flash-lite",
    config={
        "system_instruction":
        "You are a conversational assistant. Use information provided earlier in the current conversation when answering questions about the conversation."
    }
)

print("Gemini Chatbot")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break   

    try:
        response = chat.send_message(user_input)

        print(f"\nGemini: {response.text}\n")

    except Exception as e:
        print(f"\nError: {e}\n")