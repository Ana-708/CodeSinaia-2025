import ollama

class SmartAgent:

    model_name = "gemma3:1b"

    def __init__(self):
        print("Agent is created")
        self.chat_log = []
        self.update_context()

    def update_context(self):
        with open("./IntroToLLM/context_prompt.txt", "r", encoding="utf-8") as f:
            context_text = f.read()
        self.context_prompt = {"role": "system", "content": context_text}

    def chat(self, user_input):
        self.update_context() 
        messages = [self.context_prompt] + self.chat_log + [{"role": "user", "content": user_input}]
        response = ollama.chat(
            model=self.model_name,
            messages=messages
        )
        self.chat_log.append({"role": "user", "content": user_input})
        self.chat_log.append({"role": "assistant", "content": response['message']['content']})
        return response['message']['content']
