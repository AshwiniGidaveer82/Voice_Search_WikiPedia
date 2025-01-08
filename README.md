**Importing Required Libraries**
import pyttsx3 : This is a text-to-speech conversion library in Python. It allows you to convert text into speech using different voices and adjust the speech rate or volume.
import speech_recognition as sr : This library helps in recognizing speech input from a microphone. It supports various speech recognition engines like Google Speech Recognition.
import wolframalpha : This library allows you to retrieve summaries or specific content from Wikipedia articles.

**Defining the search Function**
def search(query): This function processes the user’s query and tries to provide an answer using WolframAlpha first, and then Wikipedia if necessary.

**Using WolframAlpha**
try:
    app_id = "Your_WolframAlpha_App_ID_here" => [ Unique identifier required to access WolframAlpha’s API. Replace "Your_WolframAlpha_App_ID_here" with your actual API key.]

    client = wolframalpha.Client(app_id) => [ This creates a WolframAlpha client instance to query the API.]
    
    res = client.query(query) => [ The user’s input is sent to WolframAlpha for computation.]

        answer = next(res.results).text => [ Extracts the first result (if available) from the WolframAlpha response.]

            print(answer)
            SpeakText("Your answer is " + answer) => [ Displays the computed result. Converts the result into speech and speaks it aloud.]
                        
**Fallback to Wikipedia**

                except Exception as e:
                    print(f"WolframAlpha query failed: {e}")=> [ If WolframAlpha fails (e.g., due to incorrect input or API issues), an exception is caught, and Wikipedia is used instead.]

                    query = " ".join(query.split()) => [ Cleans up the query string by removing extra spaces.]

                        SpeakText("I am searching for " + query) => [ Announces that Wikipedia is being searched.]

                            try:
                            result = wikipedia.summary(query, sentences=3) => [ Retrieves the first three sentences of a Wikipedia article summary matching the query.]

                                print(result)
                                SpeakText(result) => [ Displays and speaks the summary.]
                                    
**Handling Wikipedia Errors**

                                except wikipedia.exceptions.DisambiguationError as e:
                                print(f"Multiple results found for {query}. Please refine your query.") => [ Occurs if there are multiple possible matches for the query.]

                                  except wikipedia.exceptions.PageError:
                                    print(f"No Wikipedia page found for {query}.") => [ Triggered when no page is found for the given query.]

                                        except Exception as ex:
                                         print(f"An error occurred: {ex}") => [ Handles any other unexpected errors.]

**Text-to-Speech Function**
                                         def SpeakText(command): => [ Converts the given text (command) into speech.]

                                          engine = pyttsx3.init() => [ Initializes the pyttsx3 speech engine.]

                                            engine.say(command) => [ Prepares the text to be spoken.]

                                                engine.runAndWait() [ Executes the speech playback.]
                                                
**Driver Code
User Query Input**
                                                    query = input("Enter your query or leave blank to use voice input: ").strip().lower() => [ Prompts the user to enter a text query or leave it blank for voice input.]
                                                    

**Voice Input if Query is Blank**                                                   
                                                        if not query: => [ If no query is entered, the code listens for voice input.]

                                                         r = sr.Recognizer() => [ Creates a speech recognizer instance.]

                                                            with sr.Microphone() as source:
                                                             print("Say Something") => [ Activates the microphone and prompts the user to speak.]

                                                              r.adjust_for_ambient_noise(source, duration=2) => [ Adjusts the recognizer for background noise.]
                                                                                                     
                                                                audio = r.listen(source) => [ Records the user's speech.]
                                                                                                             
**Processing Voice Input**                                          try:
                                                                    speech = r.recognize_google(audio)
                                                                    search(speech) => [ Converts speech to text using Google Speech Recognition and passes it to the search function.]

                                                                     except sr.UnknownValueError:
                                                                      print("Google Speech Recognition could not understand audio") => [ Handles cases where the speech is not clear.]

                                                                        except sr.RequestError as e:
                                                                        print(f"Could not request results from Google Speech Recognition service; {e}") => [ Handles network or service errors.]

                                                                        else:
                                                                        search(query) => [ If the user enters a text query, it is directly passed to the search function.]




   



                        




                                                                    










