from deep_translator import GoogleTranslator #Imported google translator from deep_translator module.
from os import getcwd #Module that gets current path of main.py.

print("Welcome to my translator. Insert name of the file like this: example.txt")
while True: #While loop for repeatability
    lang_list = GoogleTranslator.get_supported_languages() #This variable holds all available languages.
    name = input("Insert name of the file: ") #Name of user's file for translation.
    path = getcwd() + "\\" + name #Path for opening user's file.
    try: #Try/except to take care of errors caused by non-existent file.
        with open(path, "r") as tr_file: #Opening user's file for reading to get lines for translation.
            try: #Try/except to take care of errors caused by choosing non-existing language, typos etc.
                with open("translated_" + name, "w") as translated: #Creating new file to save translated lines.
                    print("""\nDisclaimer: Because of encoding issues, not all languages will work.
Here are few that worked for me: basque, polish, german, english, czech, irish""")
                    tr_to = input("Choose language that you want to translate your file to: ") #User's choice of language for translation.
                    progress = 0 #Variable for showing listing line that's currently being translated.
                    for line in tr_file.readlines(): #For loop that iterates over all lines in user's file.
                        progress += 1  # Adding 1 for every line that's been translated.
                        translated_line = GoogleTranslator(source="auto", target=tr_to).translate(line) + "\n" #Translating line
                        translated.write(translated_line) #Writing translated lines into new file.
                        print(f"Translating line {progress}","\nOriginal sentence:\n",line,"\nTranslation: \n",translated_line)
                print(f"All {progress} lines were translated successfully.") #Translation completed message.
            except Exception as err: #Takes care of error caused when choosing language for translation.
                print("Something went wrong.")
                print(err) #Prints error message.
    except FileNotFoundError: #Takes care of error caused by wrong file name.
        print(f"File {path} does not exist.")
    finally: #Asks if user wants to end the program or continue to translation of another file.
        if input("Do you want to continue?(Y/N): ") == "N":
            break
