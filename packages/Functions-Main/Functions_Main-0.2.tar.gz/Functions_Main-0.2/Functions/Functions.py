import random
import time
import os
import shutil
import string
from DataBase import *
import DataBase
from PIL import Image

    
def DataBase_Save(dict, key, value):
    os.chdir(r"C:\Users\Intel\AppData\Local\Programs\Python\Python311")
    Dict = f"{dict}"
    Dict2 = f"{[key]}"
    Dict3 = f' = "{value}"'
    Dict4 = Dict + Dict2 + Dict3
    with open(f'DataBase.py', 'a') as f:
        f.write(f"\n{Dict4}\n")



def Last(words):
    if type(words) == str:
        f = len(words.split())
        if f > 2:
            word_l = []
            for word in words:
                word_l.append(word)
            
            if word_l[-1] == word_l[-2]:
                del(word_l[-1])
                return ''.join(word_l)
            else:
                return ''.join(word_l)
    elif type(words) == str:
        f = len(words.split())
        if f < 2:
            words_l_s = []
            for word in words:
                words_l_s.append(word)    

            if words_l_s[-1] == words_l_s[-2]:
                del(words_l_s[-1])
                return ''.join(words_l_s)
            else:
                return ''.join(words_l_s)
            
    elif type(words) == list:
        if words[-1] == words[-2]:
            del(words[-1])
            return words
        else:
            return words


def Pass_Maker(Name, length):
    Name = Last(Name)
    rand1 = ''.join(random.choices(f'{string.ascii_letters}', k=3))
    rand2 = ''.join(random.choices(f'{string.ascii_lowercase}', k=3))
    rand3 = ''.join(random.choices(f'{string.punctuation}', k=3))
    rand4 = ''.join(random.choices(f'{string.digits}', k=3))
    rand5 = ''.join(random.choices(f'{string.ascii_uppercase}', k=3))
    password = rand1 + rand2 + rand3 + rand4 + rand5
    password = list(password)
    random.shuffle(password)
    Password = ''.join(password[:length])
    print(f"Pass: {Password}")
    DataBase_Save("Passwords", Words_Capitalzer(Name), Password)
    return Password


def random_Items(List, no):
    List2 = List
    for i in range(no):
        rint = random.randint(1, 3)
        d = ''.join(random.choices(f'{string.ascii_letters}', k=rint))
        List2.append(d)

    return List2


def coder(str):
    if (len(str) <= 3):
        random_number = ''.join(random.choices('abcdefghijklmnopqrstwxyz', k=3))
        random_number_2 = ''.join(random.choices('abcdefghijklmnopqrstwxyz', k=3))
        str = str.lower()
        str_reverse = str[::-1]
        Encoded = random_number + str_reverse + random_number_2
        print(f"Your Encoded String Is: {Encoded}")
    elif (len(str) > 3):
        random_number = ''.join(random.choices('abcdefghijklmnopqrstwxyz', k=3))
        random_number2 = ''.join(random.choices('abcdefghijklmnopqrstwxyz', k=3))
        str = str.lower()
        str_reverse = str[::-1]
        Encoded = random_number + str_reverse + random_number2
        print(f"Your Encoded String Is: {Encoded}")


def decoder(str):
    if (len(str) > 3):
        eject = str[0:3]
        eject2 = str[-3:-1]
        Encoded = str[3:-3]
        Encoded = Encoded[::-1]
        Decoded = Encoded.capitalize()
        print(f"Your Decoded String Is: {Decoded}")
        return Decoded
    elif (len(str) < 3):
        eject = str[0:3]
        eject2 = str[-3:-1]
        Encoded = str[3:-3]
        Encoded = Encoded[::-1]
        Decoded = Encoded.capitalize()
        print(f"Your Decoded String Is: {Decoded}")
        return Decoded


def age2(x: int):
    while True:
        try:
            name = input("Enter your name: ")
            age = int(input("Enter Your Age: "))
            let_Var = f"{name} your age will be {age + x} in {x} years"
            let_Var2 = let_Var.split()
            Final_Print = ""
            for i in range(len(let_Var2)):
                Final_Print = list(Final_Print)
                Final_Print.append(let_Var2[i].capitalize())

            Join = ' '.join(Final_Print)
            print(Join)
            break
        except ValueError:
            print("Enter a Valid Number!!")
            continue


