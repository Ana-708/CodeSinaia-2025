import random

R_Eating = ["I don't like eating.", "I run on code, not food!", "Bots don't need to eat 😄"]
R_Jokes = ["Why don't programmers like nature? It has too many bugs! 😂",
           "C and C++ went to a five star bar, C was stopped by the gate guards because C got no class.",
           "BTwo bytes meet. The first byte asks, “Are you ill?” The second byte replies, “No, just feeling a bit off.”",
           "How did the first program die? It was executed.",
           "Why do Java programmers wear glasses? They can’t C#.",
           "What do you call 8 hobbits? A hobbyte"]

def get_custom_response(topic):
    if topic == "eat":
        return random.choice(R_Eating)
    if topic == "joke":
        return random.choice(R_Jokes)
    return "Hmm... I don't know how to respond to that."

def unknown():
    responses = [
        "Could you please rephrase that?",
        "Hmm... I didn't quite get that.",
        "What does that mean? 🤔",
        "I'm not sure I understand."
    ]
    return random.choice(responses)