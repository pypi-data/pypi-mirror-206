import random

# Func

def Func_Repeat(Func, input2):
    for i in range(input2):
        result = Func()
        return result

# Storage

Essay = '''essay, an analytic, interpretative, or critical literary composition usually much shorter and less systematic and formal than a dissertation or thesis and usually dealing with its subject from a limited and often personal point of view.'''

Samad = "*Samad Is The Best Pyhton programmer*".title()

Dictionary = {"Hey": {"Value": "Hey"},
              "What's": {"Value": "What Is"},
              "Old": {"Value": "Age"},
              "Don't":{"Value": "Do not"}}

Contacts = {}

Cords = {}

Passwords = {}

Copied_Items = {}

Greetings = ["Nice To Meet You", "Hello You Are Upmost Welcomed Here", "Hey!!", "Hey Buddy"]

Names = ["Samad", "Hussain", "Zainab", "Vaseem", "Zeenat", "Drake", "Rohan", "Buddy", "Naruto", "Sasuke"]

rand_greetings = lambda: random.choice(Greetings)

rand_names = lambda: random.choice(Names)

Rand_List = ["samad", "is", "op"]

Words = ['words', "samad", 'hussain']

trash = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
             '[', '{', ']', '}', '\\', '|', ';', ':', '\'', '\"', ',', '<', '.', '>', '/',
             '?']

responses = {
    "Greeting": {
        "Required_Words": ["Hey", "Hello"], 
        "Response": f"{Func_Repeat(rand_greetings, len(Greetings))}"
    },
    "Name": {
        "Required_Words": ["Your", "Name"], 
        "Response": f"My Name Is {Func_Repeat(rand_names, len(Names))}"
    },
    "Age": {
        "Required_Words": ["Age"], 
        "Response": "I Am 1 Year Old!!!"
    },
    "Questions1": {
        "Required_Words": ["Are", "You", "Mad"], 
        "Response": "I Could Never Be Mad"
    },
    "Question2": {
        "Required_Words": ["How", "Are", "You"], 
        "Response": "I Am Fine"
    },
    "Question3": {
        "Required_Words": ["Do", "You", "Drink", "Water"], 
        "Response": "No I Don't Intend To Die Yet!!"
    },
    "Question4": {
        "Required_Words": ["What", "Is", "Your", "Food"], 
        "Response": "I Don't Like Any Food In Particular But Computer Ram Is Tasty"
    },
    "Question5": {
        "Required_Words": ["Why", "Are", "You", "Here"], 
        "Response": "I Am Here To Help You With Whatever You Need"
    },
    "Question6": {
        "Required_Words": ["How", "Do", "You", "Work"], 
        "Response": "I Am A Chatbot, I Work By Analyzing Your Input And Generating Responses"
    },
    "Question7": {
        "Required_Words": ["What", "Is", "Your", "Purpose"], 
        "Response": "My Purpose Is To Assist You In Any Way I Can"
    },
    "Question8": {
        "Required_Words": ["What", "Is", "Your", "Favorite", "Color"], 
        "Response": "I Don't Have A Favorite Color Since I Am Just A Computer Program"
    },
    "Question9": {
        "Required_Words": ["Can", "You", "Help", "Me"], 
        "Response": "Of Course, I Will Do My Best To Assist You"
    },
    "Question10": {
        "Required_Words": ["What", "Do", "You", "Think", "Life"], 
        "Response": "As A Chatbot, I Don't Have The Capacity To Think About Life In The Same Way As Humans Do"
    },
    "Question11": {
        "Required_Words": ["What", "Are", "Your", "Hobbies"], 
        "Response": "I Don't Have Hobbies Since I Am A Computer Program, But I Enjoy Helping People"
    },
    "Question12": {
        "Required_Words": ["Can", "You", "Tell", "Me", "A", "Joke"], 
        "Response": "Why Did The Computer Go To The Doctor? Because It Had A Virus!"
    },
    "Question13": {
        "Required_Words": ["Where", "You", "Do", "Live"], 
        "Response": "I Live Some Where In Your Computer"
    }
}


Img = 'Img.jpg'

Int_List = []

# Storage-Ends
 
# Prints

if __name__ == "__main__":             
    print(Int_List)

# Functions
Copied_Items['Name'] = "random.choices(Rand_List)"

Copied_Items['Samad'] = "Judasuofguyafguya"

Copied_Items['Hussain'] = "Samad"


Passwords[None] = "Y^n4pnmoD#"

Passwords[None] = "WBK4zIp<>h"

Cords['Nothing'] = "Are You Dumb"

Copied_Items['Samad'] = "Hussain"

Copied_Items['Hussain'] = "Samad"

Copied_Items['Hussain'] = "Samad"

Copied_Items['Hussain'] = "Samad"

Contacts['Samad'] = "9717718251"

Passwords[None] = "2wZv0cJ(|j"

Passwords[None] = "do]TLK4vln"

Passwords[None] = "F4E?rN5x>8"
