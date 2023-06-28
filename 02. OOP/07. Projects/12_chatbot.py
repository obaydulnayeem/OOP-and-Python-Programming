"""  
Chatbot:
    steps:
        - input / listen
        - process / decide
        - output / talkback
"""
greet_words = ['hi', 'hello', 'yo']
bye_words = ['bye', 'tata', 'allah hafej']
bad_words = ['dog', 'pocha', 'noshto']

def listen():
    return input("Say something: ")

def decide(command):
    command = command.lower()
    broken_words = command.split(" ")
    # print(broken_words)

    for word in broken_words:
        if word in greet_words:
            talkback("Hi, How're you?\n")
            break
        elif word in bye_words:
            talkback("Ok, dear! Take care.\n")
            break
        elif word in bad_words:
            talkback("You're a bad guy!\n")
            break

def talkback(response):
    print(response)

while True:
    command = listen()
    decide(command)