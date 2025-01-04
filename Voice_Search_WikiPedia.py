# Python package supporting common text-to-speech engines 
import pyttsx3 

# For understanding speech 
import speech_recognition as sr 

# For fetching the answers to computational queries 
import wolframalpha 

# For fetching Wikipedia articles 
import wikipedia 

# Function to search the query that is either entered or spoken by the user 
def search(query): 
    try: 
        # Generate your App ID from WolframAlpha 
        app_id = "Your_WolframAlpha_App_ID_here"
        client = wolframalpha.Client(app_id) 
        res = client.query(query) 
        answer = next(res.results).text 
        print(answer) 
        SpeakText("Your answer is " + answer) 
        
    except Exception as e: 
        # If the query cannot be searched using WolframAlpha, search Wikipedia 
        print(f"WolframAlpha query failed: {e}")
        query = " ".join(query.split())
        SpeakText("I am searching for " + query) 
        
        try:
            result = wikipedia.summary(query, sentences=3)
            print(result) 
            SpeakText(result) 
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"Multiple results found for {query}. Please refine your query.")
        except wikipedia.exceptions.PageError:
            print(f"No Wikipedia page found for {query}.")
        except Exception as ex:
            print(f"An error occurred: {ex}")

# Function to convert text to speech 
def SpeakText(command): 
    # Initialize the engine 
    engine = pyttsx3.init() 
    engine.say(command) 
    engine.runAndWait() 

# Driver code 
query = input("Enter your query or leave blank to use voice input: ").strip().lower() 

# If query is blank, use voice input 
if not query: 
    r = sr.Recognizer() 
    with sr.Microphone() as source: 
        print("Say Something ") 
        r.adjust_for_ambient_noise(source, duration=2) 
        audio = r.listen(source) 

    try: 
        speech = r.recognize_google(audio) 
        search(speech) 

    except sr.UnknownValueError: 
        print("Google Speech Recognition could not understand audio") 

    except sr.RequestError as e: 
        print(f"Could not request results from Google Speech Recognition service; {e}") 
else: 
    search(query)
