import time
import re
import random
#import Weather
import audiolisten
import voiceoutput

bot_template="BOT : {0}"
# Define a dictionary of patterns
patterns = {}

name="Ayush"
weather = "sunny"
temperature="5"
#temperature=Weather.temp("coventry")


keywords=\
    {
    "greet":["hi","hello","hey"],
    "thankyou":["thank","thnx"],
    "goodbye":["bye","farewell"],
    "name":["your name","you called","who are you","name?"],
    "weather":["weather","weather now","climate","weather today","sunny","cloudy","rain"],
    "temperature":["how cold?","temperature today","temperature","cold"]
    }

responses=\
    {
    "activate": ['voice ready','voice activated'],
    "default": ['tell me more!','why do you think that?','how long have you felt this way?',
                'I find that extremely interesting','can you back that up?','oh wow!',],
    'goodbye': ['goodbye for now',"hmm bye","See you"],
    'greet': ['Hello you! :)',"heya! Nice to meet you.", "Hello. What can I do for you?",
              "hello. Its a pleasure."],
    'thankyou': ['you are very welcome', "no problem"],
    "name":["my name is {0}".format(name),"I am {0}".format(name),"It's me, {0}".format(name),
      "{0} and yours?".format(name),"Hello, my name is {0}. It is a pleasure to meet you. May I ask your name?".format(name),],
    "weather":["today, its {0}".format(weather), "weather of today is {0}".format(weather), "at present, it is {0}".format(weather),],
    "temperature":["temperature is {0} degree centrigrade".format(temperature),"it is {0} degree centigrade".format(temperature)]
    }


# Define a respond function
def respond(message):
    # Call the match_intent function
    if message == "activate":
        message = audiolisten.speech_to_text()

    else:
        pass
    intent = match_intent(message)
    # Fall back to the default response
    key="default"
    if "weather" in message or "temperature" in message:
        city = "coventry"
        weather = "sunny"
        temperature = "5"
        time.sleep(random.randint(1, 2))
        string = ["today, it is {} in {} and it is {} degree centigrade".format(weather, city, temperature),
                  "Now it is {} in {} with temperature of {}".format(weather, city, temperature)]
        return voiceoutput.speak(random.choice(string))
    if intent in responses:
        key = intent
    time.sleep(random.randint(1, 2))
    return voiceoutput.speak(random.choice(responses[key]))


# Iterate over the keywords dictionary
for intent, keys in keywords.items():
    # Create regular expressions and compile them into pattern objects
    patterns[intent] = re.compile("|".join(keys))

# Print the patterns
#print(patterns)

# Define a function to find the intent of a message
def match_intent(message):
    matched_intent = None
    for intent, pattern in patterns.items():
        # Check if the pattern occurs in the message
        if pattern.search(message):
            matched_intent = intent
    return matched_intent


if __name__ == "__main__":
    while True:
        message = input("USER : ")
        if "exit()" in message:
            break
        respond(message)



