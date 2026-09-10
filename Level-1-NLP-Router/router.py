#technojam ai easy task NLP ROUTER
#Ridham Singhal , 26SCSE1010788

STOPWORDS = ["is", "the","at", "and", "to", "a", "for", "my", "i" ]

def tokenizing_text(user_input):
    words = user_input.lower().split()
    return words


def removing_words(words):
    clean_words = []
    for word in words:
        if word not in STOPWORDS:
            clean_words.append(word)
    return clean_words

def routing(clean_words):
    for word in clean_words:
        if word in ["crash", "bug", "broken", "error"]:
            return "Technical support"
        elif word in ["bill", "charged", "payment", "subscription"]:
            return "Billing support"
    return "General Enquiry"


# I thought i should first make modular functions for each task and then take the input at last instead of taking input at the start and then passing it to each function. This way, the code is more organized and easier to read.
user_input = input("Please enter your query:")

tokenize = tokenizing_text(user_input)
clean = removing_words(tokenize)
route = routing(clean)

print("Cleaned Words:", clean)
print("Routed To:", route) 