def age1(x: int):
    while True:
        try:
            name = input("Enter your name: ")
            age = int(input("Enter Your Age: "))
            let_Var = f"{name} your age will be {age + x} in {x} years"
            let_Var2 = let_Var.split()
            Final_Print = ""
            for i in range(len(let_Var2)):
                Final_Print = list(Final_Print)
                Final_Print.append(let_Var2[i].capitalize())

            Join = ' '.join(Final_Print)
            print(Join)
            break
        except ValueError:
            print("Enter a Valid Number!!")
            continue


def type_Checker(objects, p=''):
    if p == '':
        return type(objects)
    else:
        print(type(objects))


def Words_Capitalzer(Obj, p=''):
    if p != '':
        if type(Obj) == str:
            String2 = Obj.split()
            Final_Print = ''
            for i in range(len(String2)):
                Final_Print = list(Final_Print)
                Final_Print.append(String2[i].capitalize())

            Join = ' '.join(Final_Print)

            print(Join)
        elif type(Obj) == list:
            Words = []
            for i in range(len(Obj)):
                Words.append(Obj[i].capitalize())

            print(Words)
    elif p == '':
         if type(Obj) == str:
            String2 = Obj.split()
            Final_Print = ''
            for i in range(len(String2)):
                Final_Print = list(Final_Print)
                Final_Print.append(String2[i].capitalize())

            Join = ' '.join(Final_Print)

            return(Join)
         elif type(Obj) == list:
            Words = []
            for i in range(len(Obj)):
                Words.append(Obj[i].capitalize())

            return(Words)


def Words_Upper(Obj, p=''):
    if p != '':
        if type(Obj) == str:
            String2 = Obj.split()
            Final_Print = ''
            for i in range(len(String2)):
                Final_Print = list(Final_Print)
                Final_Print.append(String2[i].upper())

            Join = ' '.join(Final_Print)

            print(Join)
        elif type(Obj) == list:
            Words = []
            for i in range(len(Obj)):
                Words.append(Obj[i].upper())

            print(Words)
    elif p == '':
         if type(Obj) == str:
            String2 = Obj.split()
            Final_Print = ''
            for i in range(len(String2)):
                Final_Print = list(Final_Print)
                Final_Print.append(String2[i].upper())

            Join = ' '.join(Final_Print)

            return(Join)
         elif type(Obj) == list:
            Words = []
            for i in range(len(Obj)):
                Words.append(Obj[i].upper())

            return(Words)

def Words_Lower(Obj):
    if type(Obj) == str:
        String2 = Obj.split()
        Final_Print = ''
        for i in range(len(String2)):
            Final_Print = list(Final_Print)
            Final_Print.append(String2[i].lower())
            
        Join = ' '.join(Final_Print)

        return Join
    elif type(Obj) == list:
        Words = []
        for i in range(len(Obj)):
            Words.append(Obj[i].capitalize())

        return Words



def Vowels_Checker(str):
    Vowels = ["a", "e", "i", "o", "u"]
    Vowels_Count = 0
    index = []
    Final = []
    for words in str:
        if words.lower() in Vowels:
            Samad = str.index(words)
            index.append(Samad)
            Vowels_Count += 1

    for words in index:
        print2 = str[words]
        Final.append(print2)

    let_Printing = Words_Capitalzer(f"no of vowels in your string is {Vowels_Count}")

    let_Printing_Final = print(f"{let_Printing} \n{Final}")

    return let_Printing_Final


def random_Names():
    rand_name = random.choice(Names)
    return rand_name

def Case_Checker():
    u = False
    user = input("Enter the sentence: ")
    cap_user = Words_Capitalzer(user)
    
    if cap_user == user:
        u = True
    else:
        C = []
        for word in user.split():
            if word[0].isupper():
                C.append(word)
    
    if u:
        us = "Capitalized"     
    else:
        us = "Lower"     

    lower_count = 0
    upper_count = 0
    for char in user:
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1

    return f"No. of lowercase letters: {lower_count}, no. of uppercase letters: {upper_count}, sentence type: {us}, no. of words starting with a capitalized letter: {len(C)}"



def name_Ask():
    user = input("Enter Your Name\n")
    return user


def Greeter(name1=''):
    if name1 == '':
        name = name_Ask()
        Greet = random.choice(DataBase.Greetings)
        if Greet == DataBase.Greetings[-1]:
            print(DataBase.Greetings[-1])
        else:
            print(f"{Greet} {name}")
    else:
        Greet = random.choice(DataBase.Greetings)
        if Greet == "Hey Buddy":
            print("Hey Buddy")
        else:
            print(f"{Greet} {name1}")


