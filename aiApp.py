import os
import openai


openai.api_key = os.getenv("OPENAI_API_KEY")

while True:
  question = input("\033[34mWhat is your question?\n")

  if question.lower() == "exit":
    print("\033[31mGoodbye!\n033[0m")
    break
    
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages= [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": question}
    ]
  )
  print(completion.choices[0].message.content+"\n")
  