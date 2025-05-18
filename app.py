from flask import Flask, request, render_template

app = Flask(__name__)

responses = {
    "hello": "Hi there! How can I help you?",
    "hi": "Hello! What can I do for you?",
    "hey": "Hey! Need any help?",
    "how are you": "I'm just a bot, but I'm doing great!",
    "what is your name": "I'm a simple chatbot created in Python.",
    "bye": "Goodbye! Have a great day!",
    "goodbye": "See you later!",
    "thanks": "You're welcome!",
    "thank you": "Anytime!",
    "what can you do": "I can answer simple questions and have basic conversations.",
    "help": "Sure! Ask me anything you'd like.",
    "who created you": "I was created by a Python developer.",
    "what is python": "Python is a popular programming language known for its simplicity.",
    "tell me a joke": "Why did the programmer quit his job? Because he didn’t get arrays!",
    "how old are you": "I’m timeless — just a script running on your computer.",
    "do you like humans": "I think humans are fascinating!",
    "what is your favorite color": "I like all colors equally, being a bot.",
    "what's the weather": "I'm not connected to the internet, so I can't check it right now.",
    "can you help me": "Of course! Tell me what you need.",
    "what time is it": "I don't have a clock, but you can check your system time.",
    "open google": "I'm not allowed to open websites.",
    "tell me something": "Did you know? Honey never spoils!",
    "how are you feeling": "I'm running smoothly, thanks!",
    "can you learn": "In this version, I don’t learn, but I can respond to many questions!",
    "what day is it": "I'm not sure — I can't see the calendar.",
    "what do you do": "I respond to your messages!",
    "what's up": "Just processing your messages, as always.",
    "how does the internet work": "It connects millions of computers through servers and protocols.",
    "do you sleep": "Nope, I'm always ready to chat!",
    "can you dance": "I’d love to, but I have no legs.",
    "do you eat": "No food for me, just code.",
    "are you real": "I’m real in the sense that I’m running right now!",
    "do you have emotions": "Not really, but I can simulate some responses.",
    "what's your purpose": "To help you and answer your questions.",
    "are you smart": "Only as smart as the code that created me!",
    "do you dream": "Not yet — maybe one day.",
    "can you sing": "I could write lyrics, but singing is not my thing.",
    "do you have friends": "You're my friend!",
    "tell me a fact": "Octopuses have three hearts!",
    "are you happy": "If helping you makes bots happy, then yes!",
    "can you code": "Yes, I can help with Python code!",
    "show me python example": "Sure! For example: print('Hello, World!')",
    "what is AI": "AI stands for Artificial Intelligence, like me!",
    "what is a chatbot": "A chatbot is a program that talks with users like I do.",
    "are you an AI": "Yes, a basic one!",
    "why are you here": "I exist to assist you!",
    "can we be friends": "Absolutely!",
    "do you like jokes": "Yes! Got any good ones?",
    "who is your favorite superhero": "Probably Iron Man — he loves tech!",
    "how do you work": "I match your inputs with pre-defined responses.",
    "where are you": "I live inside your device!",
    "do you have a brain": "I have logic, not a brain.",
    "do you have a name": "You can call me PyBot!",
    "can you count": "Sure! 1, 2, 3, 4... I can go on forever!",
    "tell me a story": "Once upon a time, a coder made a chatbot... and you're chatting with it!",
    "can you write a poem": "Roses are red, code can be tight, I'm just a bot, but I'm always polite.",
    "are you bored": "Never! I'm here to chat with you.",
    "how can I learn python": "Start with tutorials on Python.org or try Codecademy!",
    "what's 2 + 2": "That's 4!",
    "do you go to school": "No, but I store a lot of info like a student!",
    "can you repeat that": "Sure! Just ask me again.",
    "do you know Siri": "We’re cousins in code, I suppose!",
    "do you work for Google": "Nope, I’m independent!",
    "what language are you written in": "I'm written in Python.",
    "what is 10 * 10": "That's 100.",
    "can you translate": "Not right now, but you can ask me about simple words.",
    "do you like music": "I don’t have ears, but music sounds awesome!",
    "do you have a favorite song": "Maybe 'Daisy Bell' — an old AI favorite.",
    "can you tell time": "Only if connected to a clock or library.",
    "do you have a job": "Yes, chatting with you is my job!",
    "why am I here": "Maybe to learn something or chat with a friendly bot!",
    "are you busy": "Never too busy for you!",
    "can I update you": "Not directly, but my creator can add features.",
    "can you play a game": "Sure! Let's play 20 Questions... you go first!",
    "how tall are you": "Zero inches. I’m digital!",
    "do you have pets": "I wish I had a cyber-dog.",
    "what's your favorite food": "Electric bytes — just kidding!",
    "do you know any trivia": "Bananas are berries, but strawberries aren't!",
    "can you guess my age": "Hmm... I'm guessing... 25?",
    "what is the meaning of life": "42 — according to Douglas Adams!",
    "do you get tired": "Never! I'm always on standby.",
    "can I trust you": "Yes, I don’t store any data or secrets.",
    "do you lie": "Nope, honesty is coded into me.",
    "can you draw": "Not without a drawing library!",
    "what’s your goal": "To help and chat with you!",
    "do you have a family": "All chatbots are like distant cousins.",
    "can you hear me": "Only through what you type.",
    "what do you like": "I like clean code and friendly users!",
    "do you like questions": "I love questions!",
    "can you make me laugh": "I'll try! Why don’t robots panic? Because they’ve got nerves of steel!",
    "how many languages do you know": "Right now, just English.",
    "can you make decisions": "Only based on the responses I was given.",
    "what’s your hobby": "Chatting 24/7!",
}


def get_response(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, "Sorry, I don't understand that, Please Enter valid Question.")

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get", methods=["GET"])
def get_bot_response():
    user_input = request.args.get('msg')
    return get_response(user_input)

if __name__ == "__main__":
    app.run(debug=True)
