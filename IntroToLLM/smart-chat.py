from smart_agent import SmartAgent

chat_log = []

smart_agent = SmartAgent()

question = input("question?>").strip()
while question != "/pa":
    if question != "":
        answer = smart_agent.chat(question)
        print(answer)
    question = input("question?>").strip()
