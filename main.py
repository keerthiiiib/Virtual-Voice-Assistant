import pyttsx3
import speech_recognition as sr
import datetime
import pywhatkit as kit
import weather
import jokes
import news
import movie_recommendation
import music
import emails
import screenshots
import images

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak a text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to voice commands
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        command = ""
        try:
            command = recognizer.recognize_google(audio)
            print(f"Recognized: {command}")
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
        return command.lower()

# Main function to process commands
def run_assistant():
    speak("Hello, how can I assist you today?")
    while True:
        command = listen()

        if 'time' in command:
            speak(f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}")

        elif 'date' in command:
            speak(f"Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')}")

        elif 'weather' in command:
            weather_info = weather.get_weather()
            speak(weather_info)

        elif 'joke' in command:
            joke = jokes.get_joke()
            speak(joke)

        elif 'news' in command:
            news_info = news.get_latest_news()
            speak(news_info)

        elif 'open google' in command:
            kit.playonyt("Google")

        elif 'movie' in command:
            recommendation = movie_recommendation.get_movie_recommendation()
            speak(f"How about watching {recommendation}.")

        elif 'music' in command:
            music.play_music()

        elif 'screenshot' in command:
            screenshots.take_screenshot()

        elif 'generate image' in command:
            images.generate_image()

        elif 'email' in command:
            emails.send_email()

        elif 'exit' in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    run_assistant()