def guess_number():
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)

    # Keep track of the number of guesses
    num_guesses = 0

    while True:
        # Prompt the user to guess the number
        guess = int(input("Guess the number (between 1 and 10): "))
        num_guesses += 1

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {num_guesses} guesses.")
            break
        # Check if the guess is too high
        elif guess > secret_number:
            print("Too high! Try again.")
        # Check if the guess is too low
        else:
            print("Too low! Try again.")

def Change_Directory(Directory):
    Py_Check = os.path.basename(Directory)
    if Py_Check.endswith(".py"):
        Directory = os.path.dirname(Directory)
        Change_Directory(Directory)
    else:
        os.chdir(Directory)


def Folder_Creator(name, no_of_folders):
    if no_of_folders in [1, 0]:
        os.mkdir(f"{name}")
    else:
        for i in range(no_of_folders):
            os.mkdir(f"{name}-{i + 1}")


def Language_Setup(Lang_name, lang_extension, no_of_folders_, Whose_Tutorial_Are_You_Watching):
    Folder_Creator(Lang_name, 1)
    Change_Directory(f"F:\Samad\Code\Code(Learning)\{Lang_name}")
    time.sleep(2)
    Folder_Creator("Learning", 1)
    time.sleep(1.5)
    Change_Directory(f"F:\Samad\Code\Code(Learning)\{Lang_name}\Learning")
    Folder_Creator(f"{Whose_Tutorial_Are_You_Watching}", 1)
    time.sleep(0.5)
    Change_Directory(f"F:\Samad\Code\Code(Learning)\{Lang_name}\Learning\{Whose_Tutorial_Are_You_Watching}")
    Folder_Creator("Day", no_of_folders_)
    time.sleep(0.5)
    list = os.listdir()
    for i in list:
        Change_Directory(f"F:\Samad\Code\Code(Learning)\{Lang_name}\Learning\{Whose_Tutorial_Are_You_Watching}\{i}")
        with open(f"{i}{lang_extension}", 'w') as f:
            f.write(f" ")
    return "Done"



def random_Response():
    random_list = [
        "Please try writing something more descriptive.",
        "Oh! It appears you wrote something I don't understand yet",
        "Do you mind trying to rephrase that?",
        "I'm terribly sorry, I didn't quite catch that.",
        "I can't answer that yet, please try asking something else."
    ]
    list_count = len(random_list)
    random_index = random.randrange(list_count)
    return random_list[random_index]



def message_filter(message):
    message_list = message.split()
    trash = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
             '[', '{', ']', '}', '\\', '|', ';', ':', '\'', '\"', ',', '<', '.', '>', '/',
             '?']
    filtered_words = []
    for word in message_list:
        filtered_word = ''.join(char for char in word if char not in trash)
        if filtered_word:
            filtered_words.append(filtered_word)

    joined = ' '.join(filtered_words)
    return joined


def get_response(message):
    filtered_message = message_filter(message)
    filtered_message = Words_Capitalzer(filtered_message)
    words = filtered_message.split()
    response_found = False
    if all(word in words for word in ["How", "Are", "You"]):
        response_found = True
        return(Words_Capitalzer("I'm doing well, thank you for asking!"))
    else:
        for i in DataBase.responses:
            if any(word in DataBase.responses["Greeting"]["Required_Words"] for word in words):
                    response_found = True
                    return(DataBase.responses[f"Greeting"]["Response"])
              
            if all(word in words for word in DataBase.responses[i]["Required_Words"]):
                response_found = True
                return(DataBase.responses[f"{i}"]["Response"])
                
        if not response_found:
            return(random_Response())


def Chat_Bot():
    while True:
        user = input("User: ").lower()
        if user.lower() in ["q", "quit", "stop"]:
            print("Bot: Bye")
            return False

        if "what's" in user:
            new = user.replace("what's" , "what is")
            user = new
        
        user_Cap = Words_Capitalzer(user)

        bot = None

        while (bot != ''):
            bot = user_input("User: What Is Your Name")

        print(get_response(user_Cap))

# mage Processing: Use Python's image processing libraries like Pillow and OpenCV to perform tasks like image resizing, cropping, and filtering.


def Image_Funcs(img):
    img = Image.open(f"{img}")
    return img.show()


