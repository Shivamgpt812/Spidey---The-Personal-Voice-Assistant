import datetime
import speak
import webbrowser
import weather
import os




def Action(send) :   
  
    data_btn  = send.lower()

    if "what is your name" in   data_btn :
      speak.speak("My name is Spidey your Personal Virtual Assistant")  
      return "My name is Spidey your Personal Virtual Assistant"

    elif "hello" in data_btn  or "hye" in data_btn  or "hay" in data_btn or "hey" in data_btn: 
        speak.speak("Hey sir, How i can  help you !")  
        return "Hey sir, How i can  help you !" 

    elif "how are you" in  data_btn or  "how are you?" in data_btn or  "what's up?" in data_btn  :
            speak.speak("I am doing great these days sir") 
            return "I am doing great these days sir"   

    elif "thank you" in data_btn or "thank" in data_btn:
           speak.speak("its my pleasure sir to stay with you")
           return "its my pleasure sir to stay with you"      

    elif "good morning" in data_btn:
           speak.speak("Good morning sir, i think you might need some help")
           return "Good morning sir, i think you might need some help"

    elif "good afternoon" in data_btn:
           speak.speak("Good afternoon sir, i think you might need some help")
           return "Good afternoon sir, i think you might need some help"

    elif "good evening" in data_btn:
           speak.speak("Good evening sir, i think you might need some help")
           return "Good evening sir, i think you might need some help"   
    
    elif "good night" in data_btn:
           speak.speak("Good night sir, Sweetest dreams of your girlfriend")
           return "Good night sir, Sweetest dreams of your girlfriend"

    elif "time" in data_btn  or  "what is the time?" in data_btn or  "what is the time" in data_btn or  "what's the time?" in data_btn:
          current_time = datetime.datetime.now()
          Time = (str)(current_time.hour)+ " Hour : ", (str)(current_time.minute) + " Minute" 
          speak.speak(Time)
          return str(Time) 

    elif "shutdown" in data_btn or "quit" in data_btn or "bye" in data_btn or "goodbye" in data_btn:
            speak.speak("bye sir")
            return "bye sir"  

    elif "play music" in data_btn or "song" in data_btn:
        webbrowser.open("https://gaana.com/")   
        speak.speak("gaana.com is now ready for you, enjoy your music")                   
        return "gaana.com is now ready for you, enjoy your music"


    elif 'open google' in data_btn or 'google'  in data_btn:
        url = 'https://google.com/'
        speak.speak("Opening Google, Sir")  
        webbrowser.get().open(url)
        return "google open"

    elif 'youtube' in data_btn or "open youtube" in  data_btn:
        url = 'https://youtube.com/'
        speak.speak("Opening Youtube, Sir") 
        webbrowser.get().open(url)
        return "YouTube open"    
    
    elif 'github' in data_btn or "open github" in  data_btn:
        url = 'https://github.com/Shivamgpt812'
        speak.speak("Opening GitHub, Sir") 
        webbrowser.get().open(url)
        return "GitHub open" 
    
    elif 'weather' in data_btn or "How is the weather?" in data_btn :
       ans   = weather.Weather()
       speak.speak(ans) 
       return ans

    elif 'music from my laptop' in data_btn:
        url = 'D:\\music' 
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        speak.speak("songs playing...")
        return "songs playing..." 

    else :
        speak.speak( "i'm unable to understand!")
        return "i'm unable to understand!"       

