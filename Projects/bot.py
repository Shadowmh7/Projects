import openai

# Replace with your OpenAI API key
openai.api_key = "your_openai_api_key"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",  # You can use other models like gpt-3.5-turbo or gpt-4
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

def chat_with_gpt():
    print("GPT-3 Chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        prompt = f"You: {user_input}\nBot:"
        response = generate_response(prompt)
        print(f"Bot: {response}")

if __name__ == "__main__":
    chat_with_gpt()