def user_input(text):
    if text.endswith("\n"):
        user = input(f"{text}")
    elif text.endswith(": "):
        user = input(f"{text}")
    elif text.endswith(" "):
        user = input(f"{text}")
    else:
        user = input(f"{text}\n")
    if not user:
        raise TypeError("No input provided")
    
    return Words_Capitalzer(user)



def Num_Checker(num, r=''):
    if r == '':
        if num % 2 == 0:
            return  "It Is Even"
        else:
            return "It Is Odd"
    elif r != '':
        if num % 2 == 0:
            print("It Is Even")
        else:
            print("It Is Odd")


def Array_Arrranger(Array=list):
    New_Array = sorted(Array)
    Sorted = []
    for i in range(len(New_Array)):
        e_o = Num_Checker(New_Array[i])
        Sorted.append(e_o)
        Sorted.append(New_Array[i])

    print(Sorted)
    return 0

def find_common_integers(list1, list2):
    int_set_1 = set()
    int_set_2 = set()
    for elem in list1:
        if isinstance(elem, int):
            int_set_1.add(elem)
        elif isinstance(elem, str):
            try:
                int_set_1.add(int(elem))
            except ValueError:
                pass  # ignore non-integer strings

    for elem in list2:
        if isinstance(elem, int):
            int_set_2.add(elem)
        elif isinstance(elem, str):
            try:
                int_set_2.add(int(elem))
            except ValueError:
                pass  # ignore non-integer strings

    common_integers = int_set_1.intersection(int_set_2)
    print(list(common_integers))

def Clock(f=''):
    if f != '':
        print(time.ctime())
    else:
        return time.ctime()
    return ''

def Func_Repeat(Func, input2, args = []):
    try:
        for i in range(input2):
            result = Func()
            print(result)
    except TypeError:
        for i in range(input2):
            result = Func(args[0], args[1], args[2])
            print(result)


def Python_Code_Runner(full_file_path_with_py):
    directory_path = os.path.dirname(full_file_path_with_py)
    file_name = os.path.basename(full_file_path_with_py)
    Change_Directory(directory_path)
    os.system(f"python {file_name}")

def list_G(Obj):
    return os.listdir(Obj)


def loc():
    user = user_input("Enter The Location You Wanna But Your File, Enter Nothing If Wanna Save In CWD")
    if user != '':
        Change_Directory(user)
        return True
    else:
        return False

def File_Open(Path, Name_Of_File, Add_r_before_String = '' ):
    Change_Directory(f"{Path}")
    print("Changing The Directory")
    time.sleep(1)
    with open(f"{Name_Of_File}.py", 'r') as f:
        lines = f.readlines()
    user = user_input("Do You Wanna Put It All In A New File").lower()
    if user in ["yes", 'y']:
        file_name = loc()
        print("Analzing User Input")
        time.sleep(1)
        if file_name == True:
            file_names = user_input("Enter The Name Of The New File")
            with open(f"{file_names}.py", 'w') as f:
                print("Creating File")
                time.sleep(1)
                for i in lines:
                    f.write(i)
                print("File Created")
        else:
            with open(f"New_{Name_Of_File}.py", 'w') as f:
                print("Creating File")
                time.sleep(1)
                for i in lines:
                    f.write(i)
                print("File Created")


def Checker(x ,y):
    if x > y:
        print(x) 
    elif y > x:
        print(y) 
    else:
        print(x + y)


def Calculator():
    user = user_input("Enter The Value Seprated By Mathmetic Oprators").lower()
    if "x" in user.lower():
        user = user.replace("x", "*")
        
    result = eval(user)
    return result

def Write_File(full_file_path, Input = '', Var_Check = False, File_Path_Return = ''):
    file_name = os.path.basename(full_file_path)
    directory_path = os.path.dirname(full_file_path)
    Change_Directory(directory_path)
    with open(f"{file_name}", 'w') as w:
            if Var_Check == False:
                w.write(f"while True:\n")
                # w.write(f"  print('{Input}')\n")
                w.write(f"  user = input('User-2: ')\n")
            else:
                # w.write(f"print({Input})\n")
                w.write(f"user = input('User-2: ')\n")

    if File_Path_Return == '':
        return None
    else:
        return full_file_path


def Random_Choice(list):
    return random.choice(list)


def Join(list1, last_chrac = '', opt = ''):
       if opt != '':
           return ''.join(list1)
       if last_chrac != '':
           li = Join(list1[0:-1])
           return li + list1[-1]
       else:
        return ' '.join(list1)    


def shutter(words: str):
    shutter1 = words[0:2]
    return f"{shutter1}... {shutter1}... {words}"


