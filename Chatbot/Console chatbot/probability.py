import re
from responses import get_custom_response, unknown
RULES = [
    {
        "keywords": ["hello", "morning", "night", "afternoon","hi", "hii", "hiii", "hiiii", "hey", "heyy", "heyyy", "heyyyy", "hei", "salut"],
        "response": "Hello! 😊",
        "single_response": True
    },
    {
    "keywords": ["how", "are", "you", "doing", "how's", "your", "day", "what's", "up", "what"],
        # "required": ["you"],
        "response": "I'm doing fine, and you?"
    },
    {
        "keywords": ["what", "is", "your", "name", "what's"],
        "required": ["name"],
        "response": "I'm CodePal, your friendly chatbot 🤖"
    },
    {
        "keywords": ["who", "are", "you"],
        "required": ["who", "you"],
        "response": "I'm CodePal, your friendly chatbot 🤖"
    },
    {
        "keywords": ["i", "love", "like", "code", "palace", "you"],
        "required": ["code"],
        "response": "Thank you! ❤️"
    },
    {
        "keywords": ["what", "like", "do", "you", "to", "eat"],
        "required": ["eat"],
        "response": lambda: get_custom_response("eat")
    },
    {
        "keywords": ["bye", "goodbye", "see"],
        "response": "Goodbye! 👋",
        "single_response": True
    },
    {
        "keywords": ["help", "assist", "support"],
        "response": "How can I assist you today?",
        "single_response": True
    },
    {
        "keywords": ["joke", "funny", "humor", "laugh"],
        "response": lambda: get_custom_response("joke"),
        "single_response": True
    },
    {
        "keywords": ["weather", "forecast"],
        "response": "I can't check the weather, but I hope it's nice where you are! ☀️",
        "single_response": True
    },
    {
        "keywords": [],
        "response": unknown(),
        "single_response": True
    },
    ###########################################
    {
        "keywords": ["my", "name", "is"],
        "required": ["my","name"],
        "response": "Nice to meet you! 😊",
    },
]

def message_probability(user_message, keywords, single_response=False, required=[]):

    #TODO: Calculează probabilitatea mesajului message_certainty
    #pt fiecare cuvant din mesaj care apare in recognised_words
    #message_certainty este incrementat
    message_certainty = 0

    for word in user_message:
        if word in keywords:
            message_certainty += 1
    
    #TODO: Calculează match_ratio ca raportul dintre message_certainty și numărul de cuvinte din keywords
    #dacă keywords este gol, setăm match_ratio la 0
    match_ratio = message_certainty / len(keywords) if keywords else 0
    
    
    if required:
        if not all(word in user_message for word in required):
            return 0
        
    match_ratio = match_ratio

    if single_response:
        return 1 if match_ratio > 0 else 0
    
    return int(match_ratio * 100) if match_ratio > 0 else 0

       
    # if len(keywords) > 0:
    #     match_ratio = message_certainty / len(keywords)
    # else:
    #     match_ratio = 0






def check_all_messages(message):
    highest_prob = 0
    best_response = None

    for rule in RULES:
        None
        
        #TODO: Calculează probabilitatea mesajului pentru fiecare regulă
        #folosind funcția message_probability definită mai sus
        prob = message_probability(message, rule["keywords"], rule.get("single_response", False), rule.get("required", [])) #??
        
        #TODO: dacă prob este mai mare decât highest_prob,
        # actualizează best_response și highest_prob
        if prob > highest_prob:
            best_response = rule["response"]
            highest_prob = prob
    
    if(callable(best_response)):
        return best_response()  # Apelează funcția dacă best_response este o funcție
    #TODO: returneaza raspunsul, fie cel de eroare, fie cel gasit 
    if best_response is not None:
        return best_response
    else:
        return unknown()
    

def get_response(user_input):
    None
    #TODO: Verifică dacă user_input este gol sau conține doar spații
    if not user_input.strip():
        return "Please enter a message."

    #TODO: apeleaza functia split pentru a împărți mesajul în cuvinte 
    user_message = re.split(r'\s+|[,;?.-]\s*', user_input.lower())
    
    # apoi returneaza rezultatul obtinut folosind check_all_messages pentru a verifica mesajul
    return check_all_messages(user_message)

# Ce inseamna \s+|[,;?.-]\s*?
# \s+ înseamnă unul sau mai multe spații albe (inclusiv tab-uri și linii noi)
# | este operatorul "sau" în expresiile regulate
# [,;?.-] înseamnă oricare dintre caracterele specificate (
# virgulă, punct și virgulă, punct, semn de întrebare sau cratimă)
# \s* înseamnă zero sau mai multe spații albe după aceste caractere
# deci, expresia întreagă împarte mesajul în cuvinte folosind spațiile albe și semnele de punctuație specificate
# de exemplu, "Hello, world! How are you?" va fi împărțit în
# ["hello", "world", "how", "are", "you"]