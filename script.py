from google import genai

client = genai.Client(api_key="API")

while True:
    prompt = input("You: ")

    if prompt.lower() == "exit":
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    print("\nGemini:", response.text)