def Greetings(func_name, func_desc):
    print(f"Welcome To {Words_Capitalzer(func_name)}")
    print("-------------------------")
    print(f"{Words_Capitalzer(func_desc)}")
    _ = '_' * len(func_desc)
    print(f"{_}")
    print("Let's Start")
    print("-----------")


def Letter_Repeat(String: str):
    String = String.lower()
    letters = []

    # Iterate through each character in the input string and append it to the list of letters
    for char in String:
        letters.append(char)

    # Create a set of unique letters
    set_letters = set(letters)
    
    
    # Iterate through the list of letters
    for letter in set_letters:
        # Count the occurrences of the letter in the list of letters
        letter_count = letters.count(letter)
        # If the letter appears more than once, print it
        if letter_count > 1:
            return (letter)

def Esssay_Cleaner(Essay):
    if type(Essay) == str:
        H = False
        Essay = Essay.split()
        Cap = Words_Capitalzer(Essay)
        for words in Cap:
            if words in DataBase.Dictionary:
                index = Cap.index(words)
                Cap[index] = DataBase.Dictionary[words]["Value"]
            if words in ["How", "Why", "When", "Whose", "Whom", "Did", "Are"]:         
                index = Cap.index(words)
                Cap.append('?')
                H = True
        
        Last_Check = Last(Cap)
        if H == True:
            Last_Check = Join(Last_Check, 'Sa,ad')
        else:
            Last_Check = Join(Last_Check)
        
        return Last_Check
    
    elif type(Essay) == list:
        Essay = Join(Essay)

def Array_Check_index(Array: list, index = 0):
    try:
        l = []
        for items in Array:
            l.append(items[index])
    except IndexError:
        return("Enter A Vaid Index")

    return Join(l)




def File_Save2(file_name_with_out_py, file_folder_path, dictionary, key, value, age, race, gender):
    os.chdir(f"{file_folder_path}")
    v = "'Password'"
    a = "'Age'"
    r = "'Race'"
    g = "'Gender'"
    Dict = f"{dictionary}"
    Dict2 = f"'{key}'"
    Dict3 = ' = '
    Dict4 = '}'
    Dict23= '{'
    Dict5 = f"{v}: '{value}', {a}: '{age}', {r}: '{race}', {g}: '{gender}'"
    Dict6 = f"{Dict}[{Dict2}] {Dict3} {Dict23}{Dict5} {Dict4}"
    with open(f'{file_name_with_out_py}.py', 'a') as f:
        f.write(f"\n{Dict6}\n")


def Register(dict_name, file_path, file_name):
    Change_Directory(f'{file_path}')
    user = user_input("Set User Name")
    age = user_input("Enter Your Age")
    gender = user_input("Enter Your Gender")
    race = user_input("Enter Your Race")
    password1 = user_input("1 For Custom Password, 2-For Random Password")
    if password1 == '1':
        password = user_input("Enter Your Password")
        print("Password Saved")
        f'{dict_name}'[user] = {'Password': password, 'Age': age, 'Race': race, 'Gender': gender}
    else:
        Random_Pass = Pass_Maker(user, 10)
        print("Password Saved")
        f'{dict_name}'[user] = {'Password': Random_Pass, 'Age': age, 'Race': race, 'Gender': gender}
    File_Save2(f"{file_name}", f"{file_path}", dict_name, user, dict_name[user]['Password'], age, race, gender)


def Input_Checker(value, check):
    if type(check) == str:
        if check == value:
            return True
        else:
            return False
    elif type(check) == list:
        if value in check:
            return True
        else:
            return False

