'''#--------------------------->
import pyttsx3
sound=pyttsx3.init()
def speak_test(text):
    sound.say(text)
speak_test("hello i'm your AI assistent")
speak_test("mike testing 1 2 3")
sound.runAndWait()

#-------------------------->
import pyttsx3
sound=pyttsx3.init()
def speak_text():
    sound.say(text)
user_text=input("Enter your messgae : ").lower()
name="user"
if "my name is" in user_text:
    name=user_text.split("my name is")[-1].strip()
elif "name is" in user_text:
    name=user_text.split("name is")[-1].strip()
if user_text in["hi","hello","hay"]:
    response="hello! how can i help you?"
elif "name" in user_text:
    response=f"Hello {name} !,how can i hlep you"
else:
    response=" sorry i didn't understand that"
print(response)
sound.runAndWait()
#-------------------------->'''













