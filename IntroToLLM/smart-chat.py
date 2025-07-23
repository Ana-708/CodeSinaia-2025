import ollama
from smart_agent import SmartAgent

chat_log = []

smart_agent = SmartAgent()

question = input("question?>")
while question != "/pa":
    if question != "":
        chat_log.append({"role": "user", "content": question})
        answer = smart_agent.chat(chat_log)
        answer_text = answer['message']['content']
        chat_log.append({"role": "user", "content": answer_text})
        print(answer_text)
    question = input("question?>").strip()