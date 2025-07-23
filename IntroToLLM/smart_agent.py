import ollama

class SmartAgent:

    model_name = "gemma3:1b"

    def __init__(self):
        print("Agent is created")

    def chat(self, chat_log):
        answer = ollama.chat(
            model=self.model_name,
            messages=chat_log)
        return answer