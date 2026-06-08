from google import genai

client = genai.Client(api_key="API")

print("Gemini Chatbot")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=user_input
    )

    print("\nGemini:", response.text)
    print()