# Import random to create numbers
import random

# Import time module to run for a time lapse
import time

# Import pyttsx3 module
import pyttsx3

# One time initialization
engine = pyttsx3.init()

# Voices
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
br_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0"

# Get a time input, and decide a voice language
#try:
t = int(input("How long do you want me to count? "))
#except ValueError:
#    print("Sorry, I only accept numbers for that question.")
#else:
print("Select a language, E for English or P for Portuguese.")
v = input("E/P: ")

if v.upper() == 'E':
    # Use female English voice
    engine.setProperty('voice', en_voice_id)
    l = "And the last number..."
    b = "Thanks, thats all."
elif v.upper() == 'P':
    # Use female Brazilian voice
    engine.setProperty('voice', br_voice_id)
    l = "E o último número..."
    b = "Obrigada, isto é tudo."
else:
    print("Sorry, I don't recgonize %s as an option." % (v))
        
# Create 100 random numbers between 0 and 100.
r = random.sample(range(5000), 5000)

# Create an index = 0
i = 0

# While loop to speech number
while t != 0:
    print(r[i])
    engine.say(r[i])
    engine.runAndWait()
    time.sleep(1)
    i += 1
    t -= 1
#print(r[-1])
#engine.say(l)
#engine.say(r[-1])
engine.say(b)
engine.runAndWait()
