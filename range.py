# Import random to create numbers
import random

# Import time module to run for a time lapse
import time

# Import pyttsx3 module
import pyttsx3

# Import datetime module know 
#import datetime

# One time initialization
engine = pyttsx3.init()

# Voices
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
br_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0"

def print_input():
    # Get a time input, and decide a voice language
    try:
        t = int(input("\nHow long do you want me to count (in minutes)? "))
    except ValueError:
        print("Sorry, I only accept numbers for that question.")
    else:
        print("\nSelect a language, E for English or P for Portuguese (BR).")
        v = input("E/P: ")

    if v.upper() == 'E': # If v same as E
        # Use female English voice
        engine.setProperty('voice', en_voice_id)
        b = "Thanks, thats all."
        speech_numbers(t,b)
    elif v.upper() == 'P': # If v same as P
        # Use female Brazilian voice
        engine.setProperty('voice', br_voice_id)
        b = "Obrigada, isto é tudo."
        speech_numbers(t,b)
    else:
        print("Sorry, I don't recgonize %s as an option." % (v.upper()))

def speech_numbers(t,b):
    # List 5000 random numbers between 0 and 5000.
    r = random.sample(range(5000), 5000)

    # Create an index = 0
    i = 0

    # Receive minutes
    t_out = timeout(t)

    while True:
        #print(datetime.datetime.now())
        print(r[i])
        engine.say(r[i])
        engine.runAndWait()
        time.sleep(1.5)
        i += 1
        if time.time() > t_out:
            break
    engine.say(b)
    engine.runAndWait()

def timeout(t):
    # Calculate a time minute based
    t_out = time.time() + 60 * t # 60 * t is our time in minutes.
    return t_out

### Main ###
print("###############################################")
print("#############  Count me to Sleep  #############")
print("###############################################")

print_input()

print("\n###############################################")
print("####################  End  ####################")
print("###############################################")
