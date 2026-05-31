import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import requests
import smtplib
import os
import webbrowser

# -----------------------------
# Initialize Voice Engine
# -----------------------------

engine = pyttsx3.init()

def speak(text):

    print("Assistant:", text)

    engine.say(text)

    engine.runAndWait()

# -----------------------------
# Voice Input
# -----------------------------

def take_command():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    try:

        print("Recognizing...")

        command = recognizer.recognize_google(audio)

        command = command.lower()

        print("You said:", command)

        return command

    except Exception as e:

        print(e)

        speak("Sorry, I could not understand.")

        return ""

# -----------------------------
# Send Email
# -----------------------------

def send_email(receiver, message):

    try:

        sender_email = "your_email@gmail.com"
        sender_password = "your_password"

        server = smtplib.SMTP('smtp.gmail.com', 587)

        server.starttls()

        server.login(sender_email, sender_password)

        server.sendmail(sender_email, receiver, message)

        server.quit()

        speak("Email sent successfully")

    except Exception as e:

        print(e)

        speak("Unable to send email")

# -----------------------------
# Weather Information
# -----------------------------

def get_weather(city):

    api_key = "YOUR_OPENWEATHER_API_KEY"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)

    data = response.json()

    if data["cod"] == 200:

        temperature = data["main"]["temp"]

        weather = data["weather"][0]["description"]

        speak(f"The temperature in {city} is {temperature} degree Celsius")

        speak(f"The weather condition is {weather}")

    else:

        speak("City not found")

# -----------------------------
# Reminder
# -----------------------------

def set_reminder():

    speak("What should I remind you about?")

    reminder = take_command()

    with open("reminders.txt", "a") as file:

        file.write(reminder + "\n")

    speak("Reminder saved")

# -----------------------------
# Main Assistant
# -----------------------------

def run_assistant():

    speak("Advanced Voice Assistant Started")

    while True:

        command = take_command()

        # Greetings
        if "hello" in command:

            speak("Hello! How can I help you?")

        # Time
        elif "time" in command:

            current_time = datetime.datetime.now().strftime("%I:%M %p")

            speak(f"The current time is {current_time}")

        # Date
        elif "date" in command:

            current_date = datetime.datetime.now().strftime("%d %B %Y")

            speak(f"Today's date is {current_date}")

        # Open Google
        elif "open google" in command:

            speak("Opening Google")

            os.system("start https://www.google.com")

        # Open YouTube
        elif "open youtube" in command:

            speak("Opening YouTube")

            os.system("start https://www.youtube.com")

        # Search Web
        elif "search" in command:

            search_query = command.replace("search", "")

            speak(f"Searching for {search_query}")

            pywhatkit.search(search_query)

        # Wikipedia Questions
        elif "who is" in command or "what is" in command:

            try:

                result = wikipedia.summary(command, sentences=2)

                speak(result)

            except:

                speak("No information found")

        # Weather
        elif "weather" in command:

            speak("Please say the city name")

            city = take_command()

            get_weather(city)

        # Reminder
        elif "set reminder" in command:

            set_reminder()

        # Send Email
        elif "send email" in command:

            speak("Tell me the receiver email")

            receiver = input("Receiver Email: ")

            speak("What message should I send?")

            message = take_command()

            send_email(receiver, message)

        # Exit
        elif "stop" in command or "exit" in command:

            speak("Goodbye")

            break

        else:

            speak("Please say the command again")

# -----------------------------
# Run Assistant
# -----------------------------

run_assistant()