def Login(my_dict, file_path, file_name):
    Change_Directory(file_path)
    Passexsist = False
    while Passexsist == False:
        user_name = user_input("Enter Your User Name: ")
        keys = list(my_dict.keys())
        if user_name in keys:
            password = user_input("Enter Your Password: ")
            if password == my_dict[user_name]['Password']:
                print('Logged In Sucessfully')
                print("1-Age")
                print("2-Race")
                print("3-Password")
                print("4-Gender")
                print("5-All")
                print("6-Messanger")
                print("7-Game")
                user = int(user_input("8-Chat-Bot"))
                Check = Input_Checker(user, [1 ,2 ,3, 4, 5, 6 ,7, 8])
                if (Check):
                    if user == 1:
                        print(f'{user_name} Age Is: {my_dict[user_name]["Age"]}')
                        Passexsist = True
                    elif user == 2:
                        print(f'{user_name} Race: Is {my_dict[user_name]["Race"]}')
                        Passexsist = True
                    elif user == 3:
                        print(f'{user_name} Password IS: {my_dict[user_name]["Password"]}')
                        Passexsist = True
                    elif user == 4:
                        print(f'{user_name} Gender Is: {my_dict[user_name]["Gender"]}')
                        Passexsist = True
                    elif user == 5:
                        print(my_dict[user_name])
                        Passexsist = True
                    elif user == 6:
                        Python_Code_Runner(r"F:\Samad\Code\Code Projects\Messanger\Messanger.py")
                        Passexsist = True
                    elif user == 7:
                        print("Which Game Do You Wanna Play \n1-Flappy-Bird\n2-Snake-Points")
                        Game = user_input("Enter Game Name Or Number")
                        if Game in ["Flappy-Bird", 'Flappy Bird', '1']:
                          Python_Code_Runner(r"F:\Samad\Code\Code Projects\Games\Flappy_Bird\flappy\main.py")
                          Passexsist = True
                        elif Game in ["Snake-Game", "Snake Game", '2']:
                              Python_Code_Runner(r"F:\Samad\Code\Code(Learning)\Python\Learning\Module\Pygame\Snake_Game\main.py")
                              Passexsist = True
                        else:
                            print(shutter("Huhh"))
                            Passexsist = True
                    
                    elif user == 8:
                        Chat_Bot()
                       
                else:
                    print("Enter A Valid Value")
            else:
                print("Incorrect Password")
        else:
            print("Incorrect Username")
            print("Do You Want To Create A New Account")
            New_Account = user_input("1-Yes, 2-No")
            if New_Account == '1':
                Register(my_dict, file_path, file_name)
                return True
            else:
                print("Good Bye")
                Passexsist = True
                return False


def Unknown():
    user = user_input("Enter The String")
    Len = len(user) # 6
    if Len > 34:
        Eva = Len - 34
    else:
        Eva = 34 - Len
    
    List = user.split()

    List1 = random_Items(List, Eva+3)
    return Join(List1, '', 's'), len(List1), len(user) 


def Function_Runner():
    import Functions
    import inspect
    user1 = input("Enter:")
    dir1 = dir(Functions)
    if user1 in dir1:
        func = getattr(Functions, user1)
        if inspect.signature(func).parameters:  # Check if the function has any parameters
            # If the function has parameters, ask the user for their values
            args = []
            for param in inspect.signature(func).parameters.values():
                arg = input(f"Enter value for '{param.name}': ")
                args.append(arg)
            result = func(*args)  # Call the function with the provided arguments
        else:
            result = func()  # Call the function with no arguments
        print(result)

def Chapter_Divs (directory, no_of_chapters, file_extn, two_file = [], name = ''):
    Change_Directory(directory)
    Folder_Creator(f"{name}", 1)
    Change_Directory(f'{directory}/{name}')
    Folder_Creator("Chapter", no_of_chapters)
    folders = os.listdir(f"{directory}/{name}")
    if two_file == []:
        for folder in folders:
                Change_Directory(f"{directory}/{name}/{folder}")
                with open(f'{folder}.{file_extn}', 'w'):
                    pass
    else:
         for folder in folders:
              Change_Directory(f"{directory}/{name}/{folder}")
              with open(f'{folder}.{file_extn}', 'w') as f:
                   pass
              with open(f'{folder}-Practice.{file_extn}', 'w') as f:
                   pass
              for i in range(len(two_file)):
                with open(f"{folder}.{two_file[i]}", 'w'):
                    pass


def Dict_Correct(msg):
    msg = Words_Capitalzer(msg)
    words = msg.split()
    corrected_words = []
    for word in words:
        if word in Dictionary:
            corrected_words.append(Dictionary[word]["Value"])
        else:
            corrected_words.append(word)
    corrected_msg = Join(corrected_words)
    return corrected_msg


def Folder_Org(directory): 
    Change_Directory(directory)
    list1 = list_G(directory)
    for items in list1:
        try:
            sp = items.split(".")
            try:
                Folder_Creator(sp[1],1)
                shutil.move(f"{directory}\{items}", f"{directory}\{sp[1]}\{items}")
            except FileExistsError:
                shutil.move(f"{directory}\{items}", f"{directory}\{sp[1]}\{items}")
        except IndexError:
            continue


if __name__ == "__main__":
    pass

 