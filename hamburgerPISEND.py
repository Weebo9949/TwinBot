import speech_recognition as sr #audio input
import pyttsx3 #text to speach
import pvporcupine #for low maintencence "sleep" mode
import pyaudio #for talking
import struct
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import random #for varible response 
import requests #for pinging online api
from geotext import GeoText #for city from str
import glob #responsible for grabbig file directory


#WE ARE MAKING FILE FUNCTION AND BLUEPRINT FUNCTION RIGHT NOW MAKE SEPERATE AND THEN COMBINE TO MAIN CODE
#REMEBER FILE DIRECTORY DIFFERENT IN LINUX 


# Sample training data
dataset = [
#greetings dataset
("good morning", "greeting"),
("hello there", "greeting"),
("hi", "greeting"),
("hey what's up", "greeting"),
("good afternoon", "greeting"),
("how are you doing", "greeting"),
("yo", "greeting"),
("hey buddy", "greeting"),
("what's good", "greeting"),
("sup", "greeting"),
("hey", "greeting"),
("what's up", "greeting"),
("howdy", "greeting"),
("greetings", "greeting"),
("good to see you", "greeting"),
("long time no see", "greeting"),
("how have you been", "greeting"),
("yo what's good", "greeting"),
("sup bro", "greeting"),
("hey man", "greeting"),
("good evening", "greeting"),
("nice to meet you", "greeting"),
("hi there", "greeting"),
("how's it going", "greeting"),
("hello again", "greeting"),
("hiya", "greeting"),
("hey there friend", "greeting"),
("alright mate", "greeting"),
("bonjour", "greeting"),
("hey hey hey", "greeting"),

#weather dataset 
("what's the weather like", "weather"),
("will it rain today", "weather"),
("is it sunny outside", "weather"),
("give me the weather report", "weather"),
("is it cold today", "weather"),
("what's the temperature", "weather"),
("is it going to snow", "weather"),
("how's the weather looking", "weather"),
("weather update please", "weather"),
("is it humid right now", "weather"),
("do I need a coat today", "weather"),
("is it hot outside", "weather"),
("what's the forecast", "weather"),
("is it raining right now", "weather"),
("what's the weather saying", "weather"),
("how's the weather today", "weather"),
("is there a storm coming", "weather"),
("should I bring an umbrella", "weather"),
("check the weather", "weather"),
("weather check please", "weather"),
("what's the sky like", "weather"),
("is it cloudy today", "weather"),
("how cold is it", "weather"),
("how hot is it", "weather"),
("is it nice out", "weather"),
("any rain today", "weather"),
("will it snow tomorrow", "weather"),
("temperature check", "weather"),
("is it breezy today", "weather"),
("what kind of weather are we getting", "weather"),

#turn off dataset
("turn off", "off"),
("shut down", "off"),
("power off", "off"),
("kill the assistant", "off"),
("shut up", "off"),
("stop talking", "off"),
("please go to sleep", "off"),
("hibernate", "off"),
("stop listening", "off"),
("turn yourself off", "off"),
("disable yourself", "off"),
("go offline", "off"),
("exit", "off"),
("terminate", "off"),
("shut yourself down", "off"),
("you can rest now", "off"),
("take a break", "off"),
("end session", "off"),
("disconnect", "off"),
("leave me alone", "off"),
("close the assistant", "off"),
("assistant off", "off"),
("turn off the ai", "off"),
("disable assistant", "off"),
("stop the program", "off"),
("kill switch", "off"),
("log off", "off"),
("mute yourself", "off"),
("cease operations", "off"),
("that's enough for now", "off")

]



engine = pyttsx3.init() #starting tts 

r = sr.Recognizer() #audio recognizer function

#vectorizing dataset to keywords 
X_texts, y_labels = zip(*dataset) 
vec = TfidfVectorizer()
X_vec = vec.fit_transform(X_texts)
#regression to predict intent 
clf = LogisticRegression()
clf.fit(X_vec, y_labels)

#voice command functions

#greeting response
def greeting():
    hello_responses = [ #hello dataset
    "What's up?",
    "Hey there!",
    "Sup!",
    "Wassup!",
    "Yo yo",
    "Ayo",
    "What’s good?",
    "How’s it going?"
]

    greet = random.choice(hello_responses) 
    engine.say(greet)
    engine.runAndWait()
    
#weather function (phrase = voice input str)
def weather(phrase):
    print(phrase)
    places = GeoText(phrase) #returns list of cities
    if len(places.cities) == 0: #str has no city 
        engine.say("error in trying to get weather did you mention a city?")
        return
    CITY = places.cities[0] #ONLY grabs one bug if there is more then one
    API_KEY = "c7e7ba849bc14fddaf4928991d2e2375" #from openapi 
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    response = requests.get(URL)
    data = response.json() #returned in json form 
    if response.status_code == 200:
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        engine.say(f"Today's weather in {CITY}: {temp}°C with {desc}.")
        print(f"Today's weather in {CITY}: {temp}°C with {desc}.") #formatting to a nice str
        engine.runAndWait()
    else:
        engine.say("error in trying to get weather are you connected to internet?")
        engine.runAndWait() #not pinged or ping made def filedirlist(datatype):
    if datatype == "jpg":
        filedirs = glob.glob("C:/Users/Luke/Desktop/HAMBURGERJPG/*.jpg")
        return(filedirs)
    if datatype == "py":
        filedirs = glob.glob("C:/Users/Luke/Desktop/HAMBUGERPY/*.py")
        return(filedirs)
    else:
        return("error invalid datatype")

#next two functions get the list of directories from predetermined folder
#then grabs the correct list
#to use give filedirpath filename and py or jpg and returns the directory of said file
def filedirlist(datatype):
    if datatype == "jpg":
        filedirs = glob.glob("C:/Users/Luke/Desktop/HAMBURGERJPG/*.jpg") #predetermined locations 
        return(filedirs)
    if datatype == "py":
        filedirs = glob.glob("C:/Users/Luke/Desktop/HAMBUGERPY/*.py")
        return(filedirs)
    else:
        return("error invalid datatype")

def filedirpath(filename, datatype): #checking for if requested name is in list of folder 
    dirlist = filedirlist(datatype) 
    for i in dirlist:
        if filename in i:
            return(i)
        else:
            pass
    return("error no such file")

#blueprint function():
#lets first make a function that opens directory stored in preset directory txt file
#focus on making this possible on the laptop first
#then learn a libary for gui for pi
#make this more efficent somehow? easiest for now
#needs to run independently from python run use subprocess and some libary for opening gui and file
#what datatype? png and jpg for sure but is pdf hard?

#nerd function():
#need sleeper api on laptop that allows for open end comm
#str of phrase from pi, shoots to laptop, laptop api has script to run ai and responds in str
#back maybe shc?(kinda messy) or a preset comm pathway (harder to store)
#all nice presents can be just done by asking ai very pog
#runs the entire audio input as long as "ask nerd" is in context
#what engine? lightweight might not sort output properly
#if bt how to handel bt on but laptop off edgecase
        
#python function():
#assuming file function() works from directory run a independent subprocess for python code
#realistic demand?
#run 1 as hamburger.py case 1 has to be listening to keyword to stop subprocess
#sounds like a shit loud of edgecasses T-T
#will work for no input required runs
#will work like ass for audio i/o probably
#how do we make the subprocess somehow have less authority from run 1
#big brain we run the python code from the lapop, thus the pi is simply waiying on a
#wait command for exicution to finish 




#predicting phrase intent
def predict_intent(text, threshold=0.50): #running libary with str text with 0.x tolerence 
    x = vec.transform([text]) #returns a list of prob of all datasets 
    probs = clf.predict_proba(x)[0]  # Get class probabilities
    max_prob = max(probs) 
    predicted_label = clf.classes_[probs.argmax()] #grabs label of max prob
    print(probs)
    
    if max_prob < threshold: #highest set is less then tolerence 
        return "unknown"
    return predicted_label

def mainloop(test): #main loop after waking up
    while test == True:   
        try:
            with sr.Microphone() as source: #mic function
                engine.say("speak now") #recall r = sr.Recognizer() #audio recognizer function
                engine.runAndWait()
                audio = r.listen(source) 
            wordssaid = r.recognize_google(audio) #audiofile into str 
            print(wordssaid)
            engine.say("your intent is"  + predict_intent(wordssaid)) #output check intent 
            engine.runAndWait()
            #calling each audio i/o function
            if predict_intent(wordssaid) == "off":
                engine.say("turning off")
                engine.runAndWait()
                test = False
            elif predict_intent(wordssaid) == "greeting":
                greeting()
            elif predict_intent(wordssaid) == "weather":
                weather(wordssaid)
        #audio input returns error (mushy wave)
        except sr.UnknownValueError:
            engine.say("i did not get that please try again")
            engine.runAndWait()
    print("loop ended")



#responsible for low demand sleep mode
porcupine = pvporcupine.create(
    access_key="DiprdecnIODRcbNOqeqyhtPJK8VXSsqiUd5JoVCzV8hKiNBNXOQeAQ==", #access key for sleep ai 
    keywords=["grapefruit"]  # keyword
)
pa = pyaudio.PyAudio()
stream = pa.open(
    rate=porcupine.sample_rate,           # How many samples per second to expect (Porcupine needs a specific value)
    channels=1,                            # Mono audio (1 mic channel)
    format=pyaudio.paInt16,               # Audio format: 16-bit PCM (what Porcupine expects)
    input=True,                            # We're recording audio (input mode)
    frames_per_buffer=porcupine.frame_length  # Buffer size = the chunk size Porcupine needs to process each time
)


print("listening to wake word")

try: #sleeping case
    while True:
        pcm = stream.read(porcupine.frame_length) #reading the room per fram rate 
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
        keyword_index = porcupine.process(pcm)

        if keyword_index >= 0: #if index is non zero wake
            print("Wake word detected!")
            test = True
            mainloop(test)

except KeyboardInterrupt: #wtf is the key for this???
    print("Stopping...")



finally: #wraps up sleeper "this should be gone in final model for instead
         #a loop that sends it back to sleep the script should end on a system shutdown 
    stream.stop_stream() 
    stream.close()
    pa.terminate()
    porcupine.delete()

